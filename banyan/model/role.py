from dataclasses import field
from typing import List, Dict, Optional, Union
from uuid import UUID

from marshmallow import validate
from marshmallow_dataclass import dataclass

from banyan.model import BanyanApiObject, InfoBase


@dataclass
class Tags:
    TEMPLATE_USER = "USER"
    TEMPLATE_WORKLOAD = "WORKLOAD"
    TEMPLATE_CUSTOM = "CUSTOM"
    _TEMPLATE_VALUES = (TEMPLATE_USER, TEMPLATE_WORKLOAD, TEMPLATE_CUSTOM)
    template: str = field(metadata={"validate": validate.OneOf(_TEMPLATE_VALUES)})


@dataclass
class Metadata:
    name: str
    description: str
    tags: Tags


@dataclass
class Spec:
    EMPLOYEE_OWNED = "E"
    CORPORATE_DEDICATED = "D"
    CORPORATE_SHARED = "C"
    OTHER = "O"
    _OWNERSHIP_VALUES = (EMPLOYEE_OWNED, CORPORATE_DEDICATED, CORPORATE_SHARED, OTHER)
    known_device_only: Optional[bool]
    label_selector: List[Dict[str, str]] = field(default_factory=list)
    service_account: List[str] = field(default_factory=list)
    image: List[str] = field(default_factory=list)
    repo_tag: List[str] = field(default_factory=list)
    container_fqdn: List[str] = field(default_factory=list)
    group: List[str] = field(default_factory=list)
    email: List[str] = field(default_factory=list)
    device_ownership: List[str] = field(default_factory=list)


@dataclass
class Role(BanyanApiObject):
    KIND = "BanyanRole"
    metadata: Metadata
    spec: Spec

    def __post_init__(self):
        self.kind = self.KIND

    @property
    def name(self):
        return self.metadata.name


@dataclass
class RoleInfo(InfoBase):
    role_id: UUID = field(metadata={'data_key': 'RoleID'})
    role_name: str = field(metadata={'data_key': 'RoleName'})
    spec: str = field(metadata={'data_key': 'RoleSpec'})
    description: str = field(metadata={'data_key': 'Description'})

    type: str = field(metadata={'data_key': 'RoleType'})
    version: int = field(metadata={'data_key': 'RoleVersion'})
    enabled: bool = field(metadata={'data_key': 'Enabled'})

    @property
    def role(self) -> Role:
        return Role.Schema().loads(self.spec)

    @property
    def name(self) -> str:
        return self.role_name

    @property
    def id(self) -> str:
        return str(self.role_id)


RoleInfoOrName = Union[RoleInfo, str]
