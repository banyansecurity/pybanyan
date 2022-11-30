from abc import ABC
from dataclasses import field
from datetime import datetime
from ipaddress import IPv4Interface
from typing import ClassVar, Type, Union, Optional

from aenum import StrEnum
from marshmallow import fields, Schema, post_dump
from marshmallow_dataclass import dataclass
from semver import VersionInfo

from banyan.core.exc import BanyanError


class BanyanEnum(StrEnum):

    # noinspection PyTypeChecker
    @classmethod
    def choices(cls):
        return [m.value for m in cls]


class TimestampField(fields.DateTime):
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        elif isinstance(value, int):
            try:
                return datetime.fromtimestamp(value)
            except OSError:
                return None
        else:
            return super()._deserialize(value, attr, data, **kwargs)

    def _serialize(self, value: datetime, attr, obj, **kwargs):
        if not value:
            return 0
        elif isinstance(value, datetime):
            return int(value.timestamp())
        else:
            return super()._serialize(value, attr, obj, **kwargs)


class NanoTimestampField(fields.DateTime):
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        elif isinstance(value, int):
            try:
                return datetime.fromtimestamp(value / 1000000000)
            except Exception as ex:
                raise ValueError(f'{ex.args[0]}, value = {value}, attr = {attr}')
        else:
            return super()._deserialize(value, attr, data, **kwargs)

    def _serialize(self, value: datetime, attr, obj, **kwargs):
        if not value:
            return 0
        elif isinstance(value, datetime):
            try:
                return int(value.timestamp() * 1000000000)
            except OSError:
                return 0
        else:
            return super()._serialize(value, attr, obj, **kwargs)


class MilliTimestampField(fields.DateTime):
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        elif isinstance(value, int):
            try:
                return datetime.fromtimestamp(value / 1000)
            except Exception as ex:
                raise ValueError(f'{ex.args[0]}, value = {value}, attr = {attr}')
        else:
            return super()._deserialize(value, attr, data, **kwargs)

    def _serialize(self, value: datetime, attr, obj, **kwargs):
        if not value:
            return 0
        elif isinstance(value, datetime):
            return int(value.timestamp() * 1000)
        else:
            return super()._serialize(value, attr, obj, **kwargs)


class IPv4InterfaceField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        elif isinstance(value, str):
            try:
                return IPv4Interface(value)
            except Exception as ex:
                raise ValueError(f'{ex.args[0]}, value = {value}, attr = {attr}')
        else:
            return super()._deserialize(value, attr, data, **kwargs)

    def _serialize(self, value, attr, data, **kwargs):
        if not value:
            return ""
        elif isinstance(value, IPv4Interface):
            return str(value)
        else:
            return super()._serialize(value, attr, data, **kwargs)


class VersionField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        elif isinstance(value, str):
            if '_' in value:
                value = value.split('_')[0]
            try:
                return VersionInfo.parse(value)
            except Exception as ex:
                raise ValueError(f'{ex.args[0]}, value = {value}, attr = {attr}')
        else:
            return super()._deserialize(value, attr, data, **kwargs)

    def _serialize(self, value, attr, data, **kwargs):
        if not value:
            return ""
        elif isinstance(value, VersionInfo):
            return str(value)
        else:
            return super()._serialize(value, attr, data, **kwargs)


@dataclass
class BanyanApiObject:
    API_VERSION = "rbac.banyanops.com/v1"
    TYPE = "origin"
    KIND = ""

    apiVersion: Optional[str]
    type: Optional[str]
    kind: str
    Schema: ClassVar[Type[Schema]] = Schema

    def __post_init__(self):
        self.apiVersion = self.API_VERSION
        self.type = self.TYPE
        self.kind = self.KIND

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

    # noinspection PyUnusedLocal
    @post_dump
    def _remove_nulls(self, data, many, **kwargs):
        new_data = dict()
        for key, val in data.items():
            if isinstance(val, dict):
                new_data[key] = self._remove_nulls(val, False, **kwargs)
            elif val is not None:
                new_data[key] = val
        return new_data


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
