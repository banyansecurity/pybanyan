from dataclasses import field
from ipaddress import IPv4Interface
from typing import List, Dict, Union, Optional, ClassVar

from marshmallow import validate, pre_load, fields, Schema
from marshmallow_dataclass import dataclass

from banyan.model import BanyanApiObject, InfoBase, IPv4InterfaceField


@dataclass
class Tags:
    TEMPLATE_WEB = "USER_WEB"
    TEMPLATE_TCP = "USER_TCP"
    TEMPLATE_CUSTOM = "CUSTOM"
    APP_TYPE_WEB = "WEB"
    APP_TYPE_SSH = "SSH"
    APP_TYPE_TCP = "TCP"
    APP_TYPE_RDP = "RDP"
    APP_TYPE_GENERIC = "GENERIC"
    protocol: str
    domain: str
    user_facing: bool = field(metadata={'marshmallow_field': fields.String()})
    template: str
    service_app_type: str
    icon: str = field(default="")
    port: int = field(default=443, metadata={'marshmallow_field': fields.String()})
    Schema: ClassVar[Schema] = Schema

    # noinspection PyUnusedLocal
    @pre_load
    def _handle_empty_port(self, data, **kwargs):
        if 'port' in data and data['port'] == '':
            del data['port']
        return data


@dataclass
class Metadata:
    tags: Tags
    name: str
    description: str
    cluster: str


@dataclass
class FrontendAddress:
    port: int = field(metadata={'marshmallow_field': fields.String()})
    cidr: IPv4Interface = field(metadata={'marshmallow_field': IPv4InterfaceField()})


@dataclass
class Attributes:
    tls_sni: List[str] = field(default_factory=list)
    frontend_addresses: List[FrontendAddress] = field(default_factory=list)
    host_tag_selector: List[Dict[str, str]] = field(default_factory=list)
    addresses: List[str] = field(default_factory=list)  # Deprecated


@dataclass
class CustomTLSCert:
    enabled: bool
    cert_file: str = ""
    key_file: str = ""


@dataclass
class CertSettings:
    custom_tls_cert: CustomTLSCert = field(default_factory=CustomTLSCert)
    dns_names: List[str] = field(default_factory=list)


@dataclass
class OIDCSettings:
    enabled: bool
    service_domain_name: str = field(default='')
    post_auth_redirect_path: str = field(default='')
    api_path: str = field(default='')
    trust_callbacks: Dict[str, str] = field(default_factory=dict)


@dataclass
class HTTPRedirect:
    enabled: bool
    url: str = field(default='')
    status_code: int = field(default=302)
    addresses: List[str] = field(default_factory=list)
    from_address: List[str] = field(default_factory=list)


@dataclass
class HTTPHealthCheck:
    METHOD_GET = "GET"
    METHOD_HEAD = "HEAD"
    METHOD_DELETE = "DELETE"
    METHOD_PUT = "PUT"
    METHOD_POST = "POST"
    METHOD_OPTIONS = "OPTIONS"
    METHOD_ALL = "*"
    _METHOD_VALUES = (METHOD_GET, METHOD_POST, METHOD_HEAD, METHOD_PUT, METHOD_DELETE, METHOD_OPTIONS, METHOD_ALL, "")
    enabled: bool = field(default=False)
    path: str = field(default='/')
    user_agent: str = field(default='')
    https: bool = field(default=True)
    method: str = field(default='GET', metadata={'validate': validate.OneOf(_METHOD_VALUES)})
    addresses: List[str] = field(default_factory=list)
    from_address: List[str] = field(default_factory=list)


@dataclass
class Host:
    origin_header: List[str] = field(default_factory=list)
    target: List[str] = field(default_factory=list)


@dataclass
class Pattern:
    hosts: List[Host] = field(default_factory=list)
    methods: List[str] = field(default_factory=list)
    mandatory_headers: List[str] = field(default_factory=list)
    paths: List[str] = field(default_factory=list)


@dataclass
class ExemptedPaths:
    enabled: bool
    paths: Optional[List[str]]
    patterns: List[Pattern] = field(default_factory=list)


@dataclass
class HttpSettings:
    enabled: bool
    oidc_settings: Optional[OIDCSettings]
    http_health_check: Optional[HTTPHealthCheck]
    http_redirect: Optional[HTTPRedirect]
    exempted_paths: Optional[ExemptedPaths]


@dataclass
class CIDRAddress:
    cidr: IPv4Interface = field(metadata={'marshmallow_field': IPv4InterfaceField()})
    ports: int


@dataclass
class ClientCIDRs:
    addresses: List[CIDRAddress] = field(default_factory=list)
    host_tag_selector: List[Dict[str, str]] = field(default_factory=list)
    clusters: List[str] = field(default_factory=list)


@dataclass
class BackendTarget:
    name: str
    name_delimiter: Optional[str]
    port: int = field(default=443, metadata={'marshmallow_field': fields.String()})
    tls: Optional[bool] = True
    tls_insecure: Optional[bool] = False
    client_certificate: Optional[bool] = False

    # noinspection PyUnusedLocal
    @pre_load
    def _handle_empty_port(self, data, **kwargs):
        if 'port' in data and data['port'] == '':
            del data['port']
        return data


@dataclass
class Backend:
    target: BackendTarget
    dns_overrides: Dict[str, str] = field(default_factory=dict)
    whitelist: List[str] = field(default_factory=list)


@dataclass
class Spec:
    attributes: Attributes
    backend: Backend
    cert_settings: CertSettings
    http_settings: HttpSettings
    client_cidrs: List[ClientCIDRs] = field(default_factory=list)


@dataclass
class Service(BanyanApiObject):
    metadata: Metadata
    spec: Spec

    @property
    def name(self):
        return self.metadata.name


@dataclass
class OIDCClient:
    trust_auth: str
    trust_cb: str
    client_id: str
    client_secret: str
    trust_callbacks: Dict[str, str] = field(default_factory=dict)


@dataclass
class ServiceInfo(InfoBase):
    service_id: str = field(metadata={'data_key': 'ServiceID'})
    service_name: str = field(metadata={"data_key": 'ServiceName'})
    description: str = field(metadata={"data_key": 'Description'})
    spec: str = field(metadata={"data_key": 'ServiceSpec'})

    discovery: str = field(metadata={'data_key': 'ServiceDiscovery'})
    cluster_name: str = field(metadata={'data_key': 'ClusterName'})
    type: str = field(metadata={'data_key': 'ServiceType'})
    version: int = field(metadata={'data_key': 'ServiceVersion'})
    external: str = field(metadata={'data_key': 'External'})
    oidc_enabled: bool = field(metadata={'data_key': 'OIDCEnabled'})
    oidc_client_spec: str = field(metadata={'data_key': 'OIDCClientSpec'})
    user_facing: bool = field(metadata={'data_key': 'UserFacing'})
    protocol: str = field(metadata={'data_key': 'Protocol'})
    domain: str = field(metadata={'data_key': 'Domain'})
    port: int = field(metadata={'data_key': 'Port'})
    enabled: bool = field(metadata={'data_key': 'Enabled'})
    Schema: ClassVar[Schema] = Schema

    @property
    def service(self) -> Service:
        return Service.Schema().loads(self.spec)

    @property
    def oidc_client(self) -> OIDCClient:
        return OIDCClient.Schema().loads(self.oidc_client_spec)

    @property
    def name(self) -> str:
        return self.service_name

    @property
    def id(self) -> str:
        return self.service_id


ServiceInfoOrName = Union[ServiceInfo, str]
