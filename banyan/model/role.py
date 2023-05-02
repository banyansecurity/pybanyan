from dataclasses import field
from typing import List, Dict, Optional, Union
from uuid import UUID

from marshmallow import validate, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import BanyanApiObject, InfoBase, BanyanEnum


class RoleTemplate(BanyanEnum):
    USER = "USER"
    WORKLOAD = "WORKLOAD"
    CUSTOM = "CUSTOM"


@dataclass
class Tags:
    class Meta:
        unknown = EXCLUDE

    template: str = field(metadata={"validate": validate.OneOf(RoleTemplate.choices())})


@dataclass
class Metadata:
    class Meta:
        unknown = EXCLUDE

    name: str
    description: str
    tags: Tags


class Ownership(BanyanEnum):
    EMPLOYEE_OWNED = "E"
    CORPORATE_DEDICATED = "D"
    CORPORATE_SHARED = "C"
    OTHER = "O"


@dataclass
class Spec:
    class Meta:
        unknown = EXCLUDE

    known_device_only: Optional[bool]
    mdm_present: Optional[bool]
    label_selector: Optional[List[Dict[str, str]]] = field(default_factory=list)
    service_account: Optional[List[str]] = field(default_factory=list)
    image: Optional[List[str]] = field(default_factory=list)
    repo_tag: Optional[List[str]] = field(default_factory=list)
    container_fqdn: Optional[List[str]] = field(default_factory=list)
    group: Optional[List[str]] = field(default_factory=list)
    email: Optional[List[str]] = field(default_factory=list)
    device_ownership: Optional[List[str]] = field(default_factory=list)
    platform: Optional[List[str]] = field(default_factory=list)
    serial_numbers: Optional[List[str]] = field(default_factory=list)


@dataclass
class Role(BanyanApiObject):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    KIND = "BanyanRole"
    metadata: Metadata
    spec: Spec

    @property
    def name(self):
        return self.metadata.name


@dataclass
class RoleInfo(InfoBase):
    class Meta:
        unknown = EXCLUDE

    role_id: UUID = field(metadata={'data_key': 'RoleID'})
    role_name: str = field(metadata={'data_key': 'RoleName'})
    spec: str = field(metadata={'data_key': 'RoleSpec'})
    description: str = field(metadata={'data_key': 'Description'})

    type: str = field(metadata={'data_key': 'RoleType'})
    version: int = field(metadata={'data_key': 'RoleVersion'})
    enabled: bool = field(metadata={'data_key': 'Enabled'})

    @property
    def role_spec(self) -> Role:
        return Role.Schema().loads(self.spec)

    @property
    def name(self) -> str:
        return self.role_name

    @property
    def id(self) -> str:
        return str(self.role_id)


RoleInfoOrName = Union[RoleInfo, str]
