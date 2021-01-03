import os
import re
import socket
import textwrap
import urllib.parse
from collections import namedtuple
from dataclasses import dataclass, field
from typing import Optional, List

import dns.resolver
import requests
import requests.exceptions
from colorama import Style, Fore

from banyan.api import BanyanApiClient
from banyan.model.service import Service, BackendTarget
from banyan.model.netagent import Netagent
from banyan.lib.cloud import get_cloud_vendor
from banyan.lib.cloud.aws import AwsCloud
from banyan.lib.certs import CertPair

DEFAULT_TIMEOUT = 0.5
DEFAULT_DNS_SERVER = '8.8.8.8'


@dataclass
class TestResult:
    passed: bool
    details: str = ''
    info: List[str] = field(default_factory=list)


class ServiceTest:
    def __init__(self, service: Service, client: BanyanApiClient, timeout: float = DEFAULT_TIMEOUT,
                 external_dns_server: str = DEFAULT_DNS_SERVER,
                 wildcard_hostname: Optional[str] = None):
        self._service = service
        self._client = client
        self._timeout = timeout
        self._ext_dns = external_dns_server
        self._wildcard = wildcard_hostname
        self._my_hostname = socket.gethostname()
        self._agent = self._find_access_tier()
        self._vendor = get_cloud_vendor()
        self._cloud = self._get_cloud()
        self._dns_name = self._cloud.get_public_dns_name()

        self._resolver = dns.resolver.Resolver(configure=False)
        self._resolver.nameservers = [self._ext_dns]
        answers = self._resolver.resolve(self._dns_name, 'A', search=False)
        self._external_ips = [x.address for x in answers]

    def _find_access_tier(self) -> Netagent:
        for agent in self._client.netagents.list():  # type: Netagent
            if agent.hostname == self._my_hostname:
                return agent
        raise RuntimeError(f'Unable to find a netagent with hostname {self._my_hostname}')

    def _get_cloud(self) -> AwsCloud:
        if self._vendor == 'aws':
            return AwsCloud()
        else:
            raise RuntimeError(f'Cloud vendor "{self._vendor} is not supported')

    @property
    def _cert_dns_names(self) -> List[str]:
        return self._service.spec.cert_settings.dns_names

    @property
    def _dns_names(self) -> List[str]:
        return self._cert_dns_names or [self._service.metadata.tags.domain]

    @property
    def _target(self) -> BackendTarget:
        return self._service.spec.backend.target

    @staticmethod
    def _multimatch(value: str, multi_string: str) -> bool:
        return any([x.strip() == value for x in multi_string.split('|')])

    def _backend_hostname(self) -> str:
        host = self._target.name
        template_pattern = re.compile('{{([^}]*)}}')
        while '{{' in host:
            if not self._wildcard:
                raise RuntimeError(
                    'Service target contains a template. You must specify a value for the --wildcard option.')
            match = template_pattern.search(host)
            template_tokens = match.group(1).strip().split()
            if template_tokens[0] == '.Name':
                host = host.replace(match.group(0), self._wildcard)
            elif template_tokens[0] == 'index' and template_tokens[1] == '.Parts':
                index = int(template_tokens[2])
                host_tokens = self._wildcard.split(self._target.name_delimiter)
                host = host.replace(match.group(0), host_tokens[index])
        if host in self._service.spec.backend.dns_overrides.keys():
            host = self._service.spec.backend.dns_overrides[host]
        return host

    def run(self):
        print(f'Testing service {self._service.name} on host {self._my_hostname}:\n')
        print(f'Cloud vendor:        {self._vendor}')
        print(f'External hostname:   {self._dns_name}')
        print(f'External IPs:        {self._external_ips}')
        print()
        test_methods = [x for x in dir(self) if x.startswith('_test_')]
        for method_name in sorted(test_methods):
            method = getattr(self, method_name)
            docstring = method.__doc__
            print(docstring, end='... ')
            result: TestResult = method()
            print(f'{Fore.GREEN}PASSED' if result.passed else f'{Fore.RED}FAILED', end='')
            print(Style.RESET_ALL)
            if not result.passed:
                print(Fore.RED, end='')
                if result.details:
                    print(result.details)
                for info in result.info:
                    print(f'  * {info}')
                print(Style.RESET_ALL, end='')

    def _test_10_service_applies_here(self) -> TestResult:
        """Selected service applies to this netagent"""
        result = TestResult(True)
        matches = list()
        for i, selector in enumerate(self._service.spec.attributes.host_tag_selector):
            match = True
            for key, value in selector.items():
                if key in self._agent.host_tags.keys() and not self._multimatch(self._agent.host_tags[key], value):
                    match = False
                    result.info.append(
                        f'Selector {i}: {key}: {value} (expected) != {self._agent.host_tags[key]} (actual)')
            matches.append(match)
        if not any(matches):
            result.passed = False
            result.details = 'This netagent does not match any of the host tag selectors defined in the service ' \
                             'spec. Further results from this test may not be meaningful.'
        return result

    def _test_20_dns_names_match_tls_sni(self) -> TestResult:
        """DNS names in certificate match TLS SNI settings"""
        cert_names = set(self._service.spec.cert_settings.dns_names)
        sni_names = set(self._service.spec.attributes.tls_sni)
        if cert_names == sni_names:
            return TestResult(True)
        else:
            return TestResult(False, f'The DNS names in the service spec {list(cert_names)} do not match '
                                     f'the values specified for the TLS SNI header {list(sni_names)}. '
                                     f'Normally these should be the same.')

    def _test_30_meta_domain_matches(self) -> TestResult:
        """Meta domain matches DNS and TLS SNI settings"""
        meta_name = self._service.metadata.tags.domain
        cert_names = self._service.spec.cert_settings.dns_names
        sni_names = self._service.spec.attributes.tls_sni
        if meta_name in cert_names and meta_name in sni_names:
            return TestResult(True)
        else:
            return TestResult(False, f'The domain name "{meta_name}" in the service metadata was missing from '
                                     f'either the DNS names of the service spec {cert_names} or the TLS SNI '
                                     f'header values {sni_names}.')

    def _test_40_meta_port_in_ports(self) -> TestResult:
        """Meta port matches frontend listener port configuration"""
        meta_port = int(self._service.metadata.tags.port)
        frontend_ports = [int(x.port) for x in self._service.spec.attributes.frontend_addresses]
        if meta_port in frontend_ports:
            return TestResult(True)
        else:
            return TestResult(False, f'The port number in the service metadata ({meta_port}) does not match '
                                     f'any of the frontend ports for the service ({frontend_ports}).')

    def _test_50_public_dns(self) -> TestResult:
        """Public DNS records for service name resolve to this Access Tier"""
        result = TestResult(True)
        for name in self._dns_names:
            try:
                answers = self._resolver.resolve(name, 'A', search=False)
                dns_results = [x.address for x in answers]
                if set(dns_results) != set(self._external_ips):
                    result.passed = False
                    result.info.append(f'Public DNS for {name} resolved to {dns_results} '
                                       f'instead of {self._external_ips}')
            except dns.resolver.NXDOMAIN:
                result.passed = False
                result.info.append(f'Public DNS query against {self._resolver.nameservers} for {name} '
                                   f'did not return any records')
        if not result.passed:
            result.details = f'One or more of the DNS names specified for this service ({self._dns_names}) ' \
                             f'does not have a public DNS record pointing to the IP addresses of this ' \
                             f'Access Tier ({self._external_ips})'
        return result

    def _test_60_custom_tls_cert(self) -> TestResult:
        """Custom TLS cert exists (if specified) and is correct"""
        result = TestResult(True)
        custom_tls = self._service.spec.cert_settings.custom_tls_cert
        if custom_tls.enabled:
            try:
                cert = CertPair(custom_tls.cert_file, custom_tls.key_file)
                for name in self._dns_names:
                    if not cert.is_name_match(name):
                        result.passed = False
                        result.details = 'The path points to a valid certificate, but the DNS names of the ' \
                                         'certificate do not match the DNS names configured for the service.'
                        result.info.append(f'Service DNS name {name} does not match names configured in '
                                           f'the certificate ({cert.get_names()})')
            except FileNotFoundError:
                result.passed = False
                result.details = f'One of the filenames configured for the custom certificate could not be found.'
                if not os.path.exists(custom_tls.cert_file):
                    result.info.append(f'Certificate file {custom_tls.cert_file} is missing')
                if not os.path.exists(custom_tls.key_file):
                    result.info.append(f'Private key file {custom_tls.key_file} is missing')
            except PermissionError:
                result.passed = False
                result.details = 'The path points to a valid certificate, but the certificate could not be read ' \
                                 'due to the file permissions.'
        return result

    def _tcp_connect(self) -> TestResult:
        host = self._backend_hostname()
        result = TestResult(True)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self._timeout)
        try:
            s.connect((host, int(self._target.port)))
        except socket.timeout:
            result.passed = False
            result.details = f'Connection to backend host {host} on port {self._target.port} timed out ' \
                             f'after {self._timeout} seconds.'
        finally:
            s.close()
        return result

    def _http_connect(self) -> TestResult:
        host = self._backend_hostname()
        result = TestResult(True)
        scheme = 'https' if self._target.tls else 'http'
        url = urllib.parse.urlunparse((scheme, f'{host}:{self._target.port}', '', '', '', ''))
        params = dict()
        if self._target.client_certificate:
            params['cert'] = ('netagent.crt', 'netagent.key')
        if self._target.tls_insecure:
            params['verify'] = False
        try:
            response = requests.get(url, timeout=self._timeout, **params)
            if response.status_code != 200:
                result.passed = False
                result.details = f'{scheme.upper()} connection to {host}:{self._target.port} succeeded, but the ' \
                                 f'request resulted in a status code {response.status_code}: {response.reason}.'
        except requests.exceptions.ConnectTimeout:
            result.passed = False
            result.details = f'{scheme.upper()} connection to {host}:{self._target.port} timed out ' \
                             f'after {self._timeout} seconds.'
        except requests.exceptions.ConnectionError as ex:
            result.passed = False
            result.details = f'{scheme.upper()} connection to {host}:{self._target.port} failed: {ex}.'
        return result

    def _test_70_backend_dns(self) -> TestResult:
        """Internal DNS records exist for backend host"""
        result = TestResult(True)
        name = self._backend_hostname()
        try:
            dns.resolver.resolve(name, 'A', search=True)
        except dns.resolver.NXDOMAIN:
            result.passed = False
            result.info.append(f'DNS for {name} did not return any records')
            result.details = f'Internal DNS for {name} did not resolve to any address records.'
        return result

    def _test_80_backend_connect(self) -> TestResult:
        """Connection to backend service"""
        if self._service.spec.http_settings.enabled:
            return self._http_connect()
        else:
            return self._tcp_connect()
