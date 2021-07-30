from dataclasses import field
from typing import List, ClassVar, Type, Optional, Union
from uuid import UUID

from marshmallow import validate, EXCLUDE, Schema
from marshmallow_dataclass import dataclass

from banyan.model import Resource, BanyanEnum


@dataclass
class CloudResourceService(Resource):
    class Meta:
        unknown = EXCLUDE
    cloud_resource_service_id: UUID = field(metadata={"data_key": "id"})
    cloud_resource_id: str
    service_id: str
    created_at: int
    created_by: str
    updated_at: int
    updated_by: str

    @property
    def name(self) -> str:
        return self.service_id

    @property
    def id(self) -> str:
        return str(self.cloud_resource_service_id)


@dataclass
class CloudResourceServiceDetails(Resource):
    class Meta:
        unknown = EXCLUDE

    cloud_resource_service_id: UUID = field(metadata={"data_key": "id"})
    cloud_resource_id: str
    service_id: str
    created_at: int
    created_by: str
    updated_at: int
    updated_by: str
    port: int
    service_name: str
    service_type: str
    service_spec: str
    cluster_name: str
    resource_id: str
    resource_name: str
    resource_type: str
    status: str
    public_dns_name: Optional[str]
    public_ip: Optional[str]
    private_dns_name: Optional[str]
    private_ip: str
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.resource_name

    @property
    def id(self) -> str:
        return str(self.cloud_resource_service_id)
