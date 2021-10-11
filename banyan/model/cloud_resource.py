from dataclasses import field
from typing import List, ClassVar, Type, Optional, Union
from uuid import UUID

from marshmallow import validate, EXCLUDE, Schema
from marshmallow_dataclass import dataclass

from banyan.model import Resource, BanyanEnum


class CloudProvider(BanyanEnum):
    AWS = "AWS"
    AZURE = "Azure"
    GCP = "GCP"
    OCI = "OCI"

class ExternalCatalog(BanyanEnum):
    OKTA = "Okta"
    AAD = "AzureAD"

class CloudResourceType(BanyanEnum):
    # CloudProvider AWS
    EC2 = "EC2"
    RDS = "RDS"
    ELB = "ELB"

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
    resource_id: str
    resource_name: str
    resource_type: str
    public_dns_name: str
    public_ip: str
    private_dns_name: str
    private_ip: str
    ports: str = ''
    status: str = 'discovered'
    tags: Optional[List[ResourceTag]] = field(default_factory=list)
    parent_id: Optional[str] = ''
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
    resource_id: str
    resource_name: str
    resource_type: str
    parent_id: str
    public_dns_name: str
    public_ip: str
    private_dns_name: str
    private_ip: str
    ports: str
    created_at: int
    updated_at: int
    status: str
    tags: Optional[List[ResourceTag]] = field(default_factory=list)
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

