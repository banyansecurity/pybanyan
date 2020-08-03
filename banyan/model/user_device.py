from dataclasses import field
from datetime import datetime
from typing import List, ClassVar, Type, Optional
# from banyan.model.custom_types import NanoTimestamp, BoolString
# from dataclasses_serialization.json import JSONStrSerializerMixin, JSONSerializerMixin
from uuid import UUID

from marshmallow import Schema, validate, fields
from marshmallow_dataclass import dataclass
from semver import VersionInfo

from banyan.model import NanoTimestampField, Resource


@dataclass
class TrustFactor:
    name: str = field(metadata={'data_key': 'Name'})
    value: bool = field(metadata={'data_key': 'Value'})
    type: str = field(metadata={'data_key': 'Type'})
    source: str = field(metadata={'data_key': 'Source'})
    description: str = field(metadata={'data_key': 'Description'})


@dataclass
class TrustData:
    ALWAYS_ALLOW = "AlwaysAllow"
    ALWAYS_DENY = "AlwaysDeny"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    _TRUST_VALUES = (ALWAYS_DENY, LOW, MEDIUM, HIGH, ALWAYS_ALLOW)
    entity_trustscore: int = field(metadata={'data_key': 'EntityTrustscore'})
    override_trustscore: int = field(metadata={'data_key': 'OverrideTrustscore'})
    access_trustscore: int = field(metadata={'data_key': 'AccessTrustscore'})
    override_active: bool = field(metadata={'data_key': 'OverrideActive'})
    level: str = field(metadata={'data_key': 'Level', 'validate': validate.OneOf(_TRUST_VALUES)})
    updated_at: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='UpdatedAt')})
    factors: List[TrustFactor] = field(default_factory=list, metadata={'data_key': 'Factors'})


@dataclass
class MdmData:
    timestamp: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='Timestamp')})
    source: str = field(metadata={'data_key': 'Source'})
    compromised_status: bool = field(metadata={'data_key': 'CompromisedStatus'})
    compliant_status: str = field(metadata={'data_key': 'CompliantStatus'})


@dataclass
class User(Resource):
    username: str = field(metadata={'data_key': 'Name'})
    email: str = field(metadata={'data_key': 'Email'})
    groups: str = field(metadata={'data_key': 'Groups'})
    last_login: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='LastLogin')})
    login_count: int = field(metadata={'data_key': 'LoginCount'})
    trust_data: TrustData = field(metadata={'data_key': 'TrustData'})
    serial_numbers: List[str] = field(default_factory=list, metadata={'data_key': 'SerialNumbers'})
    roles: List[str] = field(default_factory=list, metadata={'data_key': 'Roles'})
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.username

    @property
    def id(self) -> str:
        return self.email


@dataclass
class Device(Resource):
    device_id: UUID = field(metadata={'data_key': 'DeviceID'})
    serial_number: str = field(metadata={'data_key': 'SerialNumber'})
    device_friendly_name: str = field(metadata={'data_key': 'DeviceFriendlyName'})
    last_login: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='LastLogin')})
    login_count: int = field(metadata={'data_key': 'LoginCount'})
    ownership: str = field(metadata={'data_key': 'Ownership'})
    platform: str = field(metadata={'data_key': 'Platform'})
    model: str = field(metadata={'data_key': 'Model'})
    architecture: str = field(metadata={'data_key': 'Architecture'})
    registered_status: bool = field(metadata={'data_key': 'RegisteredStatus'})
    is_banned: bool = field(metadata={'data_key': 'Banned'})
    os_level: str = field(metadata={'data_key': 'OS'})
    app_version: Optional[VersionInfo] = field(metadata={'marshmallow_field': fields.String(data_key='AppVersion'),
                                                         "missing": None})
    mdm_data: MdmData = field(metadata={'data_key': 'MdmData'})
    trust_data: TrustData = field(metadata={'data_key': 'TrustData'})
    emails: List[str] = field(default_factory=list, metadata={'data_key': 'Emails'})
    roles: List[str] = field(default_factory=list, metadata={'data_key': 'Roles'})
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.device_friendly_name

    @property
    def id(self) -> str:
        return str(self.device_id)

