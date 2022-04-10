from dataclasses import field
from typing import List, Dict, ClassVar, Type, Optional, Union
from datetime import datetime
from uuid import UUID

from marshmallow import Schema, validate, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import BanyanApiObject, NanoTimestampField, Resource


@dataclass
class Metadata:
    class Meta:
        unknown = EXCLUDE

    name: str
    display_name: str


@dataclass
class PeerAccessTier:
    class Meta:
        unknown = EXCLUDE

    cluster: str
    access_tiers: List[str]


@dataclass
class Spec:
    class Meta:
        unknown = EXCLUDE

    api_key_id: UUID
    keepalive: int
    cidrs: List[str]
    peer_access_tiers: List[PeerAccessTier]


@dataclass
class Connector(BanyanApiObject):
    class Meta:
        unknown = EXCLUDE

    KIND = "BanyanConnector"
    metadata: Metadata
    spec: Spec

    def __post_init__(self):
        self.kind = self.KIND

    @property
    def name(self):
        return self.metadata.name


@dataclass
class ConnectorInfo(Resource):
    class Meta:
        unknown = EXCLUDE

    connector_id: UUID = field(metadata={"data_key": "id"})
    connector_name: str = field(metadata={"data_key": "name"})
    org_id: UUID
    display_name: str
    api_key_id: UUID
    keepalive: int
    cidrs: List[str]
    spec: str

    created_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='created_at')})
    created_by: str
    updated_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='updated_at')})
    updated_by: str

    tunnel_ip_address: Optional[str]
    status: Optional[str]
    wireguard_public_key: Optional[str]
    access_tiers: Optional[list]
    connector_version: Optional[str]
    host_info: Optional[dict]

    Schema: ClassVar[Schema] = Schema

    @property
    def id(self) -> str:
        return str(self.connector_id)

    @property
    def name(self) -> str:
        return str(self.connector_name)

    @property
    def connector(self) -> Connector:
        return Connector.Schema().loads(self.spec)
        
    