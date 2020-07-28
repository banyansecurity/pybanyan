from dataclasses import field
from datetime import datetime
from typing import List, ClassVar, Type, Optional, Union
from uuid import UUID

from marshmallow import validate, Schema, pre_load
from marshmallow_dataclass import dataclass

from banyan.model import BanyanApiObject, InfoBase, NanoTimestampField


@dataclass
class Tags:
    TEMPLATE_USER = "USER"
    TEMPLATE_WORKLOAD = "WORKLOAD"
    TEMPLATE_CUSTOM = "CUSTOM"
    _TEMPLATE_VALUES = (TEMPLATE_USER, TEMPLATE_WORKLOAD, TEMPLATE_CUSTOM)
    template: str = field(metadata={"validate": validate.OneOf(_TEMPLATE_VALUES)})


@dataclass
class Metadata:
    name: str
    description: str
    tags: Tags = field(default_factory=Tags)


@dataclass
class Options:
    disable_tls_client_authentication: bool
    l7_protocol: str
    mixed_users_and_workloads: Optional[bool]


@dataclass
class PolicyException:
    src_addr: List[str] = field(default_factory=list)
    tls_src_addr: List[str] = field(default_factory=list)  # Deprecated


@dataclass
class L7Access:
    PROTOCOL_HTTP = "http"
    PROTOCOL_KAFKA = "kafka"
    PROTOCOL_MYSQL = "mysql"
    RESOURCE_ALL = "*"
    ACTION_READ = "READ"
    ACTION_WRITE = "WRITE"
    ACTION_CREATE = "CREATE"
    ACTION_UPDATE = "UPDATE"
    ACTION_DELETE = "DELETE"
    ACTION_ALL = "*"
    _ACTION_VALUES = (ACTION_READ, ACTION_WRITE, ACTION_CREATE, ACTION_UPDATE, ACTION_DELETE, ACTION_ALL)
    action: Optional[str] = field(metadata={"validate": validate.OneOf(_ACTION_VALUES + ("",))})
    resources: List[str] = field(default_factory=list)
    actions: List[str] = field(default_factory=list)


@dataclass
class Conditions:
    TRUST_LEVEL_ALWAYS_DENY = "AlwaysDeny"
    TRUST_LEVEL_LOW = "Low"
    TRUST_LEVEL_MEDIUM = "Medium"
    TRUST_LEVEL_HIGH = "High"
    TRUST_LEVEL_ALWAYS_ALLOW = "AlwaysAllow"
    _TRUST_LEVEL_VALUES = (
        TRUST_LEVEL_ALWAYS_DENY, TRUST_LEVEL_LOW, TRUST_LEVEL_MEDIUM, TRUST_LEVEL_HIGH, TRUST_LEVEL_ALWAYS_ALLOW)
    start_time: Optional[datetime]  # should really be a datetime
    end_time: Optional[datetime]  # should really be a datetime
    trust_level: Optional[str] = field(metadata={"missing": TRUST_LEVEL_ALWAYS_ALLOW,
                                                 "validate": validate.OneOf(_TRUST_LEVEL_VALUES + ("",))})

    @pre_load
    def replace_empty_dates(self, data, many, **kwargs):
        if "start_time" in data and data["start_time"] == "":
            del data["start_time"]
        if "end_time" in data and data["end_time"] == "":
            del data["end_time"]
        return data


@dataclass
class Rules:
    comment: Optional[str]
    conditions: Conditions
    l7_access: List[L7Access] = field(default_factory=list)


@dataclass
class Access:
    rules: Rules
    roles: List[str] = field(default_factory=list)


@dataclass
class Spec:
    options: Options
    exception: PolicyException
    access: List[Access] = field(default_factory=list)


@dataclass
class Policy(BanyanApiObject):
    metadata: Metadata
    spec: Spec
    type: str
    KIND = "BanyanPolicy"
    Schema: ClassVar[Type[Schema]] = Schema

    def __post_init__(self):
        self.kind = self.KIND

    @property
    def name(self):
        return self.metadata.name


@dataclass
class PolicyInfo(InfoBase):
    id: UUID = field(metadata={"data_key": "PolicyID"})
    name: str = field(metadata={"data_key": "PolicyName"})
    spec: str = field(metadata={"data_key": "PolicySpec"})
    description: str = field(metadata={"data_key": "Description"})
    version: int = field(metadata={"data_key": "PolicyVersion"})
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def policy(self) -> Policy:
        return Policy.Schema().loads(self.spec)


@dataclass
class PolicyAttachInfo:
    policy_id: UUID = field(metadata={'data_key': 'PolicyID'})
    service_id: str = field(metadata={'data_key': 'ServiceID'})
    attached_by: str = field(metadata={'data_key': 'AttachedBy'})
    attached_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='AttachedAt')})
    enabled: bool = field(metadata={'data_key': 'Enabled'})
    detached_by: str = field(metadata={'data_key': 'DetachedBy'})
    detached_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='DetachedAt')})
    Schema: ClassVar[Type[Schema]] = Schema


PolicyInfoOrName = Union[PolicyInfo, str]
