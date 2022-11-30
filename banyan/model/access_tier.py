from dataclasses import field
from typing import List, Dict, ClassVar, Type, Optional, Union
from datetime import datetime
from uuid import UUID

from marshmallow import Schema, validate, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import NanoTimestampField, BanyanApiObject, Resource


@dataclass
class Metadata:
    class Meta:
        unknown = EXCLUDE

    name: str
    description: Optional[str]
    cluster_name: Optional[str]


@dataclass
class AccessTierTunnel:
    class Meta:
        unknown = EXCLUDE

    udp_port_number: int
    cidrs: Optional[List[str]]
    domains: Optional[List[str]]
    keepalive: Optional[int]
    dns_enabled: bool = True


@dataclass 
class Spec:
    class Meta:
        unknown = EXCLUDE

    # sync w metadata
    description: Optional[str]
    cluster_name: str

    api_key_id: UUID
    address: str
    deployment_method: Optional[str]

    tunnel_enduser: Optional[AccessTierTunnel] = field(default_factory=dict)


@dataclass
class AccessTier(BanyanApiObject):
    class Meta:
        unknown = EXCLUDE

    KIND = "BanyanAccessTier"
    metadata: Metadata
    spec: Spec

    def __post_init__(self):
        super().__post_init__()
        # api object bug
        self.metadata.description = self.spec.description
        self.metadata.cluster_name = self.spec.cluster_name

    @property
    def name(self):
        return self.metadata.name



@dataclass
class AccessTierInfo(Resource):
    class Meta:
        unknown = EXCLUDE

    access_tier_id: UUID = field(metadata={"data_key": "id"})
    access_tier_name: str = field(metadata={"data_key": "name"})
    spec: str
    
    description: str
    cluster_name: str
    api_key_id: UUID
    address: str
    deployment_method: str
    tunnel_enduser: Optional[AccessTierTunnel]

    created_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='created_at')})
    created_by: str
    updated_at: datetime = field(metadata={'marshmallow_field': NanoTimestampField(data_key='updated_at')})
    updated_by: str

    status: Optional[str]
    netagents: Optional[list]

    @property
    def access_tier_spec(self) -> AccessTier:
        return AccessTier.Schema().loads(self.spec)

    @property
    def id(self) -> str:
        return str(self.access_tier_id)

    @property
    def name(self) -> str:
        return str(self.access_tier_name)        

