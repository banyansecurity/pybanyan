from dataclasses import field
from datetime import datetime
from ipaddress import IPv4Address
from typing import List, Dict, ClassVar, Type, Optional
from uuid import UUID

import OpenSSL.crypto
from marshmallow import fields, Schema, validate, pre_load
from marshmallow_dataclass import dataclass
from marshmallow.fields import Integer, String
from semver import VersionInfo

from banyan.model import Resource, NanoTimestampField, MilliTimestampField
from banyan.model.netagent import Netagent


@dataclass
class EventUser:
    email: str
    groups: List[str]
    roles: List[str]


@dataclass
class EventDevice:
    device_id: UUID = field(metadata={"data_key": "id"})
    friendly_name: str
    mac_address: str
    serial_number: str
    registration_status: bool = field(metadata={'marshmallow_field': fields.String()})
    compromised_status: str
    compliance_status: str
    oem_info: str
    model: str
    platform: str
    ownership: str
    architecture: str
    udid: str
    source: str
    last_mdm_data_synced_at: datetime = field(metadata={'marshmallow_field': MilliTimestampField()})


@dataclass
class EventClient:
    user_agent: str
    ip_address: str


@dataclass
class EventUserPrincipal:
    user: EventUser
    device: EventDevice
    client: EventClient


@dataclass
class EventWorkloadSet:
    container_name: str
    container_id: str
    image: str
    repo: str
    tag: str
    labels: str
    container_ips: str
    app_name: str


@dataclass
class EventWorkloadHost:
    host_ips: str
    host_name: str
    cluster_id: str
    port_map: str


@dataclass
class EventWorkloadPrincipal:
    workload_set: EventWorkloadSet
    host: EventWorkloadHost


@dataclass
class EventRoleInfo:
    role_id: UUID = field(metadata={"data_key": "id"})
    role_name: str = field(metadata={"data_key": "name"})
    version: int
    bound_by: str
    bound_at: datetime = field(metadata={'marshmallow_field': MilliTimestampField()})


@dataclass
class EventPolicyInfo:
    policy_id: str = field(metadata={"data_key": "id"})
    policy_name: str = field(metadata={"data_key": "name"})
    version: int
    attached_by: str
    attached_at: datetime = field(metadata={'marshmallow_field': MilliTimestampField()})
    enabled: bool


@dataclass
class EventServiceInfo:
    service_id: str = field(metadata={"data_key": "id"})
    service_name: str = field(metadata={"data_key": "name"})
    service_type: str = field(metadata={"data_key": "type"})
    version: int = field(metadata={'marshmallow_field': String()})


@dataclass
class EventAccessLevel:
    resource: str


@dataclass
class EventSniData:
    name_requested: str
    name_matched: str


@dataclass
class EventRequestData:
    protocol: str
    request_type: str = field(metadata={"data_key": "type"})
    query_crud_types: str
    query_resources: str


@dataclass
class EventChannelInfo:
    access_level: EventAccessLevel
    sni_data: EventSniData
    request_data: EventRequestData


@dataclass
class EventLinkSource:
    container_id: str
    container_name: str
    service_id: str
    service_name: str
    service_version: Optional[int] = field(metadata={"marshmallow_field": String()})
    host_name: str
    ip: str


@dataclass
class EventLinkDestination:
    container_id: str
    container_name: str
    service_id: str
    service_name: str
    service_version: Optional[int] = field(metadata={"marshmallow_field": String(data_key="serivce_version")})
    host_name: str
    ip: str
    port: Optional[str]


@dataclass
class EventLinkInfo:
    source: EventLinkSource
    destination: EventLinkDestination


@dataclass
class EventTrustScore:
    trustscore_id: str = field(metadata={"data_key": "id"})
    trustscore_type: str = field(metadata={"data_key": "type"})
    timestamp: datetime = field(metadata={'marshmallow_field': NanoTimestampField()})
    score: int


@dataclass
class EventV2(Resource):
    SEVERITY_DEBUG = "DEBUG"
    SEVERITY_INFO = "INFO"
    SEVERITY_WARN = "WARN"
    SEVERITY_ERROR = "ERROR"
    _SEVERITIES = (SEVERITY_DEBUG, SEVERITY_INFO, SEVERITY_WARN, SEVERITY_ERROR)

    TYPE_ACCESS = "Access"
    TYPE_IDENTITY = "Identity"
    TYPE_REGISTRATION = "Registration"
    TYPE_TRUSTSCORING = "Trustscoring"
    _TYPES = (TYPE_ACCESS, TYPE_IDENTITY, TYPE_REGISTRATION, TYPE_TRUSTSCORING)

    SUBTYPE_DEVICE = "Device"
    SUBTYPE_USERPRINCIPAL = "UserPrincipal"
    SUBTYPE_CONNECTION = "Connection"
    SUBTYPE_RESOURCE = "Resource"
    _SUBTYPES = (SUBTYPE_DEVICE, SUBTYPE_USERPRINCIPAL, SUBTYPE_CONNECTION, SUBTYPE_RESOURCE)

    event_id: UUID = field(metadata={"data_key": "id"})
    external_id: Optional[str]
    org_id: UUID
    org_name: str
    severity: str = field(metadata={"validate": validate.OneOf(_SEVERITIES)})
    action: str
    event_type: str = field(metadata={"data_key": "type", "validate": validate.OneOf(_TYPES)})
    sub_type: str = field(metadata={"validate": validate.OneOf(_SUBTYPES)})
    message: str
    message: str
    result: str
    created_at: datetime = field(metadata={'marshmallow_field': MilliTimestampField()})
    user_principal: EventUserPrincipal
    workload_principal: EventWorkloadPrincipal
    role: List[EventRoleInfo]
    trustscore: EventTrustScore
    service: EventServiceInfo
    policy: EventPolicyInfo
    channel: EventChannelInfo
    link: EventLinkInfo
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.id

    @property
    def id(self) -> str:
        return str(self.event_id)

    @pre_load
    def _remove_empty_dates(self, data, many, **kwargs):
        if "LastActivityAt" in data and data["LastActivityAt"] == "":
            del data["LastActivityAt"]
        return data
