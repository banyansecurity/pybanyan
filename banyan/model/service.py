from dataclasses import field
from ipaddress import IPv4Interface
from typing import List, Dict, Union, Optional, ClassVar

from marshmallow import validate, fields, Schema, EXCLUDE, pre_load
from marshmallow_dataclass import dataclass

from banyan.model import BanyanApiObject, InfoBase, IPv4InterfaceField, BanyanEnum


class ServiceTemplate(BanyanEnum):
    WEB = "WEB_USER"
    TCP = "TCP_USER"
    WORKLOAD = "TCP_WORKLOAD"
    CUSTOM = "CUSTOM"


class ServiceAppType(BanyanEnum):
    WEB = "WEB"
    SSH = "SSH"
    TCP = "TCP"
    RDP = "RDP"
    K8S = "K8S"
    GENERIC = "GENERIC"
    CUSTOM = "CUSTOM"


@dataclass
class Tags:
    class Meta:
        unknown = EXCLUDE

    protocol: str
    domain: str
    user_facing: bool = field(metadata={'marshmallow_field': fields.String()})
    template: str = field(metadata={'validate': validate.OneOf(ServiceTemplate.choices() + ["USER_WEB", "USER_TCP"])})
    service_app_type: str = field(metadata={'validate': validate.OneOf(ServiceAppType.choices())})
    icon: str = field(default="")
    port: int = field(default=443, metadata={'marshmallow_field': fields.String(), 'allow_none': True})
    Schema: ClassVar[Schema] = Schema


@dataclass
class Metadata:
    class Meta:
        unknown = EXCLUDE

    tags: Tags
    name: str
    description: str
    cluster: str


@dataclass
class FrontendAddress:
    class Meta:
        unknown = EXCLUDE

    port: int = field(metadata={'marshmallow_field': fields.String()})
    cidr: IPv4Interface = field(metadata={'marshmallow_field': IPv4InterfaceField()})


@dataclass
class Attributes:
    class Meta:
        unknown = EXCLUDE

    tls_sni: List[str] = field(default_factory=list)
    frontend_addresses: List[FrontendAddress] = field(default_factory=list)
    host_tag_selector: List[Dict[str, str]] = field(default_factory=list)
    addresses: List[str] = field(default_factory=list)  # Deprecated


@dataclass
class CustomTLSCert:
    class Meta:
        unknown = EXCLUDE

    enabled: bool
    cert_file: str = ""
    key_file: str = ""


@dataclass
class CertSettings:
    class Meta:
        unknown = EXCLUDE

    custom_tls_cert: CustomTLSCert = field(default_factory=CustomTLSCert)
    dns_names: List[str] = field(default_factory=list)


@dataclass
class OIDCSettings:
    class Meta:
        unknown = EXCLUDE

    enabled: bool
    service_domain_name: str = field(default='')
    post_auth_redirect_path: str = field(default='')
    api_path: str = field(default='')
    trust_callbacks: Dict[str, str] = field(default_factory=dict)

    # noinspection PyUnusedLocal
    @pre_load
    def _remove_nulls(self, data, many, **kwargs):
        if 'trust_callbacks' in data and data['trust_callbacks'] is None:
            del data['trust_callbacks']
        return data


@dataclass
class HTTPRedirect:
    class Meta:
        unknown = EXCLUDE

    enabled: bool
    url: str = field(default='')
    status_code: int = field(default=302)
    addresses: List[str] = field(default_factory=list)
    from_address: List[str] = field(default_factory=list)


class HttpMethod(BanyanEnum):
    GET = "GET"
    HEAD = "HEAD"
    DELETE = "DELETE"
    PUT = "PUT"
    POST = "POST"
    OPTIONS = "OPTIONS"
    ALL = "*"


@dataclass
class HTTPHealthCheck:
    class Meta:
        unknown = EXCLUDE

    enabled: bool = field(default=False)
    path: str = field(default='/')
    user_agent: str = field(default='')
    https: bool = field(default=True)
    method: str = field(default='GET', metadata={'validate': validate.OneOf(HttpMethod.choices() + [""])})
    addresses: List[str] = field(default_factory=list)
    from_address: List[str] = field(default_factory=list)


@dataclass
class Host:
    class Meta:
        unknown = EXCLUDE

    origin_header: List[str] = field(default_factory=list)
    target: List[str] = field(default_factory=list)


@dataclass
class Pattern:
    class Meta:
        unknown = EXCLUDE

    hosts: List[Host] = field(default_factory=list)
    methods: List[str] = field(default_factory=list)
    mandatory_headers: List[str] = field(default_factory=list)
    paths: List[str] = field(default_factory=list)


@dataclass
class ExemptedPaths:
    class Meta:
        unknown = EXCLUDE

    enabled: bool
    paths: Optional[List[str]]
    patterns: List[Pattern] = field(default_factory=list)


@dataclass
class HttpSettings:
    class Meta:
        unknown = EXCLUDE

    enabled: bool
    oidc_settings: Optional[OIDCSettings]
    http_health_check: Optional[HTTPHealthCheck]
    http_redirect: Optional[HTTPRedirect]
    exempted_paths: Optional[ExemptedPaths]


@dataclass
class CIDRAddress:
    class Meta:
        unknown = EXCLUDE

    cidr: IPv4Interface = field(metadata={'marshmallow_field': IPv4InterfaceField()})
    ports: int


@dataclass
class ClientCIDRs:
    class Meta:
        unknown = EXCLUDE

    addresses: List[CIDRAddress] = field(default_factory=list)
    host_tag_selector: List[Dict[str, str]] = field(default_factory=list)
    clusters: List[str] = field(default_factory=list)


@dataclass
class BackendTarget:
    class Meta:
        unknown = EXCLUDE

    name: str
    name_delimiter: Optional[str]
    port: int = field(default=443, metadata={'marshmallow_field': fields.String(), 'allow_none': True})
    tls: Optional[bool] = False
    tls_insecure: Optional[bool] = False
    client_certificate: Optional[bool] = False


@dataclass
class Backend:
    class Meta:
        unknown = EXCLUDE

    target: BackendTarget
    dns_overrides: Dict[str, str] = field(default_factory=dict)
    whitelist: List[str] = field(default_factory=list)


@dataclass
class Spec:
    class Meta:
        unknown = EXCLUDE

    attributes: Attributes
    backend: Backend
    cert_settings: CertSettings
    http_settings: HttpSettings
    client_cidrs: List[ClientCIDRs] = field(default_factory=list)


@dataclass
class Service(BanyanApiObject):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    metadata: Metadata
    spec: Spec

    @property
    def name(self):
        return self.metadata.name


@dataclass
class OIDCClient:
    class Meta:
        unknown = EXCLUDE

    trust_auth: str
    trust_cb: str
    client_id: str
    client_secret: str
    trust_callbacks: Dict[str, str] = field(default_factory=dict)
    Schema: ClassVar[Schema] = Schema


@dataclass
class ServiceInfo(InfoBase):
    class Meta:
        unknown = EXCLUDE

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
