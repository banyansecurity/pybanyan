from dataclasses import field
from typing import List, Dict, ClassVar, Type, Optional, Union
from datetime import datetime
from uuid import UUID

from marshmallow import Schema, validate, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import NanoTimestampField, BanyanApiObject, Resource


@dataclass
class Tags:
    class Meta:
        unknown = EXCLUDE

    icon: Optional[str]
    description_link: Optional[str]


@dataclass
class Metadata:
    class Meta:
        unknown = EXCLUDE

    name: str
    friendly_name: str
    description: str
    tags: Tags = field(default_factory=Tags)


@dataclass
class PeerAccessTier:
    class Meta:
        unknown = EXCLUDE

    cluster: str
    access_tiers: Optional[List[str]]
    connectors: Optional[List[str]]


@dataclass
class Spec:
    class Meta:
        unknown = EXCLUDE

    peer_access_tiers: List[PeerAccessTier]


@dataclass
class ServiceTunnel(BanyanApiObject):
    class Meta:
        unknown = EXCLUDE

    KIND = "BanyanServiceTunnel"
    metadata: Metadata
    spec: Spec

    @property
    def name(self):
        return self.metadata.name


@dataclass
class ServiceTunnelInfo(Resource):
    class Meta:
        unknown = EXCLUDE

    service_tunnel_id: UUID = field(metadata={"data_key": "id"})
    service_tunnel_name: str = field(metadata={"data_key": "name"})
    description: str
    spec: str

    created_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='created_at')})
    created_by: str
    updated_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='updated_at')})
    updated_by: str
    Schema: ClassVar[Schema] = Schema

    @property
    def service(self) -> ServiceTunnel:
        return ServiceTunnel.Schema().loads(self.spec)

    @property
    def name(self) -> str:
        return self.service_tunnel_name

    @property
    def id(self) -> str:
        return self.service_tunnel_id