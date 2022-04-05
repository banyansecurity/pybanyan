import dataclasses
from marshmallow_dataclass import dataclass
from banyan.model.service import *

@dataclass
class ServiceWebStandard:
    name: str = field(
        default=None,
        metadata={'required': True, 'help': 'Name of the service; use lowercase alphanumeric characters or "-"'}
        )
    description: str = field(
        default='ServiceWebStandard',
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
        default=443,
        metadata={'ignored': True, 'help': 'The external-facing port for this service; set to 443 for hosted websites'}
        )
    letsencrypt: bool = field(
        default=False,
        metadata={'help': 'Use a Public CA-issued server certificate instead of a Private CA-issued one'}
        )
    # backend
    backend_domain: str = field(
        default=None,
        metadata={'required': True, 'help': 'The internal network address where this service is hosted; ex. 192.168.1.2'}
        )
    backend_port: int = field(
        default=None,
        metadata={'required': True, 'help': 'The internal port where this service is hosted'}
        )
    backend_tls: bool = field(
        default=False,
        metadata={'help': 'Indicates the backend server uses TLS'}
        )
    backend_tls_insecure: bool = field(
        default=False,
        metadata={'help': 'Indicates the backend server does not validate the TLS certficate'}
        )
    # TODO: cors, exemptions, custom_headers, service_accounts
    # in ui but ignore here - description_link, icon, show_in_catalog, backend_tls_client_cert

    # sanity check params and update dependencies
    def _initialize(self):
        # basics
        if not self.name or not self.domain or not self.backend_domain or not self.backend_port:
            raise Exception("Configuration Error! Need to specify name, domain, backend_domain, backend_port.")
        # deployment model
        if not self.cluster:
            raise Exception("Configuration Error! Need to specify cluster.")
        if (not self.connector and not self.access_tier) or (self.connector and self.access_tier):
            raise Exception("Configuration Error! Need to specify either access_tier or connector.")
        # deployment model = self-hosted access-tier
        if self.access_tier:
            self.connector = ""
        # deployment model = global-edge
        if self.connector:
            self.access_tier = "*"

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

    # create a Service object
    def service_obj(self) -> Service:
        self._initialize()
        tags = Tags(
            template = str(ServiceTemplate.WEB),
            user_facing = "true",
            protocol = "https",
            domain = self.domain,
            port = str(self.port),
            icon = "",
            service_app_type = str(ServiceAppType.WEB),
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
            tls = self.backend_tls,
            tls_insecure = self.backend_tls_insecure
        )
        backend = Backend(
            target = target,
            connector_name = self.connector
        )
        cert_settings = CertSettings(
            dns_names = [self.domain],
            letsencrypt = self.letsencrypt
        )
        oidc_settings = OIDCSettings(
            enabled = True,
            service_domain_name = "https://" + self.domain
        )
        exempted_paths = ExemptedPaths(
            enabled = False
        )
        http_settings = HttpSettings(
            enabled = True,
            oidc_settings = oidc_settings,
            exempted_paths = exempted_paths
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
