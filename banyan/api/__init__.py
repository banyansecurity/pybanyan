"""
The `banyan.api` module contains classes and methods that do the work of actually interacting with the Banyan
Command Center, translating JSON responses into objects from the :py:mod:`banyan.model` module.
"""
import configparser
import logging
import os
import sys
from pathlib import Path
from typing import Dict, Any, List, Union, Callable

import urllib3
import requests
from cement import init_defaults
from requests.auth import AuthBase

from banyan.api.attachment import AttachmentAPI
from banyan.api.audit import AuditAPI
from banyan.api.device import DeviceAPI
from banyan.api.event_v2 import EventV2API
from banyan.api.netagent import NetagentAPI
from banyan.api.policy import PolicyAPI
from banyan.api.role import RoleAPI
from banyan.api.service import ServiceAPI
from banyan.api.service_web import ServiceWebAPI
from banyan.api.service_infra import ServiceInfraAPI
from banyan.api.shield import ShieldAPI
from banyan.api.user import UserAPI
from banyan.api.cloud_resource import CloudResourceAPI
from banyan.core.exc import BanyanError

JsonListOrObj = Union[List, Dict]
ProgressCallback = Callable[[str, str, int, int, List[JsonListOrObj]], None]


class BanyanApiClient:
    """
    Main class for interacting with the Banyan API.

    :param api_server_url: URL for the Banyan Command Center. This should be the same as the
        URL you enter in your browser to log into the Command Center. If not supplied, we will
        look for an environment variable named :envvar:`BANYAN_API_URL`; if that is also not present,
        the URL defaults to <https://net.banyanops.com>.
    :type api_server_url: str
    :param refresh_token: Initial API token used to authorize the connection. The refresh token
        will then be exchanged for an access token. If not supplied, we look for an environment
        varialbe named :envvar:`BANYAN_REFRESH_TOKEN`; if that is also not present, it causes a
        :py:exc:`BanyanError`.
    :type refresh_token: str
    :param debug: If True, extra debugging output from the Requests module will be logged.
    :type debug: bool
    :param log: Optional logger to use in debug mode. If not provided, the standard
        logger will be used.
    :type log: logging.Logger
    :raises: :py:exc:`BanyanError` if no refresh token is provided.
    """

    DEFAULT_API_URL = 'https://net.banyanops.com'
    """
    Default API server URL if none is specified and if a :envvar:`BANYAN_API_URL` environment variable
    is not found.
    """

    JSON_TYPE = 'application/json'
    """
    Default MIME content type for all requests and responses.
    """

    class _Auth(AuthBase):
        """
        Internal class for storing API tokens.
        :meta private:
        """

        def __init__(self, parent) -> None:
            self._obj = parent

        def __call__(self, r: requests.Request) -> requests.Request:
            token = self._obj.access_token or self._obj.refresh_token
            r.headers['Authorization'] = f'Bearer {token}'
            return r

    def __init__(self, api_server_url: str = None, refresh_token: str = None, debug: bool = False,
                 log: logging.Logger = None) -> None:
        self._debug = debug
        self._log = log
        self._progress_callback = None
        self._access_token = None
        self._insecure_tls = False
        self._api_url = self._normalize_url(api_server_url or os.getenv('BANYAN_API_URL') or
                                            BanyanApiClient.DEFAULT_API_URL)
        self._refresh_token = refresh_token or os.getenv('BANYAN_REFRESH_TOKEN')
        if not self._refresh_token:
            self._read_config_file()
        if not self._refresh_token:
            raise BanyanError("Refresh token must be set")
        if self._debug:
            requests_log = logging.getLogger('requests.packages.urllib3')
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
        self._http = self._create_session()        
        self._services = ServiceAPI(self)
        self._policies = PolicyAPI(self)
        self._attach = AttachmentAPI(self)
        self._roles = RoleAPI(self)
        self._shields = ShieldAPI(self)
        self._agents = NetagentAPI(self)
        self._users = UserAPI(self)
        self._devices = DeviceAPI(self)
        self._events = EventV2API(self)
        self._audit = AuditAPI(self)
        self._cloud_resources = CloudResourceAPI(self)
        self._services_web = ServiceWebAPI(self)
        self._services_infra = ServiceInfraAPI(self)

    def __del__(self):
        if self._http:
            try:
                self._http.close()
            except Exception:
                pass
            finally:
                self._http = None

    def _read_config_file(self):
        conf_path = Path.home() / '.banyan.conf'
        if conf_path.exists():
            try:
                cp = configparser.ConfigParser(CONFIG)
                cp.read(conf_path)
                self._api_url = self._normalize_url(cp.get('banyan', 'api_url'))
                self._refresh_token = cp.get('banyan', 'refresh_token')
            except configparser.Error:
                pass

    # noinspection PyMethodMayBeStatic
    def _normalize_url(self, url: str) -> str:
        if '/api' not in url:
            url += '/api/v1'
        return url

    def _create_session(self) -> requests.Session:
        http = requests.session()
        http.headers['Accept'] = 'application/json'
        http.auth = self._Auth(self)
        if self._debug:
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
        return http

    def get_access_token(self) -> str:
        """
        Forces the client to obtain a new access token. This method is provided for testing. You should not need
        to call it, as the client will automatically fetch an access token when needed.

        :return: the new access token.
        :raises: :py:exc:`BanyanError` if the refresh token is invalid.
        """
        content = self._request('POST', '/refresh_token').json()
        self._access_token = content['Message']
        return self._access_token

    def _request(self, method: str, url: str, params: Dict[str, Any] = None, data: Any = None,
                 headers: Dict[str, str] = None, cookies: Dict[str, str] = None,
                 files=None, auth=None, timeout=None, allow_redirects=True, proxies=None,
                 hooks=None, stream=None, verify=None, cert=None, json=None) -> requests.Response:
        if '://' not in url:
            url = self._api_url + url
        if '/v2/' in url:
            url = url.replace('/api/v1', '/api/experimental')
        if self._insecure_tls and not verify:
            verify = False
            urllib3.disable_warnings()
        else:
            urllib3.warnings.resetwarnings()

        headers = headers or dict()
        headers['Accept'] = 'application/json'
        response = requests.request(
            method=method, url=url, params=params, data=data, headers=headers, cookies=cookies, files=files,
            auth=auth or self._http.auth, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies,
            hooks=hooks, stream=stream, verify=verify, cert=cert, json=json)
        if response.status_code >= 400:
            try:
                content = response.json()
                if 'Message' in content:
                    raise BanyanError(f'{response.status_code} Client Error: {response.reason} for '
                                      f'url: {response.url}: {content["Message"]}')
                elif 'error' in content:
                    raise BanyanError(f'{response.status_code} Client Error: {response.reason} for '
                                      f'url: {response.url}: {content["error_code"]}: {content["error"]}')
            except ValueError:
                raise BanyanError(f'{response.status_code} Client Error: {response.reason} for url: {response.url}')
        return response

    def api_request(self, method: str, uri: str, params: Dict[str, Any] = None, data: Any = None,
                    json: str = None, headers: Dict[str, str] = None, accept: str = None) -> JsonListOrObj:
        """
        Sends an API request to Banyan and parses the response. All responses are assumed to be in JSON format.

        .. note:: This method is meant to be called by methods in various resource API classes (e.g.
           :py:class:`PolicyAPI`). You do not need to call :py:meth:`api_request` directly unless you
           are calling an endpoint not currently implemented in this library.

        :param method: HTTP method to execute (e.g. `GET`, `POST`, `HEAD`, `DELETE`, etc.)
        :type method: str
        :param uri: Relative URI or absolute URL endpoint. If a relative URI is provided, it is appended
            to the :py:meth:`api_url` property.
        :type uri: str
        :param params: Optional query string parameters.
        :type params: Dict[str, str]
        :param data: Data to be serialized in JSON format and sent in the body of a `POST` request.
        :param json: Pre-serialized JSON data to be sent in the body of the request. Note that only one of
            `data` or `json` should be supplied.
        :type json: str
        :param headers: Additional headers to be sent with the HTTP request. The library
            automatically adds `Content-Type` and `Authorization` headers.
        :type headers: Dict[str, str]
        :param accept: Content type to expect in the response. If not supplied, the response is assumed
            to be in `application/json` format.
        :type accept: str
        :return: returns the raw Response object from the `Requests` module.
        :rtype: requests.Response
        """
        if not self._access_token:
            self.get_access_token()
        headers = headers or dict()
        headers['Accept'] = accept or self.JSON_TYPE
        if data:
            headers['Content-Type'] = self.JSON_TYPE

        with self._request(method=method, url=uri, params=params, data=data, headers=headers, json=json) as response:
            resp = response.json()
            if '/v2/' in uri:
                return resp['data']
            return resp

    @property
    def progress_callback(self) -> ProgressCallback:
        return self._progress_callback

    @progress_callback.setter
    def progress_callback(self, value: ProgressCallback) -> None:
        self._progress_callback = value

    def _do_progress_callback(self, callback_func: ProgressCallback, method: str, uri: str, count: int, total: int,
                              partial_results: List[JsonListOrObj]) -> None:
        if callback_func:
            try:
                callback_func(method, uri, count, total, partial_results)
            except Exception as ex:
                err_msg = f'{ex.__class__.__name__} exception in progress callback: {ex.args[0]}'
                if self._log:
                    self._log.error(err_msg)
                else:
                    print(err_msg, file=sys.stderr)

    def paged_request(self, method: str, uri: str, params: Dict[str, Any] = None, data: Any = None,
                      json: str = None, headers: Dict[str, str] = None, accept: str = None,
                      progress_callback: ProgressCallback = None) -> JsonListOrObj:
        params = params or dict()
        skip = params.get('skip', 0)
        limit = params.get('limit', 1000)
        all_results = list()
        callback = progress_callback or self._progress_callback

        while True:
            params['skip'] = skip
            params['limit'] = limit
            results = self.api_request(method, uri, params, data, json, headers, accept)
            for key in results.keys():
                logging.debug('Looking for %s in %s', key, uri)
                if key in uri or key == 'data' or key == 'result':
                    if len(results[key]) == 0:
                        return all_results
                    all_results.extend(results[key])
                    logging.debug('Found %s, result count = %d, total count = %d',
                                  key, len(results[key]), len(all_results))
                    self._do_progress_callback(callback, method, uri, len(all_results),
                                               results.get('count', -1), results[key])
                    skip += limit

    @property
    def access_token(self) -> str:
        """
        Gets the current access token.
        """
        return self._access_token

    @property
    def refresh_token(self) -> str:
        """
        Gets/sets the refresh token, which is exchanged for an access token that allows us to actually make
        API calls.
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value: str) -> None:
        self._refresh_token = value
        if self._access_token:
            self._access_token = None

    @property
    def api_url(self) -> str:
        """
        Gets/sets the API server URL. Useful if the URL is not known at instantiation time.
        If an access token has already been obtained, it will be discarded after resetting this property.
        The next API request will result in a new access token being issued.
        """
        return self._api_url

    @api_url.setter
    def api_url(self, value: str) -> None:
        self._api_url = self._normalize_url(value)
        self._access_token = None

    @property
    def insecure_tls(self) -> bool:
        return self._insecure_tls

    @insecure_tls.setter
    def insecure_tls(self, value: bool) -> None:
        self._insecure_tls = value

    @property
    def services_web(self) -> ServiceWebAPI:
        """
        Returns an instance of the :py:class:`ServiceWebAPI` class, which can be used to manage Banyan hosted websites.
        """
        return self._services_web

    @property
    def services_infra(self) -> ServiceInfraAPI:
        """
        Returns an instance of the :py:class:`ServiceInfraAPI` class, which can be used to manage Banyan infra services.
        """
        return self._services_infra        

    @property
    def services(self) -> ServiceAPI:
        """
        Returns an instance of the :py:class:`ServiceAPI` class, which can be used to manage Banyan services.
        """
        return self._services

    @property
    def policies(self) -> PolicyAPI:
        """
        Returns an instance of the :py:class:`PolicyAPI` class, which can be used to manage Banyan security policies.
        """
        return self._policies

    @property
    def roles(self) -> RoleAPI:
        """
        Returns an instance of the :py:class:`RoleAPI` class, which can be used to manage Banyan roles.
        """
        return self._roles

    @property
    def attachments(self) -> AttachmentAPI:
        """
        Returns an instance of the :py:class:`AttachmentAPI` class, which can be used to query which policies
        are attached to services.
        """
        return self._attach

    @property
    def shields(self) -> ShieldAPI:
        """
        Returns an instance of the :py:class:`ShieldAPI` class, which can be used to get information about
        Banyan Shields.
        """
        return self._shields

    @property
    def netagents(self) -> NetagentAPI:
        """
        Returns an instance of the :py:class:`NetagentAPI` class, which can be used to manage Banyan netagents
        in AccessTier mode or Host mode.
        """
        return self._agents

    @property
    def users(self) -> UserAPI:
        """
        Returns an instance of the :py:class:`UserAPI` class, which can be used to manage Banyan users.
        """
        return self._users

    @property
    def devices(self) -> DeviceAPI:
        """
        Returns an instance of the :py:class:`DeviceAPI` class, which can be used to manage devices such
        as laptops and tablets.
        """
        return self._devices

    @property
    def events(self) -> EventV2API:
        return self._events

    @property
    def audit(self) -> AuditAPI:
        return self._audit

    @property
    def cloud_resources(self) -> CloudResourceAPI:
        return self._cloud_resources


# configuration defaults
CONFIG = init_defaults('banyan')
CONFIG['banyan']['api_url'] = BanyanApiClient.DEFAULT_API_URL
CONFIG['banyan']['refresh_token'] = None


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    c = BanyanApiClient(api_server_url='https://gcstage.banyanops.com',
                        refresh_token=os.getenv('BANYAN_REFRESH_TOKEN'), debug=True)
    print(c.get_access_token())
    print(c.services.list())
