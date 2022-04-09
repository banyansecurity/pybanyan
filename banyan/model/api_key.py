from dataclasses import field
from typing import List, ClassVar, Type, Optional, Union
from datetime import datetime
from uuid import UUID

from marshmallow import Schema, validate, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import NanoTimestampField

@dataclass
class ApiKey:
    class Meta:
        unknown = EXCLUDE

    name: str
    secret: str
    description: str
    scope: str

    Schema: ClassVar[Schema] = Schema


@dataclass
class ApiKeyInfo:
    class Meta:
        unknown = EXCLUDE

    api_key_id: UUID = field(metadata={"data_key": "id"})
    org_id: UUID
    name: str
    secret: str
    description: str
    scope: str
    created_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='created_at')})
    created_by: str
    updated_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='updated_at')})
    updated_by: str

    Schema: ClassVar[Schema] = Schema

    @property
    def id(self) -> str:
        return str(self.api_key_id)
    