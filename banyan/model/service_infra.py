import dataclasses
from marshmallow_dataclass import dataclass
from banyan.model.service import *

@dataclass
class ServiceInfraBase:
    name: str = field(
        default=None,
        metadata={'required': True, 'help': 'Name of the service; use lowercase alphanumeric characters or "-"'}
        )
    description: str = field(
        default='ServiceInfraBase',
        metadata={'help': 'Description of the service'}
        )
    # deployment model
    cluster: str = field(
        default=None,
        metadata={'required': True, 'help': 'Name of the cluster used for your deployment; for Global Edge set to "global-edge", for Private Edge set to "cluster1"'}
        )
    access_tier: str = field(
        default=None,
        metadata={'required': True, 'help': 'Name of the access_tier which will proxy requests to your service backend; set to "" if using Global Edge deployment'}
        )
    connector: str = field(
        default=None,
        metadata={'required': True, 'help': 'Name of the connector which will proxy requests to your service backend; set to "" if using Private Edge deployment'}
        )
    # frontend
    domain: str = field(
        default=None,
        metadata={'required': True, 'help': 'The external-facing network address for this service; ex. website.example.com'}
        )
    port: int = field(
        default=8443,
        metadata={'ignored': True, 'help': 'The external-facing port for this service; set to 8443 for infrastructure services'}
        )
    # backend
    backend_http_connect: bool = field(
        default=False,
        metadata={'required': True, 'help': 'Client will specify backend address & port using HTTP Connect; set to False if using backend_domain'}
        )
    backend_domain: str = field(
        default='',
        metadata={'required': True, 'help': 'The internal network address where this service is hosted; ex. 192.168.1.2; set to "" if using backend_http_connect'}
        )
    backend_port: int = field(
        default='',
        metadata={'required': True, 'help': 'The internal port where this service is hosted; set to 0 if using backend_http_connect'}
        )
    # client proxy
    client_banyanproxy_listen_port: int = field(
        default=None,
        metadata={'help': 'Local listen port to be used by client proxy; if not specified, a random local port will be used'}
        )
    # TODO: backend_allowed_hostnames, backend_allowed_cidrs
    # TODO: ssh wildcard logic
    # in ui but ignore here - backend_target_delimiter, backend_domain_templating, ssh_write_config, user_override

    # sanity check params and update dependencies
    def _initialize(self):
        # basics
        if not self.name or not self.domain:
            raise Exception("Configuration Error! Need to specify name, domain.")
        # deployment model
        if not self.cluster:
            raise Exception("Configuration Error! Need to specify cluster.")
        if (not self.connector and not self.access_tier) or (self.connector and self.access_tier):
            raise Exception("Configuration Error! Need to specify either access_tier or connector.")
        # deployment model = private-edge
        if self.access_tier:
            self.connector = ""
        # deployment model = global-edge
        if self.connector:
            self.access_tier = "*"
        # backend connectivity
        if (self.backend_http_connect and self.backend_domain) or (not self.backend_http_connect and not self.backend_domain):
            raise Exception("Configuration Error! Need to specify either backend_http_connect or backend_domain.")
        if self.backend_domain and not self.backend_port:
            raise Exception("Configuration Error! Need to specify backend_domain and backend_port.")
        if self.backend_http_connect:
            self.backend_domain = ""
            self.backend_port = ""

    # argparse arguments in controller
    @classmethod
    def arguments(cls) -> list:
        args = []
        flds = dataclasses.fields(globals()[cls.__name__])
        for fld in flds:
            if fld.metadata.get("ignored"):
                continue
            # optional args are prefixed with "--", and should have valid defaults
            argname = fld.name if fld.metadata.get("required") else ("--" + fld.name)
            # help text should contain type
            helptext = f'(type: {fld.type.__name__}) {fld.metadata.get("help")}'
            arg = ([argname], dict(type = fld.type, help = helptext))
            args.append(arg)
        return args

    def service_obj(self) -> Service:
        self._initialize()
        tags = Tags(
            template = str(ServiceTemplate.TCP),
            user_facing = "true",
            protocol = "tcp",
            domain = self.domain,
            port = str(self.port),
            service_app_type = "", # child must override
            allow_user_override = True,
            description_link = ""
        )
        metadata = Metadata(
            name = self.name,
            friendly_name = None,
            description = self.description,
            cluster = self.cluster,
            tags = tags
        )
        frontend_address = FrontendAddress(
            port = str(self.port),
            cidr = None
        )
        attributes = Attributes(
            tls_sni = [self.domain],
            frontend_addresses = [frontend_address],
            host_tag_selector = [
                { "com.banyanops.hosttag.site_name": self.access_tier }
            ]
        )
        target = BackendTarget(
            name = self.backend_domain,
            port = str(self.backend_port),
            tls = False,
        )
        allow_pattern = AllowPattern(
            cidrs = [],
            hostnames = []
        )
        backend = Backend(
            target = target,
            connector_name = self.connector,
            http_connect = self.backend_http_connect,
            allow_patterns = [allow_pattern] if self.backend_http_connect else []
        )
        cert_settings = CertSettings(
            dns_names = [self.domain],
        )
        http_settings = HttpSettings(
            enabled = False,
            oidc_settings = OIDCSettings(
                enabled = False
            ),
            exempted_paths = ExemptedPaths(
                enabled = False,
                patterns = [Pattern(
                    hosts = [Host()]
                )]
            )
        )
        spec = Spec(
            attributes = attributes,
            backend = backend,
            cert_settings = cert_settings,
            http_settings = http_settings
        )
        service = Service(
            kind = "BanyanService",
            apiVersion = "rbac.banyanops.com/v1",
            type = "origin",
            metadata = metadata, 
            spec = spec
        )
        return service


@dataclass
class ServiceInfraSSH(ServiceInfraBase):
    client_ssh_auth: str = field(
        default=str(ServiceClientCertificateType.TRUSTCERT),
        metadata={'help': 'Specifies which certificates - TRUSTCERT | SSHCERT | BOTH - should be used when the user connects to this service; default: TRUSTCERT '}
        )
    client_ssh_host_directive: str = field(
        default="",
        metadata={'help': 'Creates an entry in the SSH config file using the Host keyword. Wildcards are supported such as "192.168.*.?"; default: <service name>'}
        )
    client_banyanproxy_listen_port: int = field(
        default=None,
        metadata={'ignored': True, 'help': 'For SSH, banyanproxy uses stdin instead of a local port'}
        )

    def service_obj(self) -> Service:
        svc = super().service_obj()
        # tags
        svc.metadata.tags.service_app_type = str(ServiceAppType.SSH)
        svc.metadata.tags.ssh_service_type = self.client_ssh_auth
        svc.metadata.tags.ssh_host_directive = self.client_ssh_host_directive
        svc.metadata.tags.write_ssh_config = True
        svc.metadata.tags.allow_user_override = None # must not be set for SSH
        # proxy mode
        svc.metadata.tags.ssh_chain_mode = self.backend_http_connect
        return svc


@dataclass
class ServiceInfraK8S(ServiceInfraBase):
    backend_domain: str = field(
        default='',
        metadata={'ignored': True, 'help': 'For K8S, we use Client Specified connectivity'}
        )
    backend_port: int = field(
        default='',
        metadata={'ignored': True, 'help': 'For K8S, we use Client Specified connectivity'}
        )
    backend_http_connect: bool = field(
        default=True,
        metadata={'ignored': True, 'help': 'For K8S, we use Client Specified connectivity'}
        )
    backend_dns_override_for_domain: str = field(
        default='',
        metadata={'required': True, 'help': 'Override DNS for service domain name with this value'}
        )
    client_kube_cluster_name: str = field(
        default='',
        metadata={'required': True, 'help': 'Creates an entry in the Banyan KUBE config file under this name and populates the associated configuration parameters.'}
        )
    client_kube_ca_key: str = field(
        default='',
        metadata={'required': True, 'help': 'CA Public Key generated during Kube-OIDC-Proxy deployment'}
        )

    def _initialize(self):
        if self.client_kube_cluster_name == "" or self.client_kube_ca_key == "" or self.backend_dns_override_for_domain == "":
            raise Exception("Configuration Error! Need to specify client_kube_cluster_name, client_kube_ca_key, backend_dns_override_for_domain.")
        super()._initialize()

    def service_obj(self) -> Service:
        svc = super().service_obj()
        # tags
        svc.metadata.tags.service_app_type = str(ServiceAppType.K8S)
        svc.metadata.tags.app_listen_port = str(self.client_banyanproxy_listen_port)
        svc.metadata.tags.kube_cluster_name = self.client_kube_cluster_name
        svc.metadata.tags.kube_ca_key = self.client_kube_ca_key
        # proxy mode
        svc.metadata.tags.banyanproxy_mode = str(ServiceClientProxyMode.CHAIN)
        # dns override
        svc.spec.backend.dns_overrides = { self.domain : self.backend_dns_override_for_domain }
        svc.spec.backend.allow_patterns[0].hostnames = [ self.domain ]
        return svc


@dataclass
class ServiceInfraRDP(ServiceInfraBase):
    def service_obj(self) -> Service:
        svc = super().service_obj()
        # tags
        svc.metadata.tags.service_app_type = str(ServiceAppType.RDP)
        svc.metadata.tags.app_listen_port = str(self.client_banyanproxy_listen_port)
        # proxy mode
        svc.metadata.tags.banyanproxy_mode = str(ServiceClientProxyMode.RDPGATEWAY) if self.backend_http_connect else str(ServiceClientProxyMode.TCP)
        return svc


@dataclass
class ServiceInfraDatabase(ServiceInfraBase):
    client_banyanproxy_allowed_domains: list = field(
        default_factory=list,
        metadata={'help': 'Restrict which domains can be proxied through the banyanproxy; only used with Client Specified connectivity'}
        )

    def service_obj(self) -> Service:
        svc = super().service_obj()
        # tags
        svc.metadata.tags.service_app_type = str(ServiceAppType.DATABASE)
        svc.metadata.tags.app_listen_port = str(self.client_banyanproxy_listen_port)
        svc.metadata.tags.include_domains = self.client_banyanproxy_allowed_domains
        # proxy mode
        svc.metadata.tags.banyanproxy_mode = str(ServiceClientProxyMode.CHAIN) if self.backend_http_connect else str(ServiceClientProxyMode.TCP)
        return svc


@dataclass
class ServiceInfraTCP(ServiceInfraBase):
    client_banyanproxy_allowed_domains: list = field(
        default_factory=list,
        metadata={'help': 'Restrict which domains can be proxied through the banyanproxy; only used with Client Specified connectivity'}
        )

    def service_obj(self) -> Service:
        svc = super().service_obj()
        # tags
        svc.metadata.tags.service_app_type = str(ServiceAppType.TCP)
        svc.metadata.tags.app_listen_port = str(self.client_banyanproxy_listen_port)
        svc.metadata.tags.include_domains = self.client_banyanproxy_allowed_domains
        # proxy mode
        svc.metadata.tags.banyanproxy_mode = str(ServiceClientProxyMode.CHAIN) if self.backend_http_connect else str(ServiceClientProxyMode.TCP)
        return svc
