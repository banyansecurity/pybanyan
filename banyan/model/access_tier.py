from dataclasses import field
from typing import List, Dict, ClassVar, Type, Optional, Union
from datetime import datetime
from uuid import UUID

from marshmallow import Schema, validate, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import NanoTimestampField, BanyanApiObject, Resource


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
    cluster_name: str
    address: str
    domains: Optional[List[str]] = field(default_factory=list)
    tunnel_satellite: Optional[Tunnel] = field(default_factory=dict)
    tunnel_enduser: Optional[Tunnel] = field(default_factory=dict)

    Schema: ClassVar[Schema] = Schema


@dataclass
class AccessTierInfo(Resource):
    class Meta:
        unknown = EXCLUDE

    access_tier_id: UUID = field(metadata={"data_key": "id"})
    access_tier_name: str = field(metadata={"data_key": "name"})
    
    cluster_name: str
    address: str
    tunnel_satellite: Optional[Tunnel]
    tunnel_enduser: Optional[Tunnel]

    created_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='created_at')})
    created_by: str
    updated_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='updated_at')})
    updated_by: str

    status: Optional[str]
    netagents: Optional[list]
    domains: Optional[List[str]]

    Schema: ClassVar[Schema] = Schema

    @property
    def id(self) -> str:
        return str(self.access_tier_id)

    @property
    def name(self) -> str:
        return str(self.access_tier_name)        

