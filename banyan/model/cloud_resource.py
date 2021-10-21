from dataclasses import field
from typing import List, ClassVar, Type, Optional, Union
from uuid import UUID

from marshmallow import validate, EXCLUDE, Schema
from marshmallow_dataclass import dataclass

from banyan.model import Resource, BanyanEnum

@dataclass
class ResourceTag:
    class Meta:
        ordered = True

    tag_udid: UUID = field(metadata={"data_key": "id"})
    cloud_resource_id: str
    name: str
    value: str

@dataclass
class CloudResource(Resource):
    class Meta:
        unknown = EXCLUDE

    cloud_provider: str
    account: str
    region: str

    resource_type: str
    resource_id: str
    resource_name: str

    public_dns_name: str
    public_ip: str
    private_dns_name: str
    private_ip: str
    ports: str = ''
    status: str = 'discovered'
    tags: Optional[List[ResourceTag]] = field(default_factory=list)
    parent_id: str = ''
    
    Schema: ClassVar[Schema] = Schema

    @property
    def name(self) -> str:
        return self.resource_name

@dataclass
class CloudResourceInfo(Resource):
    class Meta:
        unknown = EXCLUDE

    resource_udid: UUID = field(metadata={"data_key": "id"})
    cloud_provider: str
    account: str
    region: str

    resource_type: str
    resource_id: str
    resource_name: str

    public_dns_name: str
    public_ip: str
    private_dns_name: str
    private_ip: str
    ports: str
    status: str
    tags: Optional[List[ResourceTag]]
    parent_id: str

    created_at: Optional[int]
    updated_at: Optional[int]
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.resource_name

    @property
    def id(self) -> str:
        return str(self.resource_udid)

@dataclass
class CloudResourceAssociateInfo:
    class Meta:
        unknown = EXCLUDE
    
    id: str
    resource_udid: UUID = field(metadata={"data_key": "cloud_resource_id"})
    resource_id: str
    resource_name: str
    resource_type: str
    resource_status: str = field(metadata={"data_key": "status"})
    service_id: str
    service_name: str
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def cloud_resource_id(self) -> str:
        return str(self.resource_udid)