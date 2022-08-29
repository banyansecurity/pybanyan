from abc import ABC
from dataclasses import field
from typing import List, ClassVar, Type, Optional, Union
from uuid import UUID

from marshmallow import validate, EXCLUDE, Schema
from marshmallow_dataclass import dataclass

from banyan.model import BanyanApiObject, BanyanEnum


class ConnectorStatus(BanyanEnum):
    HEALTHY = "Healthy"
    PARTIALLY_HEALTHY = "PartiallyHealthy"
    PENDING = "Pending"


@dataclass
class PeerAccessTier:
    class Meta:
        unknown = EXCLUDE

    cluster: str
    access_tiers: List[str]


@dataclass
class PeerAccessTierStatus:
    class Meta:
        unknown = EXCLUDE

    access_tier_id: str
    access_tier_name: str
    healthy: bool


@dataclass
class Metadata:
    class Meta:
        unknown = EXCLUDE

    name: str
    display_name: str


@dataclass
class Spec:
    class Meta:
        unknown = EXCLUDE

    api_key_id: str
    peer_access_tiers: List[PeerAccessTier]

    cidrs: Optional[List[str]]
    domains: Optional[List[str]]

    keepalive: int = 20
    disable_snat: bool = False


@dataclass
class Connector(BanyanApiObject):
    class Meta:
        unknown = EXCLUDE

    KIND = "BanyanConnector"
    metadata: Metadata
    spec: Spec
    
    @property
    def name(self):
        return self.metadata.name


@dataclass
class ConnectorInfo(ABC):
    class Meta:
        unknown = EXCLUDE

    id: UUID
    name: str
    spec: str

    cidrs: Optional[List[str]]
    domains: Optional[List[str]]

    created_by: str 
    updated_by: str
    status: str = field(metadata={"validate": validate.OneOf(ConnectorStatus.choices())})
    tunnel_ip_address: Optional[str]
    wireguard_public_key: Optional[str]
    access_tiers: Optional[List[PeerAccessTierStatus]]

    @property
    def connector(self) -> Connector:
        return Connector.Schema().loads(self.spec)
