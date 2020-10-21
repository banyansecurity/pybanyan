from dataclasses import field
from datetime import datetime
from ipaddress import IPv4Address
from typing import List, Dict, ClassVar, Type, Optional, Any
from uuid import UUID

import OpenSSL.crypto
from marshmallow import fields, Schema, validate, pre_load, INCLUDE
from marshmallow_dataclass import dataclass
from marshmallow.fields import Integer, String, Dict
from semver import VersionInfo

from banyan.model import Resource, NanoTimestampField, MilliTimestampField
from banyan.model.netagent import Netagent

import json


@dataclass
class AuditEvent(Resource):
    TYPE_ADMIN_SIGN_ON = "admin_sign_on"
    TYPE_IDP_SETTINGS = "idp_settings"
    TYPE_MDM_SETTINGS = "mdm_settings"
    TYPE_TRUSTSCORE_FACTORS = "trustscore_factors"
    TYPE_UNKNOWN_DEVICE_SETTINGS = "unknown_device"
    TYPE_SECURITY_ATTACH_POLICY = "security_attach_policy"
    TYPE_POLICY = "policy"
    TYPE_REGISTERED_SERVICE = "registered_service"
    TYPE_ROLE = "role"
    TYPE_DEVICE_REGISTRATION_IDP_SETTINGS = "device_registration_idp_settings"
    TYPE_ADMIN_USER = "admin_user"
    TYPE_MDM_DEPLOY_OTP_SKIP_ROLE = "mdm_deploy_otp_skip_role"
    TYPE_MDM_DEPLOY_KEY = "mdm_deploy_key"
    TYPE_INVITATION_CODE = "invitation_code"
    TYPE_TRUSTSCORE_TTL = "trustscore_ttl"
    TYPE_ENDUSER_DEVICE = "enduser_device"
    TYPE_PREFERRED_APPLICATIONS = "preferred_applications"
    TYPE_LATEST_OS_CONFIG = "latest_os_config"
    TYPE_TRUST_CONFIG = "trust_config"
    TYPE_ROOT_CERTS = "root_certs"
    TYPE_SAAS_APPLICATIONS = "saas_applications"
    TYPE_IDP_ROUTED_APPLICATIONS = "idp_routed_applications"
    _AUDIT_EVENT_TYPES = (TYPE_ADMIN_SIGN_ON, TYPE_ADMIN_USER, TYPE_DEVICE_REGISTRATION_IDP_SETTINGS,
                          TYPE_ENDUSER_DEVICE, TYPE_IDP_ROUTED_APPLICATIONS, TYPE_IDP_SETTINGS, TYPE_INVITATION_CODE,
                          TYPE_LATEST_OS_CONFIG, TYPE_MDM_DEPLOY_KEY, TYPE_MDM_DEPLOY_OTP_SKIP_ROLE, TYPE_MDM_SETTINGS,
                          TYPE_POLICY, TYPE_PREFERRED_APPLICATIONS, TYPE_REGISTERED_SERVICE, TYPE_ROLE, TYPE_ROOT_CERTS,
                          TYPE_SAAS_APPLICATIONS, TYPE_SECURITY_ATTACH_POLICY, TYPE_TRUST_CONFIG, TYPE_TRUSTSCORE_FACTORS,
                          TYPE_TRUSTSCORE_TTL, TYPE_UNKNOWN_DEVICE_SETTINGS)

    ACTION_UPDATE = "update"
    ACTION_CREATE = "create"
    ACTION_DELETE = "delete"
    ACTION_ENABLE = "enable"
    ACTION_DISABLE = "disable"
    _ACTIONS = (ACTION_UPDATE, ACTION_CREATE, ACTION_DELETE, ACTION_ENABLE, ACTION_DISABLE)

    class Meta:
        unknown = INCLUDE

    event_id: str = field(metadata={"data_key": "id"})
    event_type: str = field(metadata={"data_key": "type", "validate": validate.OneOf(_AUDIT_EVENT_TYPES)})
    org_id: UUID
    created_at: datetime = field(metadata={"marshmallow_field": NanoTimestampField()})
    message: str
    action: str = field(metadata={"validate": validate.OneOf(_ACTIONS)})
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

    @pre_load
    def _remove_empty_dates(self, data, many, **kwargs):
        if "changes_new" in data and data["changes_new"] is not None:
            data["changes_new"] = json.dumps(data["changes_new"])
        if "changes_old" in data and data["changes_old"] is not None:
                data["changes_old"] = json.dumps(data["changes_old"])
        return data
