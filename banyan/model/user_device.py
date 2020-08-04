from dataclasses import field
from datetime import datetime
from typing import List, ClassVar, Type, Optional
from uuid import UUID

from marshmallow import Schema, validate, fields, pre_load
from marshmallow_dataclass import dataclass
from semver import VersionInfo

from banyan.model import NanoTimestampField, Resource
from banyan.model.trustscore import TrustFactorsV2


@dataclass
class TrustFactorV1:
    name: str = field(metadata={'data_key': 'Name'})
    value: bool = field(metadata={'data_key': 'Value'})
    type: str = field(metadata={'data_key': 'Type'})
    source: str = field(metadata={'data_key': 'Source'})
    description: str = field(metadata={'data_key': 'Description'})


@dataclass
class TrustDataV1:
    ALWAYS_ALLOW = "AlwaysAllow"
    ALWAYS_DENY = "AlwaysDeny"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    TRUST_VALUES = (ALWAYS_DENY, LOW, MEDIUM, HIGH, ALWAYS_ALLOW)
    entity_trustscore: int = field(metadata={'data_key': 'EntityTrustscore'})
    override_trustscore: int = field(metadata={'data_key': 'OverrideTrustscore'})
    access_trustscore: int = field(metadata={'data_key': 'AccessTrustscore'})
    override_active: bool = field(metadata={'data_key': 'OverrideActive'})
    level: str = field(metadata={'data_key': 'Level', 'validate': validate.OneOf(TRUST_VALUES)})
    updated_at: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='UpdatedAt')})
    factors: List[TrustFactorV1] = field(default_factory=list, metadata={'data_key': 'Factors'})


@dataclass
class MdmData:
    timestamp: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='Timestamp')})
    source: str = field(metadata={'data_key': 'Source'})
    compromised_status: str = field(metadata={'data_key': 'CompromisedStatus'})
    compliant_status: str = field(metadata={'data_key': 'CompliantStatus'})


@dataclass
class User(Resource):
    username: str = field(metadata={'data_key': 'Name'})
    email: str = field(metadata={'data_key': 'Email'})
    groups: str = field(metadata={'data_key': 'Groups'})
    last_login: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='LastLogin')})
    login_count: int = field(metadata={'data_key': 'LoginCount'})
    trust_data: TrustDataV1 = field(metadata={'data_key': 'TrustData'})
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
    CORPORATE_DEDICATED = 'Corporate Dedicated'
    CORPORATE_SHARED = 'Corporate Shared'
    EMPLOYEE_OWNED = 'Employee Owned'
    OTHER = 'Other'
    _OWNERSHIP_VALUES = (CORPORATE_DEDICATED, CORPORATE_SHARED, EMPLOYEE_OWNED, OTHER)

    serial_number: str = field(metadata={'data_key': 'SerialNumber'})
    device_friendly_name: str = field(metadata={'data_key': 'DeviceFriendlyName'})
    last_login: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='LastLogin')})
    login_count: int = field(metadata={'data_key': 'LoginCount'})
    ownership: str = field(metadata={'data_key': 'Ownership', 'validate': validate.OneOf(_OWNERSHIP_VALUES)})
    platform: str = field(metadata={'data_key': 'Platform'})
    model: str = field(metadata={'data_key': 'Model'})
    architecture: str = field(metadata={'data_key': 'Architecture'})
    registered_status: bool = field(metadata={'data_key': 'RegisteredStatus'})
    is_banned: bool = field(metadata={'data_key': 'Banned'})
    os_level: str = field(metadata={'data_key': 'OS'})
    app_version: Optional[VersionInfo] = field(metadata={'marshmallow_field': fields.String(data_key='AppVersion'),
                                                         "missing": None})
    mdm_data: MdmData = field(metadata={'data_key': 'MdmData'})
    trust_data: TrustDataV1 = field(metadata={'data_key': 'TrustData'})
    emails: List[str] = field(default_factory=list, metadata={'data_key': 'Emails'})
    roles: List[str] = field(default_factory=list, metadata={'data_key': 'Roles'})
    device_id: UUID = field(default=None, metadata={'data_key': 'DeviceID', 'missing': ''})
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.device_friendly_name

    @property
    def id(self) -> str:
        return self.serial_number

    # noinspection PyUnusedLocal
    @pre_load
    def _remove_empty_id(self, data, **kwargs):
        if 'DeviceID' in data and data['DeviceID'] == '':
            del data['DeviceID']
        return data


@dataclass
class TrustScore(Resource):
    TRUST_TYPE_DEVICE = 'Device'
    TRUST_TYPE_USER = 'EndUser'
    TRUST_TYPE_EXTERNAL = 'External'
    _TRUST_TYPE_VALUES = (TRUST_TYPE_DEVICE, TRUST_TYPE_USER, TRUST_TYPE_EXTERNAL)
    trust_type: str = field(metadata={'data_key': 'TrustType', 'validate': validate.OneOf(_TRUST_TYPE_VALUES)})
    trust_id: str = field(metadata={'data_key': 'TrustID'})
    score: int = field(metadata={'data_key': 'Score'})
    level: str = field(metadata={'data_key': 'Level'})
    ext_source: str = field(metadata={'data_key': 'ExtSource'})
    reason: str = field(metadata={'data_key': 'Reason'})
    factors_json: str = field(metadata={'data_key': 'FactorsJSON'})
    created_at: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='CreatedAt')})
    deleted_at: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='DeletedAt')})
    last_updated_at: datetime = field(metadata={"marshmallow_field": NanoTimestampField(data_key='LastUpdatedAt')})
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.trust_id

    @property
    def id(self) -> str:
        return self.trust_id

    @property
    def factors(self) -> TrustFactorsV2:
        return TrustFactorsV2.Schema().loads(self.factors_json)
