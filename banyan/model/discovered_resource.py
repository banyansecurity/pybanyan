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

class DiscoveredResourceType(BanyanEnum):
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
class DiscoveredResource(Resource):
    class Meta:
        unknown = EXCLUDE

    cloud_provider: str
    region: str
    resource_id: str
    resource_name: str
    resource_type: str
    public_ip: str
    private_ip: str
    tags: Optional[List[ResourceTag]]
    status: str = 'discovered'
    public_dns_name: Optional[str] = ''
    private_dns_name: Optional[str] = ''
    parent_id: Optional[str] = ''
    Schema: ClassVar[Schema] = Schema

    @property
    def name(self) -> str:
        return self.resource_name


@dataclass
class DiscoveredResourceInfo(Resource):
    class Meta:
        unknown = EXCLUDE

    resource_udid: UUID = field(metadata={"data_key": "id"})
    cloud_provider: str
    region: str
    resource_id: str
    resource_name: str
    resource_type: str
    parent_id: Optional[str]
    public_dns_name: Optional[str]
    public_ip: Optional[str]
    private_dns_name: Optional[str]
    private_ip: str
    created_at: int
    updated_at: int
    tags: Optional[List[ResourceTag]]
    status: str
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.resource_name

    @property
    def id(self) -> str:
        return str(self.resource_udid)
