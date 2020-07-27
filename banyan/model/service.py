from dataclasses import field
from typing import List, Dict, Union, Optional, ClassVar, Type
from banyan.model import BanyanApiObject, ObjectCrud
# from banyan.model.custom_types import IPv4Interface
from marshmallow import validate, Schema, pre_load, fields
from marshmallow_dataclass import dataclass
from ipaddress import IPv4Interface


class SerializableIPv4Interface(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        elif isinstance(value, str):
            return IPv4Interface(value)
        else:
            return super()._deserialize(value, attr, data, **kwargs)

    def _serialize(self, value, attr, data, **kwargs):
        if not value:
            return ""
        elif isinstance(value, IPv4Interface):
            return str(value)
        else:
            return super()._serialize(value, attr, data, **kwargs)




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
    port: Optional[int] = field(metadata={"missing": 443})
    user_facing: bool
    template: str
    service_app_type: str
    icon: str = field(default="")
    Schema: ClassVar[Type[Schema]] = Schema

    @pre_load
    def handle_empty_port(self, data, **kwargs):
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
    port: int
    cidr: IPv4Interface = field(metadata={'marshmallow_field': SerializableIPv4Interface()})


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
    service_domain_name: str
    post_auth_redirect_path: str
    api_path: str
    trust_callbacks: Dict[str, str] = field(default_factory=dict)


@dataclass
class HTTPRedirect:
    enabled: bool
    url: str
    status_code: int
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
    enabled: bool
    path: str
    user_agent: str
    https: bool
    method: str = field(metadata={"validate": validate.OneOf(_METHOD_VALUES)})
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
    oidc_settings: Optional[OIDCSettings]  # = field(default_factory=OIDCSettings)
    http_health_check: Optional[HTTPHealthCheck]  # = field(default_factory=HTTPHealthCheck)
    http_redirect: Optional[HTTPRedirect]  # = field(default_factory=HTTPRedirect)
    exempted_paths: Optional[ExemptedPaths]  # = field(default_factory=ExemptedPaths)


@dataclass
class CIDRAddress:
    cidr: IPv4Interface = field(metadata={'marshmallow_field': SerializableIPv4Interface()})
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
    port: Optional[int] = 443
    tls: Optional[bool] = True
    tls_insecure: Optional[bool] = False
    client_certificate: Optional[bool] = False

    @pre_load
    def handle_empty_port(self, data, **kwargs):
        if 'port' in data and data['port'] == '':
            del data['port']
        return data


@dataclass
class Backend:
    target: BackendTarget  # = field(default_factory=BackendTarget)
    dns_overrides: Dict[str, str] = field(default_factory=dict)
    whitelist: List[str] = field(default_factory=list)


@dataclass
class Spec:
    attributes: Attributes  # = field(default_factory=Attributes)
    backend: Backend  # = field(default_factory=Backend)
    cert_settings: CertSettings  # = field(default_factory=CertSettings)
    http_settings: HttpSettings  # = field(default_factory=HttpSettings)
    client_cidrs: List[ClientCIDRs] = field(default_factory=list)


@dataclass
class Service(BanyanApiObject):
    metadata: Metadata
    spec: Spec
    Schema: ClassVar[Type[Schema]] = Schema

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
class ServiceInfo(ObjectCrud):
    service_id: str = field(metadata={"data_key": "ServiceID"})
    service_name: str = field(metadata={"data_key": "ServiceName"})
    cluster_name: str = field(metadata={"data_key": "ClusterName"})
    service_type: str = field(metadata={"data_key": "ServiceType"})
    discovery: str = field(metadata={"data_key": "ServiceDiscovery"})
    version: int = field(metadata={"data_key": "ServiceVersion"})
    description: str = field(metadata={"data_key": "Description"})
    external: str = field(metadata={"data_key": "External"})
    oidc_enabled: bool = field(metadata={"data_key": "OIDCEnabled"})
    oidc_client_spec: str = field(metadata={"data_key": "OIDCClientSpec"})
    service_spec: str = field(metadata={"data_key": "ServiceSpec"})
    user_facing: bool = field(metadata={"data_key": "UserFacing"})
    protocol: str = field(metadata={"data_key": "Protocol"})
    domain: str = field(metadata={"data_key": "Domain"})
    port: int = field(metadata={"data_key": "Port"})
    enabled: bool = field(metadata={"data_key": "Enabled"})
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def service(self) -> Service:
        return Service.Schema().loads(self.service_spec)
        # return Service.from_json_str(self.ServiceSpec)

    @property
    def oidc_client(self) -> OIDCClient:
        return OIDCClient.Schema().loads(self.oidc_client_spec)
        # return OIDCClient.from_json_str(self.OIDCClientSpec)

    @property
    def name(self):
        return self.service_name
