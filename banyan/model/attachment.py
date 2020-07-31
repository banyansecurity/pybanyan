from dataclasses import field
from datetime import datetime
from typing import ClassVar, Type
from uuid import UUID

from marshmallow import Schema, validate
from marshmallow_dataclass import dataclass

from banyan.model import NanoTimestampField


@dataclass
class Attachment:
    SERVICE = "service"
    SAAS_APP = "saasapp"
    _ATTACH_TYPES = (SERVICE, SAAS_APP)
    policy_id: UUID = field(metadata={'data_key': 'PolicyID'})
    policy_name: str = field(metadata={'data_key': 'PolicyName'})
    attached_to_id: str = field(metadata={'data_key': 'AttachedToID'})
    attached_to_name: str = field(metadata={'data_key': 'AttachedToName'})
    attached_to_type: str = field(metadata={'data_key': 'AttachedToType',
                                            'validate': validate.OneOf(_ATTACH_TYPES)})
    enabled: bool = field(metadata={'data_key': 'Enabled'})
    attached_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='AttachedAt')})
    attached_by: str = field(metadata={'data_key': 'AttachedBy'})
    Schema: ClassVar[Type[Schema]] = Schema