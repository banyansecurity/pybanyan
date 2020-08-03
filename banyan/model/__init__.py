from abc import ABC
from dataclasses import field
from datetime import datetime
from ipaddress import IPv4Interface
from typing import ClassVar, Type, Union

from marshmallow import fields, Schema
from marshmallow_dataclass import dataclass

from banyan.core.exc import BanyanError

API_VERSION = "rbac.banyanops.com/v1"


class NanoTimestampField(fields.DateTime):
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        elif isinstance(value, int):
            return datetime.fromtimestamp(value / 1000000000)
        else:
            return super()._deserialize(value, attr, data, **kwargs)

    def _serialize(self, value: datetime, attr, obj, **kwargs):
        if not value:
            return 0
        elif isinstance(value, datetime):
            return int(value.timestamp() * 1000000000)
        else:
            return super()._serialize(value, attr, obj, **kwargs)


class IPv4InterfaceField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        elif isinstance(value, str):
            return IPv4Interface(value)
        else:
            return super()._deserialize(value, attr, data, **kwargs)

    def _serialize(self, value, attr, data, **kwargs):
        if not value:
            return ""
        elif isinstance(value, IPv4Interface):
            return str(value)
        else:
            return super()._serialize(value, attr, data, **kwargs)


@dataclass
class BanyanApiObject:
    TYPE = "origin"
    apiVersion: str
    kind: str
    type: str
    Schema: ClassVar[Type[Schema]] = Schema

    def __post_init__(self):
        self.apiVersion = API_VERSION
        self.type = self.TYPE

    @property
    def name(self) -> str:
        raise NotImplementedError('not implemented in the base class')


@dataclass
class Resource(ABC):
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        raise BanyanError('not implemented')

    @property
    def id(self) -> str:
        raise BanyanError('not implemented')


ResourceOrName = Union[Resource, str]


@dataclass
class InfoBase(Resource, ABC):
    created_by: str = field(metadata={'data_key': 'CreatedBy'})
    created_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='CreatedAt')})
    last_updated_by: str = field(metadata={'data_key': 'LastUpdatedBy'})
    last_updated_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='LastUpdatedAt')})
    deleted_by: str = field(metadata={'data_key': 'DeletedBy'})
    deleted_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='DeletedAt')})
    spec: str
    description: str
    Schema: ClassVar[Type[Schema]] = Schema
