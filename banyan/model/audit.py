import json
from dataclasses import field
from datetime import datetime
from typing import ClassVar, Type, Optional
from uuid import UUID

from marshmallow import Schema, validate, pre_load, EXCLUDE
from marshmallow_dataclass import dataclass

from banyan.model import Resource, NanoTimestampField, BanyanEnum
from banyan.model.attachment import Attachment
from banyan.model.policy import PolicyInfo
from banyan.model.role import RoleInfo
from banyan.model.service import ServiceInfo


class AuditEventType(BanyanEnum):
    ADMIN_SIGN_ON = "admin_sign_on"
    IDP_SETTINGS = "idp_settings"
    MDM_SETTINGS = "mdm_settings"
    TRUSTSCORE_FACTORS = "trustscore_factors"
    UNKNOWN_DEVICE_SETTINGS = "unknown_device"
    SECURITY_ATTACH_POLICY = "security_attach_policy"
    POLICY = "policy"
    REGISTERED_SERVICE = "registered_service"
    ROLE = "role"
    DEVICE_REGISTRATION_IDP_SETTINGS = "device_registration_idp_settings"
    ADMIN_USER = "admin_user"
    MDM_DEPLOY_OTP_SKIP_ROLE = "mdm_deploy_otp_skip_role"
    MDM_DEPLOY_KEY = "mdm_deploy_key"
    INVITATION_CODE = "invitation_code"
    TRUSTSCORE_TTL = "trustscore_ttl"
    ENDUSER_DEVICE = "enduser_device"
    PREFERRED_APPLICATIONS = "preferred_applications"
    LATEST_OS_CONFIG = "latest_os_config"
    TRUST_CONFIG = "trust_config"
    ROOT_CERTS = "root_certs"
    SAAS_APPLICATIONS = "saas_applications"
    IDP_ROUTED_APPLICATIONS = "idp_routed_applications"


class AuditAction(BanyanEnum):
    UPDATE = "update"
    CREATE = "create"
    DELETE = "delete"
    ENABLE = "enable"
    DISABLE = "disable"


@dataclass
class AuditEvent(Resource):
    class Meta:
        unknown = EXCLUDE

    event_id: str = field(metadata={"data_key": "id"})
    event_type: str = field(metadata={"data_key": "type", "validate": validate.OneOf(AuditEventType.choices())})
    org_id: UUID
    created_at: datetime = field(metadata={"marshmallow_field": NanoTimestampField()})
    message: str
    action: str = field(metadata={"validate": validate.OneOf(AuditAction.choices())})
    admin_email: str
    changes_new: Optional[str]
    changes_old: Optional[str]
    Schema: ClassVar[Type[Schema]] = Schema

    @property
    def name(self) -> str:
        return self.id

    @property
    def id(self) -> str:
        return str(self.event_id)

    def _extract_obj(self, obj_str: str) -> Resource:
        if self.event_type == AuditEventType.REGISTERED_SERVICE:
            return ServiceInfo.Schema().loads(obj_str)
        elif self.event_type == AuditEventType.POLICY:
            return PolicyInfo.Schema().loads(obj_str)
        elif self.event_type == AuditEventType.ROLE:
            return RoleInfo.Schema().loads(obj_str)
        elif self.event_type == AuditEventType.SECURITY_ATTACH_POLICY:
            return Attachment.Schema().loads(obj_str)
        else:
            raise ValueError(f'unknown object type for deserialization: {self.event_type}')

    @property
    def object_old(self) -> Resource:
        return self._extract_obj(self.changes_old) if self.changes_old else None

    @property
    def object_new(self) -> Resource:
        return self._extract_obj(self.changes_new) if self.changes_new else None

    # noinspection PyUnusedLocal
    # pylint: disable=W0613,R0201
    @pre_load
    def _remove_empty_dates(self, data, many, **kwargs):
        if "changes_new" in data and data["changes_new"] is not None:
            data["changes_new"] = json.dumps(data["changes_new"])
        if "changes_old" in data and data["changes_old"] is not None:
            data["changes_old"] = json.dumps(data["changes_old"])
        return data
