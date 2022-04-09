from dataclasses import field
from typing import List, Dict, ClassVar, Type, Optional, Union
from datetime import datetime
from uuid import UUID

from marshmallow import Schema, validate, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import NanoTimestampField


@dataclass
class Tunnel:
    class Meta:
        unknown = EXCLUDE

    udp_port_number: int
    keepalive: int
    cidrs: list
    dns_enabled: bool
    domains: list


@dataclass
class AccessTier:
    class Meta:
        unknown = EXCLUDE

    name: str
    address: str
    domains: List[str]
    tunnel_satellite: Tunnel
    tunnel_enduser: Tunnel

    Schema: ClassVar[Schema] = Schema


@dataclass
class AccessTierInfo:
    class Meta:
        unknown = EXCLUDE

    access_tier_id: UUID = field(metadata={"data_key": "id"})
    cluster_name: str

    name: str
    address: str
    domains: List[str]

    created_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='created_at')})
    created_by: str
    updated_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='updated_at')})
    updated_by: str

    status: Optional[str]
    netagents: Optional[list]
    tunnel_satellite: Optional[dict]
    tunnel_enduser: Optional[dict]

    Schema: ClassVar[Schema] = Schema

    @property
    def id(self) -> str:
        return str(self.access_tier_id)

