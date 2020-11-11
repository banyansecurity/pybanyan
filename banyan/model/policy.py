from dataclasses import field
from datetime import datetime
from typing import List, ClassVar, Optional, Union
from uuid import UUID

from marshmallow import validate, Schema, pre_load, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import BanyanApiObject, InfoBase, NanoTimestampField, BanyanEnum
from banyan.model.trustscore import TrustLevel


class Template(BanyanEnum):
    USER = "USER"
    WORKLOAD = "WORKLOAD"
    CUSTOM = "CUSTOM"


@dataclass
class Tags:
    class Meta:
        unknown = EXCLUDE

    template: str = field(metadata={"validate": validate.OneOf(Template.choices())})


@dataclass
class Metadata:
    class Meta:
        unknown = EXCLUDE

    name: str
    description: str
    tags: Tags = field(default_factory=Tags)


@dataclass
class Options:
    class Meta:
        unknown = EXCLUDE

    disable_tls_client_authentication: bool
    l7_protocol: Optional[str]
    mixed_users_and_workloads: Optional[bool]


@dataclass
class PolicyException:
    class Meta:
        unknown = EXCLUDE

    src_addr: List[str] = field(default_factory=list)
    tls_src_addr: List[str] = field(default_factory=list)  # Deprecated


class L7Protocol(BanyanEnum):
    HTTP = "http"
    KAFKA = "kafka"
    MYSQL = "mysql"


class L7Action(BanyanEnum):
    READ = "READ"
    WRITE = "WRITE"
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    ALL = "*"


@dataclass
class L7Access:
    class Meta:
        unknown = EXCLUDE

    RESOURCE_ALL = "*"
    action: Optional[str] = field(metadata={"validate": validate.OneOf(L7Action.choices() + [""])})
    resources: List[str] = field(default_factory=list)
    actions: List[str] = field(default_factory=list)


@dataclass
class Conditions:
    class Meta:
        unknown = EXCLUDE

    start_time: Optional[datetime]
    end_time: Optional[datetime]
    trust_level: Optional[str] = field(metadata={"missing": TrustLevel.ALWAYS_ALLOW,
                                                 "validate": validate.OneOf(TrustLevel.choices() + [""])})

    # noinspection PyUnusedLocal
    @pre_load
    def _replace_empty_dates(self, data, many, **kwargs):
        if "start_time" in data and data["start_time"] == "":
            del data["start_time"]
        if "end_time" in data and data["end_time"] == "":
            del data["end_time"]
        return data


@dataclass
class Rules:
    class Meta:
        unknown = EXCLUDE

    conditions: Conditions
    l7_access: Optional[List[L7Access]] = field(default_factory=list)


@dataclass
class Access:
    class Meta:
        unknown = EXCLUDE

    rules: Rules
    roles: List[str] = field(default_factory=list)


@dataclass
class Spec:
    class Meta:
        unknown = EXCLUDE

    options: Options
    exception: PolicyException
    access: List[Access] = field(default_factory=list)


@dataclass
class Policy(BanyanApiObject):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    metadata: Metadata
    spec: Spec
    type: str
    KIND = "BanyanPolicy"

    def __post_init__(self):
        self.kind = self.KIND

    @property
    def name(self):
        return self.metadata.name


@dataclass
class PolicyInfo(InfoBase):
    class Meta:
        unknown = EXCLUDE

    policy_id: UUID = field(metadata={'data_key': 'PolicyID'})
    policy_name: str = field(metadata={'data_key': 'PolicyName'})
    spec: str = field(metadata={'data_key': 'PolicySpec'})
    description: str = field(metadata={'data_key': 'Description'})
    version: int = field(metadata={'data_key': 'PolicyVersion'})
    Schema: ClassVar[Schema] = Schema

    @property
    def policy(self) -> Policy:
        return Policy.Schema().loads(self.spec)

    @property
    def name(self) -> str:
        return self.policy_name

    @property
    def id(self) -> str:
        return str(self.policy_id)


@dataclass
class PolicyAttachInfo:
    class Meta:
        unknown = EXCLUDE

    enabled: bool = field(metadata={'data_key': 'Enabled'})
    policy_id: UUID = field(metadata={'data_key': 'PolicyID'})
    service_id: str = field(metadata={'data_key': 'ServiceID'})
    attached_by: str = field(metadata={'data_key': 'AttachedBy'})
    detached_by: str = field(metadata={'data_key': 'DetachedBy'})
    attached_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='AttachedAt')})
    detached_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='DetachedAt')})
    Schema: ClassVar[Schema] = Schema


PolicyInfoOrName = Union[PolicyInfo, str]
