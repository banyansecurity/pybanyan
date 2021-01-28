from dataclasses import field
from datetime import datetime
from typing import List, ClassVar, Type, Optional, Union
from uuid import UUID

from marshmallow import Schema, validate, pre_load, EXCLUDE
from marshmallow.fields import String
from marshmallow_dataclass import dataclass

from banyan.model import Resource, NanoTimestampField, MilliTimestampField, BanyanEnum, TimestampField


@dataclass
class EventUser:
    class Meta:
        unknown = EXCLUDE

    email: str
    groups: List[str] = field(default_factory=list)
    roles: List[str] = field(default_factory=list)

    # noinspection PyUnusedLocal
    @pre_load
    def _remove_nulls(self, data, many, **kwargs):
        if "roles" in data and data["roles"] is None:
            del data["roles"]
        if "groups" in data and data["groups"] is None:
            del data["groups"]
        return data


@dataclass
class EventDevice:
    class Meta:
        unknown = EXCLUDE

    device_id: str = field(metadata={"data_key": "id"})
    friendly_name: str
    mac_address: str
    serial_number: str
    unregistered: bool
    compromised_status: str
    compliance_status: str
    oem_info: str
    model: str
    platform: str
    ownership: str
    architecture: str
    udid: str
    source: str
    last_mdm_data_synced_at: datetime = field(metadata={'marshmallow_field': TimestampField()})
    last_user_agent: Optional[str]


@dataclass
class EventClient:
    class Meta:
        unknown = EXCLUDE

    user_agent: str
    ip_address: str


@dataclass
class EventUserPrincipal:
    class Meta:
        unknown = EXCLUDE

    user: Optional[EventUser]
    device: Optional[EventDevice]
    client: Optional[EventClient]


@dataclass
class EventWorkloadSet:
    class Meta:
        unknown = EXCLUDE

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
    class Meta:
        unknown = EXCLUDE

    host_ips: str
    host_name: str
    cluster_id: str
    port_map: str


@dataclass
class EventWorkloadPrincipal:
    class Meta:
        unknown = EXCLUDE

    workload_set: EventWorkloadSet
    host: EventWorkloadHost


@dataclass
class EventRoleInfo:
    class Meta:
        unknown = EXCLUDE

    role_id: UUID = field(metadata={"data_key": "id"})
    role_name: str = field(metadata={"data_key": "name"})
    version: int
    bound_by: str
    bound_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField()})


@dataclass
class EventPolicyInfo:
    class Meta:
        unknown = EXCLUDE

    policy_id: str = field(metadata={"data_key": "id"})
    policy_name: str = field(metadata={"data_key": "name"})
    version: int
    attached_by: str
    attached_at: datetime = field(metadata={'marshmallow_field': MilliTimestampField()})
    enabled: bool


@dataclass
class EventServiceInfo:
    class Meta:
        unknown = EXCLUDE

    service_id: str = field(metadata={"data_key": "id"})
    service_name: str = field(metadata={"data_key": "name"})
    service_type: str = field(metadata={"data_key": "type"})
    version: int = field(metadata={'marshmallow_field': String()})


@dataclass
class EventAccessLevel:
    class Meta:
        unknown = EXCLUDE

    resource: str


@dataclass
class EventSniData:
    class Meta:
        unknown = EXCLUDE

    name_requested: str
    name_matched: str


@dataclass
class EventRequestData:
    class Meta:
        unknown = EXCLUDE

    protocol: str
    request_type: str = field(metadata={"data_key": "type"})
    query_crud_types: str
    query_resources: str


@dataclass
class EventChannelInfo:
    class Meta:
        unknown = EXCLUDE

    access_level: EventAccessLevel
    sni_data: EventSniData
    request_data: EventRequestData


@dataclass
class EventLinkSource:
    class Meta:
        unknown = EXCLUDE

    container_id: str
    container_name: str
    service_id: str
    service_name: str
    service_version: Optional[int] = field(metadata={"marshmallow_field": String()})
    host_name: str
    ip: str


@dataclass
class EventLinkDestination:
    class Meta:
        unknown = EXCLUDE

    container_id: str
    container_name: str
    service_id: str
    service_name: str
    service_version: Optional[int] = field(metadata={"marshmallow_field": String()})
    host_name: str
    ip: str
    port: Optional[str]


@dataclass
class EventLinkInfo:
    class Meta:
        unknown = EXCLUDE

    source: EventLinkSource
    destination: EventLinkDestination


@dataclass
class EventTrustScore:
    class Meta:
        unknown = EXCLUDE

    trustscore_id: str = field(metadata={"data_key": "id"})
    trustscore_type: str = field(metadata={"data_key": "type"})
    timestamp: datetime = field(metadata={'marshmallow_field': NanoTimestampField()})
    score: int


class EventV2Severity(BanyanEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"


class EventV2Type(BanyanEnum):
    ACCESS = "Access"
    IDENTITY = "Identity"
    REGISTRATION = "Registration"
    TRUST_SCORING = "TrustScoring"


class EventV2Subtype(BanyanEnum):
    DEVICE = "Device"
    USER_PRINCIPAL = "UserPrincipal"
    CONNECTION = "Connection"
    RESOURCE = "Resource"


@dataclass
class EventV2(Resource):
    class Meta:
        unknown = EXCLUDE

    event_id: UUID = field(metadata={"data_key": "id"})
    external_id: Optional[str]
    org_id: UUID
    org_name: str
    event_type: str = field(metadata={"data_key": "type", "validate": validate.OneOf(EventV2Type.choices())})
    sub_type: str = field(metadata={"validate": validate.OneOf(EventV2Subtype.choices())})
    severity: str = field(metadata={"validate": validate.OneOf(EventV2Severity.choices())})
    action: str
    message: str
    result: str
    created_at: datetime = field(metadata={'marshmallow_field': MilliTimestampField()})
    user_principal: EventUserPrincipal
    workload_principal: Optional[EventWorkloadPrincipal]
    role: Optional[List[EventRoleInfo]]
    trustscore: Optional[EventTrustScore]
    service: Optional[EventServiceInfo]
    policy: Optional[EventPolicyInfo]
    channel: Optional[EventChannelInfo]
    link: Optional[EventLinkInfo]
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.id

    @property
    def id(self) -> str:
        return str(self.event_id)


@dataclass
class EventV2TypeCount(Resource):
    class Meta:
        unknown = EXCLUDE

        end_date: datetime = field(metadata={"data_key": "StatsEndTime"})
        delta_time: int = field(metadata={"data_key": "DeltaTime"})
        access_auth: int = field(metadata={"data_key": "NumEventTypeAccessAuth"})
        access_unauth: int = field(metadata={"data_key": "NumEventTypeAccessUnauth"})
        identity_grant: int = field(metadata={"data_key": "NumEventTypeIdentityGrant"})
        identity_deny: int = field(metadata={"data_key": "NumEventTypeIdentityDeny"})
        service: int = field(metadata={"data_key": "NumEventTypeService"})
        link: int = field(metadata={"data_key": "NumEventTypeLink"})
        policy: int = field(metadata={"data_key": "NumEventTypePolicy"})
        role: int = field(metadata={"data_key": "NumEventTypeRole"})


EventOrID = Union[EventV2, str]
