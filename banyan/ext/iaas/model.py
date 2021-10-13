from typing import Dict, List
from dataclasses import dataclass, field

@dataclass
class IaasLevel:
    type: str
    id: str = ''
    name: str = ''

@dataclass
class IaasLocation:
    type: str
    id: str = ''
    name: str = ''
    #latlong?

@dataclass
class IaasInstance:
    type: str
    id: str = ''
    name: str = ''
    public_dns_name: str = ''
    public_ip: str = ''
    private_dns_name: str = ''
    private_ip: str = ''
    ports: List = field(default_factory=list)
    tags: Dict = field(default_factory=dict)

@dataclass
class IaasResource:
    provider: str
    account: IaasLevel
    parent: IaasLevel
    location: IaasLocation
    instance: IaasInstance



