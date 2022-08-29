from abc import ABC
from dataclasses import field
from uuid import UUID
from datetime import datetime
from typing import List, Dict, Optional, ClassVar

from marshmallow import validate, EXCLUDE, Schema
from marshmallow_dataclass import dataclass

from banyan.model import Resource, BanyanEnum
from banyan.model.netagent import Netagent

class AccessTierStatus(BanyanEnum):
    TERMINATED = "Terminated"
    REPORTING = "Reporting"
    PENDING = "Pending"
    
@dataclass
class TunnelConfig:
    class Meta:
        unknown = EXCLUDE

    udp_port_number: int
    cidrs: Optional[List[str]]
    domains: Optional[List[str]]
    shared_fqdn: Optional[str]

    keepalive: int = 20
    dns_enabled: bool = True
    dns_search_domains: str = ""


@dataclass
class AccessTier(ABC):
    class Meta:
        unknown = EXCLUDE

    name: str
    cluster_name: str
    address: str

    disable_snat: Optional[bool]
    tunnel_satellite: Optional[TunnelConfig]
    tunnel_enduser: Optional[TunnelConfig]


@dataclass
class AccessTierInfo(ABC):
    class Meta:
        unknown = EXCLUDE

    id: UUID
    name: str
    cluster_name: str
    address: str

    disable_snat: Optional[bool]
    tunnel_satellite: Optional[TunnelConfig]
    tunnel_enduser: Optional[TunnelConfig]

    created_by: str 
    updated_by: str
    status: str = field(metadata={"validate": validate.OneOf(AccessTierStatus.choices())})
    netagents: Optional[List[Netagent]]

