from dataclasses import field
from typing import List, ClassVar, Type, Optional, Union
from datetime import datetime
from uuid import UUID

from marshmallow import Schema, validate, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import NanoTimestampField, Resource

@dataclass
class ApiKey():
    class Meta:
        unknown = EXCLUDE

    name: str
    description: str
    scope: str

    Schema: ClassVar[Schema] = Schema


@dataclass
class ApiKeyInfo(Resource):
    class Meta:
        unknown = EXCLUDE

    api_key_id: UUID = field(metadata={"data_key": "id"})
    api_key_name: str = field(metadata={"data_key": "name"})
    org_id: UUID
    secret: str
    description: str
    scope: str
    created_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='created_at')})
    created_by: str
    updated_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='updated_at')})
    updated_by: str

    @property
    def id(self) -> str:
        return str(self.api_key_id)
    
    @property
    def name(self) -> str:
        return str(self.api_key_name)
