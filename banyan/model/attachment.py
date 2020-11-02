from dataclasses import field
from datetime import datetime
from typing import ClassVar, Type
from uuid import UUID

from marshmallow import EXCLUDE, Schema, validate
from marshmallow_dataclass import dataclass

from banyan.model import NanoTimestampField, Resource, BanyanEnum


class AttachmentType(BanyanEnum):
    SERVICE = "service"
    SAAS_APP = "saasapp"


@dataclass
class Attachment(Resource):
    class Meta:
        unknown = EXCLUDE

    policy_id: UUID = field(metadata={'data_key': 'PolicyID'})
    policy_name: str = field(metadata={'data_key': 'PolicyName'})
    attached_to_id: str = field(metadata={'data_key': 'AttachedToID'})
    attached_to_name: str = field(metadata={'data_key': 'AttachedToName'})
    attached_to_type: str = field(metadata={'data_key': 'AttachedToType',
                                            'validate': validate.OneOf(AttachmentType.choices())})
    enabled: bool = field(metadata={'data_key': 'Enabled'})
    attached_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='AttachedAt')})
    attached_by: str = field(metadata={'data_key': 'AttachedBy'})
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.policy_name + '|' + self.attached_to_type + '|' + self.attached_to_name

    @property
    def id(self) -> str:
        return str(self.policy_id) + '|' + self.attached_to_type + '|' + self.attached_to_id
