import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.v1_mdm_deploy_config_deploy_key import V1MdmDeployConfigDeployKey
from openapi_client.apis.paths.v1_latest_os import V1LatestOs
from openapi_client.apis.paths.v1_delete_device import V1DeleteDevice
from openapi_client.apis.paths.v1_enduser_facing_devices import V1EnduserFacingDevices
from openapi_client.apis.paths.v1_enduser_facing_services import V1EnduserFacingServices
from openapi_client.apis.paths.v1_enduser_facing_set_max_trust_level import V1EnduserFacingSetMaxTrustLevel
from openapi_client.apis.paths.v1_policy_policy_id_attachment import V1PolicyPolicyIDAttachment
from openapi_client.apis.paths.v1_security_policies import V1SecurityPolicies
from openapi_client.apis.paths.v2_device_trustscore_exclusion import V2DeviceTrustscoreExclusion
from openapi_client.apis.paths.v2_enduser_facing_logs import V2EnduserFacingLogs
from openapi_client.apis.paths.v2_enduser_facing_integration_device_identity_command import V2EnduserFacingIntegrationDeviceIdentityCommand
from openapi_client.apis.paths.v2_integration_crowdstrike import V2IntegrationCrowdstrike
from openapi_client.apis.paths.v2_tunnel_cidr_id import V2TunnelCidrId
from openapi_client.apis.paths.v1_all_apps import V1AllApps
from openapi_client.apis.paths.v1_banyanidp_admin_user_reset import V1BanyanidpAdminUserReset
from openapi_client.apis.paths.v1_banyanidp_enduser_forgotpassword import V1BanyanidpEnduserForgotpassword
from openapi_client.apis.paths.v1_insert_pwless_config import V1InsertPwlessConfig
from openapi_client.apis.paths.v1_send_device_notification import V1SendDeviceNotification
from openapi_client.apis.paths.v1_set_max_trust_level import V1SetMaxTrustLevel
from openapi_client.apis.paths.v1_enduser_facing_trustscores import V1EnduserFacingTrustscores
from openapi_client.apis.paths.v1_unregistered_device_endusers_csv import V1UnregisteredDeviceEndusersCsv
from openapi_client.apis.paths.v1_cert_exchange import V1CertExchange
from openapi_client.apis.paths.v2_enduser_facing_client_cert_issue import V2EnduserFacingClientCertIssue
from openapi_client.apis.paths.v2_deploy_config_otp_skip_eligible_role import V2DeployConfigOtpSkipEligibleRole
from openapi_client.apis.paths.v1_events import V1Events
from openapi_client.apis.paths.v2_access_tier_id import V2AccessTierId
from openapi_client.apis.paths.v2_auth_user_metadata import V2AuthUserMetadata
from openapi_client.apis.paths.v2_report import V2Report
from openapi_client.apis.paths.v2_devices_csv import V2DevicesCsv
from openapi_client.apis.paths.v2_cloud_resource_service_id import V2CloudResourceServiceId
from openapi_client.apis.paths.v2_signup import V2Signup
from openapi_client.apis.paths.v2_signup_internal import V2SignupInternal
from openapi_client.apis.paths.v2_mom_org import V2MomOrg
from openapi_client.apis.paths.v2_mom_org_org_id import V2MomOrgOrgId
from openapi_client.apis.paths.v1_endusers_stats import V1EndusersStats
from openapi_client.apis.paths.v1_security_attach_policies import V1SecurityAttachPolicies
from openapi_client.apis.paths.v2_event_daily_counts import V2EventDailyCounts
from openapi_client.apis.paths.v1_config_url import V1ConfigUrl
from openapi_client.apis.paths.v1_delete_org import V1DeleteOrg
from openapi_client.apis.paths.v2_bundle_bundle_id import V2BundleBundleId
from openapi_client.apis.paths.v2_enduser_facing_service_tunnel import V2EnduserFacingServiceTunnel
from openapi_client.apis.paths.v2_externalcert_id_services import V2ExternalcertIdServices
from openapi_client.apis.paths.v2_integration_sync_config import V2IntegrationSyncConfig
from openapi_client.apis.paths.v2_integration_sync_stats_device_csv import V2IntegrationSyncStatsDeviceCsv
from openapi_client.apis.paths.v2_unregistered_device_endusers import V2UnregisteredDeviceEndusers
from openapi_client.apis.paths.v1_hostagents_stats import V1HostagentsStats
from openapi_client.apis.paths.v1_enable_registered_service import V1EnableRegisteredService
from openapi_client.apis.paths.v1_securityroles_stats import V1SecurityrolesStats
from openapi_client.apis.paths.v2_access_tier_tunnel import V2AccessTierTunnel
from openapi_client.apis.paths.v2_service_bundle import V2ServiceBundle
from openapi_client.apis.paths.v2_tunnel_resource_ct import V2TunnelResourceCt
from openapi_client.apis.paths.v2_tunnel_resource_dns import V2TunnelResourceDns
from openapi_client.apis.paths.v2_tunnel_resource_id import V2TunnelResourceId
from openapi_client.apis.paths.v2_tunnel_resource import V2TunnelResource
from openapi_client.apis.paths.v2_signup_captcha import V2SignupCaptcha
from openapi_client.apis.paths.v1_mdm_deploy_config_otp_skip_roles import V1MdmDeployConfigOtpSkipRoles
from openapi_client.apis.paths.v1_policies_stats import V1PoliciesStats
from openapi_client.apis.paths.v2_cloud_resource_id import V2CloudResourceId
from openapi_client.apis.paths.v2_service_account_id import V2ServiceAccountId
from openapi_client.apis.paths.v2_registered_domain_challenge_id import V2RegisteredDomainChallengeId
from openapi_client.apis.paths.v2_service_account import V2ServiceAccount
from openapi_client.apis.paths.v1_access_tiers_stats import V1AccessTiersStats
from openapi_client.apis.paths.v1_saml_metadata import V1SamlMetadata
from openapi_client.apis.paths.v1_admin_add_user import V1AdminAddUser
from openapi_client.apis.paths.v1_disable_security_role import V1DisableSecurityRole
from openapi_client.apis.paths.v2_externalcert_id import V2ExternalcertId
from openapi_client.apis.paths.v2_externalcert import V2Externalcert
from openapi_client.apis.paths.v2_global_domain_directory import V2GlobalDomainDirectory
from openapi_client.apis.paths.v2_refresh_token import V2RefreshToken
from openapi_client.apis.paths.v1_policy_attachment_attached_to_type_attached_to_id import V1PolicyAttachmentAttachedToTypeAttachedToID
from openapi_client.apis.paths.v1_insert_security_role import V1InsertSecurityRole
from openapi_client.apis.paths.v2_access_tier_tunnel_id import V2AccessTierTunnelId
from openapi_client.apis.paths.v2_endusers import V2Endusers
from openapi_client.apis.paths.v2_enduser_facing_bundle import V2EnduserFacingBundle
from openapi_client.apis.paths.v1_banyanidp_enduser_authorize import V1BanyanidpEnduserAuthorize
from openapi_client.apis.paths.v1_config import V1Config
from openapi_client.apis.paths.v1_enable_security_role import V1EnableSecurityRole
from openapi_client.apis.paths.v2_externalcert_id_retry_issuance import V2ExternalcertIdRetryIssuance
from openapi_client.apis.paths.v2_signup_provision_org import V2SignupProvisionOrg
from openapi_client.apis.paths.v2_signup_provision_org_org_id import V2SignupProvisionOrgOrgId
from openapi_client.apis.paths.v1_org_status import V1OrgStatus
from openapi_client.apis.paths.v1_services_stats import V1ServicesStats
from openapi_client.apis.paths.unregistered_device_endusers_stats import UnregisteredDeviceEndusersStats
from openapi_client.apis.paths.v2_api_key_id import V2ApiKeyId
from openapi_client.apis.paths.v2_enduser_facing_favorite_service_service_id import V2EnduserFacingFavoriteServiceServiceId
from openapi_client.apis.paths.v2_integration import V2Integration
from openapi_client.apis.paths.v2_service_tunnel import V2ServiceTunnel
from openapi_client.apis.paths.v1_access_activity import V1AccessActivity
from openapi_client.apis.paths.v1_ca_certs import V1CaCerts
from openapi_client.apis.paths.v1_delete_pwless_config import V1DeletePwlessConfig
from openapi_client.apis.paths.health import Health
from openapi_client.apis.paths.v1_update_org import V1UpdateOrg
from openapi_client.apis.paths.v2_integration_sync_stats import V2IntegrationSyncStats
from openapi_client.apis.paths.v2_integration_test_credentials import V2IntegrationTestCredentials
from openapi_client.apis.paths.v2_superadmin_upload_product_analytics_csv import V2SuperadminUploadProductAnalyticsCsv
from openapi_client.apis.paths.v1_mdm_deploy_config import V1MdmDeployConfig
from openapi_client.apis.paths.v1_banyanidp_enduser_profile import V1BanyanidpEnduserProfile
from openapi_client.apis.paths.v1_security_roles_enduser_devices import V1SecurityRolesEnduserDevices
from openapi_client.apis.paths.v1_mdm_insert_devices import V1MdmInsertDevices
from openapi_client.apis.paths.v1_trustscore_config_device_org_preferred_apps import V1TrustscoreConfigDeviceOrgPreferredApps
from openapi_client.apis.paths.v2_enduser_groups import V2EnduserGroups
from openapi_client.apis.paths.v2_integration_device_identity_command import V2IntegrationDeviceIdentityCommand
from openapi_client.apis.paths.v2_registered_domain_id import V2RegisteredDomainId
from openapi_client.apis.paths.v2_registered_domain import V2RegisteredDomain
from openapi_client.apis.paths.v1_endusers import V1Endusers
from openapi_client.apis.paths.v2_devices import V2Devices
from openapi_client.apis.paths.v2_satellite import V2Satellite
from openapi_client.apis.paths.v1_policy_attachment_attached_to_type import V1PolicyAttachmentAttachedToType
from openapi_client.apis.paths.v1_admin_list_users import V1AdminListUsers
from openapi_client.apis.paths.v2_cert_update_prepare import V2CertUpdatePrepare
from openapi_client.apis.paths.v2_enduser_facing_autorun_service import V2EnduserFacingAutorunService
from openapi_client.apis.paths.v1_admin_list_orgs import V1AdminListOrgs
from openapi_client.apis.paths.v1_mdm_otdp import V1MdmOtdp
from openapi_client.apis.paths.v1_insert_default_registered_services import V1InsertDefaultRegisteredServices
from openapi_client.apis.paths.v1_service_connection_test import V1ServiceConnectionTest
from openapi_client.apis.paths.v1_user_org_details import V1UserOrgDetails
from openapi_client.apis.paths.v2_client_certificate import V2ClientCertificate
from openapi_client.apis.paths.v1_enduser_devices_data import V1EnduserDevicesData
from openapi_client.apis.paths.v1_enduser_devices import V1EnduserDevices
from openapi_client.apis.paths.v1_event_types import V1EventTypes
from openapi_client.apis.paths.v1_shield_config import V1ShieldConfig
from openapi_client.apis.paths.v2_api_key_scope import V2ApiKeyScope
from openapi_client.apis.paths.v2_cloud_resource_service import V2CloudResourceService
from openapi_client.apis.paths.v2_enduser_facing_favorite_service import V2EnduserFacingFavoriteService
from openapi_client.apis.paths.v1_trustscore_config_device_trustscore_factors import V1TrustscoreConfigDeviceTrustscoreFactors
from openapi_client.apis.paths.v1_banyanidp_admin_group_user import V1BanyanidpAdminGroupUser
from openapi_client.apis.paths.v1_enduser_facing_device_features import V1EnduserFacingDeviceFeatures
from openapi_client.apis.paths.v1_invite_code import V1InviteCode
from openapi_client.apis.paths.v1_insert_registered_service import V1InsertRegisteredService
from openapi_client.apis.paths.v1_security_events_type_count import V1SecurityEventsTypeCount
from openapi_client.apis.paths.v2_access_tier import V2AccessTier
from openapi_client.apis.paths.v2_access_tier_id_registered_services import V2AccessTierIdRegisteredServices
from openapi_client.apis.paths.v2_cert_update import V2CertUpdate
from openapi_client.apis.paths.v2_command_center_settings import V2CommandCenterSettings
from openapi_client.apis.paths.v2_enduser_facing_autorun_service_service_id import V2EnduserFacingAutorunServiceServiceId
from openapi_client.apis.paths.v2_integration_test_credentials_crowdstrike import V2IntegrationTestCredentialsCrowdstrike
from openapi_client.apis.paths.service_tunnel_id_security_policy_policy_id import ServiceTunnelIdSecurityPolicyPolicyId
from openapi_client.apis.paths.v2_shield_config import V2ShieldConfig
from openapi_client.apis.paths.v1_enduser_facing_org_details import V1EnduserFacingOrgDetails
from openapi_client.apis.paths.v1_delete_netagent import V1DeleteNetagent
from openapi_client.apis.paths.v1_registered_services import V1RegisteredServices
from openapi_client.apis.paths.v1_delete_security_policy import V1DeleteSecurityPolicy
from openapi_client.apis.paths.v1_delete_security_role import V1DeleteSecurityRole
from openapi_client.apis.paths.v2_cert_request_device_only_registration import V2CertRequestDeviceOnlyRegistration
from openapi_client.apis.paths.v2_cloud_resource import V2CloudResource
from openapi_client.apis.paths.v2_enduser_facing_tunnel_config import V2EnduserFacingTunnelConfig
from openapi_client.apis.paths.v2_integration_sentinelone import V2IntegrationSentinelone
from openapi_client.apis.paths.v2_signup_org_names import V2SignupOrgNames
from openapi_client.apis.paths.v2_satellite_facing_config_satellite_name import V2SatelliteFacingConfigSatelliteName
from openapi_client.apis.paths.service_tunnel_id_security_policy import ServiceTunnelIdSecurityPolicy
from openapi_client.apis.paths.v1_trustscore_config_device_trustscore_ttl import V1TrustscoreConfigDeviceTrustscoreTtl
from openapi_client.apis.paths.v1_enduser_facing_app_version import V1EnduserFacingAppVersion
from openapi_client.apis.paths.v2_bundle import V2Bundle
from openapi_client.apis.paths.v2_registered_domain_challenge import V2RegisteredDomainChallenge
from openapi_client.apis.paths.v1_banyanidp_enduser_confirmforgotpassword import V1BanyanidpEnduserConfirmforgotpassword
from openapi_client.apis.paths.v1_mdm_device_info import V1MdmDeviceInfo
from openapi_client.apis.paths.v1_insert_security_attach_policy import V1InsertSecurityAttachPolicy
from openapi_client.apis.paths.v2_enduser import V2Enduser
from openapi_client.apis.paths.v2_enduser_facing_login_services import V2EnduserFacingLoginServices
from openapi_client.apis.paths.v2_registered_domain_id_validate import V2RegisteredDomainIdValidate
from openapi_client.apis.paths.v2_tunnel_cidr import V2TunnelCidr
from openapi_client.apis.paths.v1_banyanidp_admin_user_changepassword import V1BanyanidpAdminUserChangepassword
from openapi_client.apis.paths.v1_one_time_security_key import V1OneTimeSecurityKey
from openapi_client.apis.paths.v1_delete_registered_service import V1DeleteRegisteredService
from openapi_client.apis.paths.v1_disable_registered_service import V1DisableRegisteredService
from openapi_client.apis.paths.v1_unregistered_device_endusers import V1UnregisteredDeviceEndusers
from openapi_client.apis.paths.v2_integration_signal import V2IntegrationSignal
from openapi_client.apis.paths.v2_satellite_id import V2SatelliteId
from openapi_client.apis.paths.v2_satellite_facing_satellite_name_status import V2SatelliteFacingSatelliteNameStatus
from openapi_client.apis.paths.v2_connector_stats import V2ConnectorStats
from openapi_client.apis.paths.v1_audit_logs import V1AuditLogs
from openapi_client.apis.paths.v1_device_refresh_certs import V1DeviceRefreshCerts
from openapi_client.apis.paths.v1_netagents import V1Netagents
from openapi_client.apis.paths.v1_policy_attachment import V1PolicyAttachment
from openapi_client.apis.paths.v1_security_roles import V1SecurityRoles
from openapi_client.apis.paths.v1_events_feed import V1EventsFeed
from openapi_client.apis.paths.health_authentication import HealthAuthentication
from openapi_client.apis.paths.v1_mdm_resend_otdp_mail import V1MdmResendOtdpMail
from openapi_client.apis.paths.insert_saasapp import InsertSaasapp
from openapi_client.apis.paths.v1_delete_shield_cluster import V1DeleteShieldCluster
from openapi_client.apis.paths.v1_device_id_token import V1DeviceIdToken
from openapi_client.apis.paths.v2_deploy_config_otp_skip_role import V2DeployConfigOtpSkipRole
from openapi_client.apis.paths.v2_enduser_facing_bundle_bundle_id import V2EnduserFacingBundleBundleId
from openapi_client.apis.paths.v2_service_tunnel_id import V2ServiceTunnelId
from openapi_client.apis.paths.v2_upload_enduser_counts_csv import V2UploadEnduserCountsCsv
from openapi_client.apis.paths.v1_banyanidp_enduser_signin import V1BanyanidpEnduserSignin
from openapi_client.apis.paths.v1_delete_security_attach_policy import V1DeleteSecurityAttachPolicy
from openapi_client.apis.paths.v2_signup_resend_email import V2SignupResendEmail
from openapi_client.apis.paths.v2_signup_provision_org_retry import V2SignupProvisionOrgRetry
from openapi_client.apis.paths.v2_staged_device_cert_password import V2StagedDeviceCertPassword
from openapi_client.apis.paths.v1_api_v1_admin_saml import V1ApiV1AdminSaml
from openapi_client.apis.paths.v1_device_unregister import V1DeviceUnregister
from openapi_client.apis.paths.v1_add_org import V1AddOrg
from openapi_client.apis.paths.v1_org_details import V1OrgDetails
from openapi_client.apis.paths.v2_command_center_settings_id import V2CommandCenterSettingsId
from openapi_client.apis.paths.v2_onboarding_state import V2OnboardingState
from openapi_client.apis.paths.v2_satellite_facing_satellite_name_iptables import V2SatelliteFacingSatelliteNameIptables
from openapi_client.apis.paths.v1_banyanidp_admin_user import V1BanyanidpAdminUser
from openapi_client.apis.paths.v2_bundle_bundle_id_service import V2BundleBundleIdService
from openapi_client.apis.paths.v2_bundle_bundle_id_service_service_id import V2BundleBundleIdServiceServiceId
from openapi_client.apis.paths.v1_banyanidp_enduser_resendconfirmationcode import V1BanyanidpEnduserResendconfirmationcode
from openapi_client.apis.paths.v1_admin_delete_user import V1AdminDeleteUser
from openapi_client.apis.paths.v1_trustscore import V1Trustscore
from openapi_client.apis.paths.v1_one_click_support_bundle import V1OneClickSupportBundle
from openapi_client.apis.paths.v1_admin_update_user import V1AdminUpdateUser
from openapi_client.apis.paths.v2_service_metadata_service_id import V2ServiceMetadataServiceId
from openapi_client.apis.paths.v2_service_metadata_services import V2ServiceMetadataServices
from openapi_client.apis.paths.v2_admin_client_certificate import V2AdminClientCertificate
from openapi_client.apis.paths.v2_enduser_id import V2EnduserId
from openapi_client.apis.paths.v2_integration_partner import V2IntegrationPartner
from openapi_client.apis.paths.v1_api_v1_admin_setup_saml import V1ApiV1AdminSetupSaml
from openapi_client.apis.paths.v2_enduser_facing_bundle_bundle_id_service import V2EnduserFacingBundleBundleIdService
from openapi_client.apis.paths.v2_enduser_facing_bundle_bundle_id_service_service_id import V2EnduserFacingBundleBundleIdServiceServiceId
from openapi_client.apis.paths.v2_enduser_facing_org_support import V2EnduserFacingOrgSupport
from openapi_client.apis.paths.v1_banyanidp_admin_group import V1BanyanidpAdminGroup
from openapi_client.apis.paths.banyanidp_admin_user import BanyanidpAdminUser
from openapi_client.apis.paths.v1_banyanidp_enduser_newpassword import V1BanyanidpEnduserNewpassword
from openapi_client.apis.paths.v1_refresh_token import V1RefreshToken
from openapi_client.apis.paths.v1_security_events import V1SecurityEvents
from openapi_client.apis.paths.v1_insert_security_policy import V1InsertSecurityPolicy
from openapi_client.apis.paths.v2_access_tier_access_tier_id_tunnel_config_tunnel_config_id import V2AccessTierAccessTierIdTunnelConfigTunnelConfigId
from openapi_client.apis.paths.v2_service_bundle_bundled_service_id import V2ServiceBundleBundledServiceId
from openapi_client.apis.paths.v1_active_users import V1ActiveUsers
from openapi_client.apis.paths.v1_admin_trustscore_profiles import V1AdminTrustscoreProfiles
from openapi_client.apis.paths.v1_trustscore_config_device_latest_os import V1TrustscoreConfigDeviceLatestOs
from openapi_client.apis.paths.v1_banyanidp_admin_user_enable import V1BanyanidpAdminUserEnable
from openapi_client.apis.paths.v1_banyanidp_admin_user_group import V1BanyanidpAdminUserGroup
from openapi_client.apis.paths.v1_banyanidp_admin_user_password import V1BanyanidpAdminUserPassword
from openapi_client.apis.paths.v1_device_register import V1DeviceRegister
from openapi_client.apis.paths.v1_devices import V1Devices
from openapi_client.apis.paths.v1_devices_stats import V1DevicesStats
from openapi_client.apis.paths.v1_endusers_csv import V1EndusersCsv
from openapi_client.apis.paths.v1_events_count import V1EventsCount
from openapi_client.apis.paths.v1_hosts import V1Hosts
from openapi_client.apis.paths.v1_impersonate import V1Impersonate
from openapi_client.apis.paths.v1_api_v1_reset_password import V1ApiV1ResetPassword
from openapi_client.apis.paths.v1_service_hostname_mapping import V1ServiceHostnameMapping
from openapi_client.apis.paths.v1_mdm_update_device import V1MdmUpdateDevice
from openapi_client.apis.paths.v2_superadmin_validate_private_key_records import V2SuperadminValidatePrivateKeyRecords
from openapi_client.apis.paths.v2_api_key import V2ApiKey
from openapi_client.apis.paths.v2_access_tier_access_tier_id_config import V2AccessTierAccessTierIdConfig
from openapi_client.apis.paths.v2_access_tier_access_tier_id_test import V2AccessTierAccessTierIdTest
from openapi_client.apis.paths.v2_access_tier_facing_access_tier_name_config import V2AccessTierFacingAccessTierNameConfig
from openapi_client.apis.paths.v2_access_tier_facing_access_tier_name_cert_request import V2AccessTierFacingAccessTierNameCertRequest

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_MDM_DEPLOY_CONFIG_DEPLOY_KEY: V1MdmDeployConfigDeployKey,
        PathValues.V1_LATEST_OS: V1LatestOs,
        PathValues.V1_DELETE_DEVICE: V1DeleteDevice,
        PathValues.V1_ENDUSER_FACING_DEVICES: V1EnduserFacingDevices,
        PathValues.V1_ENDUSER_FACING_SERVICES: V1EnduserFacingServices,
        PathValues.V1_ENDUSER_FACING_SET_MAX_TRUST_LEVEL: V1EnduserFacingSetMaxTrustLevel,
        PathValues.V1_POLICY_POLICY_ID_ATTACHMENT: V1PolicyPolicyIDAttachment,
        PathValues.V1_SECURITY_POLICIES: V1SecurityPolicies,
        PathValues.V2_DEVICE_TRUSTSCORE_EXCLUSION: V2DeviceTrustscoreExclusion,
        PathValues.V2_ENDUSER_FACING_LOGS: V2EnduserFacingLogs,
        PathValues.V2_ENDUSER_FACING_INTEGRATION_DEVICE_IDENTITY_COMMAND: V2EnduserFacingIntegrationDeviceIdentityCommand,
        PathValues.V2_INTEGRATION_CROWDSTRIKE: V2IntegrationCrowdstrike,
        PathValues.V2_TUNNEL_CIDR_ID: V2TunnelCidrId,
        PathValues.V1_ALL_APPS: V1AllApps,
        PathValues.V1_BANYANIDP_ADMIN_USER_RESET: V1BanyanidpAdminUserReset,
        PathValues.V1_BANYANIDP_ENDUSER_FORGOTPASSWORD: V1BanyanidpEnduserForgotpassword,
        PathValues.V1_INSERT_PWLESS_CONFIG: V1InsertPwlessConfig,
        PathValues.V1_SEND_DEVICE_NOTIFICATION: V1SendDeviceNotification,
        PathValues.V1_SET_MAX_TRUST_LEVEL: V1SetMaxTrustLevel,
        PathValues.V1_ENDUSER_FACING_TRUSTSCORES: V1EnduserFacingTrustscores,
        PathValues.V1_UNREGISTERED_DEVICE_ENDUSERS_CSV: V1UnregisteredDeviceEndusersCsv,
        PathValues.V1_CERT_EXCHANGE: V1CertExchange,
        PathValues.V2_ENDUSER_FACING_CLIENT_CERT_ISSUE: V2EnduserFacingClientCertIssue,
        PathValues.V2_DEPLOY_CONFIG_OTP_SKIP_ELIGIBLE_ROLE: V2DeployConfigOtpSkipEligibleRole,
        PathValues.V1_EVENTS: V1Events,
        PathValues.V2_ACCESS_TIER_ID: V2AccessTierId,
        PathValues.V2_AUTH_USER_METADATA: V2AuthUserMetadata,
        PathValues.V2_REPORT: V2Report,
        PathValues.V2_DEVICES_CSV: V2DevicesCsv,
        PathValues.V2_CLOUD_RESOURCE_SERVICE_ID: V2CloudResourceServiceId,
        PathValues.V2_SIGNUP: V2Signup,
        PathValues.V2_SIGNUP_INTERNAL: V2SignupInternal,
        PathValues.V2_MOM_ORG: V2MomOrg,
        PathValues.V2_MOM_ORG_ORG_ID: V2MomOrgOrgId,
        PathValues.V1_ENDUSERS_STATS: V1EndusersStats,
        PathValues.V1_SECURITY_ATTACH_POLICIES: V1SecurityAttachPolicies,
        PathValues.V2_EVENT_DAILY_COUNTS: V2EventDailyCounts,
        PathValues.V1_CONFIG_URL: V1ConfigUrl,
        PathValues.V1_DELETE_ORG: V1DeleteOrg,
        PathValues.V2_BUNDLE_BUNDLE_ID: V2BundleBundleId,
        PathValues.V2_ENDUSER_FACING_SERVICE_TUNNEL: V2EnduserFacingServiceTunnel,
        PathValues.V2_EXTERNALCERT_ID_SERVICES: V2ExternalcertIdServices,
        PathValues.V2_INTEGRATION_SYNC_CONFIG: V2IntegrationSyncConfig,
        PathValues.V2_INTEGRATION_SYNC_STATS_DEVICE_CSV: V2IntegrationSyncStatsDeviceCsv,
        PathValues.V2_UNREGISTERED_DEVICE_ENDUSERS: V2UnregisteredDeviceEndusers,
        PathValues.V1_HOSTAGENTS_STATS: V1HostagentsStats,
        PathValues.V1_ENABLE_REGISTERED_SERVICE: V1EnableRegisteredService,
        PathValues.V1_SECURITYROLES_STATS: V1SecurityrolesStats,
        PathValues.V2_ACCESS_TIER_TUNNEL: V2AccessTierTunnel,
        PathValues.V2_SERVICE_BUNDLE: V2ServiceBundle,
        PathValues.V2_TUNNEL_RESOURCE_CT: V2TunnelResourceCt,
        PathValues.V2_TUNNEL_RESOURCE_DNS: V2TunnelResourceDns,
        PathValues.V2_TUNNEL_RESOURCE_ID: V2TunnelResourceId,
        PathValues.V2_TUNNEL_RESOURCE: V2TunnelResource,
        PathValues.V2_SIGNUP_CAPTCHA: V2SignupCaptcha,
        PathValues.V1_MDM_DEPLOY_CONFIG_OTP_SKIP_ROLES: V1MdmDeployConfigOtpSkipRoles,
        PathValues.V1_POLICIES_STATS: V1PoliciesStats,
        PathValues.V2_CLOUD_RESOURCE_ID: V2CloudResourceId,
        PathValues.V2_SERVICE_ACCOUNT_ID: V2ServiceAccountId,
        PathValues.V2_REGISTERED_DOMAIN_CHALLENGE_ID: V2RegisteredDomainChallengeId,
        PathValues.V2_SERVICE_ACCOUNT: V2ServiceAccount,
        PathValues.V1_ACCESS_TIERS_STATS: V1AccessTiersStats,
        PathValues.V1_SAML_METADATA: V1SamlMetadata,
        PathValues.V1_ADMIN_ADD_USER: V1AdminAddUser,
        PathValues.V1_DISABLE_SECURITY_ROLE: V1DisableSecurityRole,
        PathValues.V2_EXTERNALCERT_ID: V2ExternalcertId,
        PathValues.V2_EXTERNALCERT: V2Externalcert,
        PathValues.V2_GLOBAL_DOMAIN_DIRECTORY: V2GlobalDomainDirectory,
        PathValues.V2_REFRESH_TOKEN: V2RefreshToken,
        PathValues.V1_POLICY_ATTACHMENT_ATTACHED_TO_TYPE_ATTACHED_TO_ID: V1PolicyAttachmentAttachedToTypeAttachedToID,
        PathValues.V1_INSERT_SECURITY_ROLE: V1InsertSecurityRole,
        PathValues.V2_ACCESS_TIER_TUNNEL_ID: V2AccessTierTunnelId,
        PathValues.V2_ENDUSERS: V2Endusers,
        PathValues.V2_ENDUSER_FACING_BUNDLE: V2EnduserFacingBundle,
        PathValues.V1_BANYANIDP_ENDUSER_AUTHORIZE: V1BanyanidpEnduserAuthorize,
        PathValues.V1_CONFIG: V1Config,
        PathValues.V1_ENABLE_SECURITY_ROLE: V1EnableSecurityRole,
        PathValues.V2_EXTERNALCERT_ID_RETRYISSUANCE: V2ExternalcertIdRetryIssuance,
        PathValues.V2_SIGNUP_PROVISION_ORG: V2SignupProvisionOrg,
        PathValues.V2_SIGNUP_PROVISION_ORG_ORG_ID: V2SignupProvisionOrgOrgId,
        PathValues.V1_ORG_STATUS: V1OrgStatus,
        PathValues.V1_SERVICES_STATS: V1ServicesStats,
        PathValues.UNREGISTERED_DEVICE_ENDUSERS_STATS: UnregisteredDeviceEndusersStats,
        PathValues.V2_API_KEY_ID: V2ApiKeyId,
        PathValues.V2_ENDUSER_FACING_FAVORITE_SERVICE_SERVICE_ID: V2EnduserFacingFavoriteServiceServiceId,
        PathValues.V2_INTEGRATION: V2Integration,
        PathValues.V2_SERVICE_TUNNEL: V2ServiceTunnel,
        PathValues.V1_ACCESS_ACTIVITY: V1AccessActivity,
        PathValues.V1_CA_CERTS: V1CaCerts,
        PathValues.V1_DELETE_PWLESS_CONFIG: V1DeletePwlessConfig,
        PathValues.HEALTH: Health,
        PathValues.V1_UPDATE_ORG: V1UpdateOrg,
        PathValues.V2_INTEGRATION_SYNC_STATS: V2IntegrationSyncStats,
        PathValues.V2_INTEGRATION_TEST_CREDENTIALS: V2IntegrationTestCredentials,
        PathValues.V2_SUPERADMIN_UPLOAD_PRODUCT_ANALYTICS_CSV: V2SuperadminUploadProductAnalyticsCsv,
        PathValues.V1_MDM_DEPLOY_CONFIG: V1MdmDeployConfig,
        PathValues.V1_BANYANIDP_ENDUSER_PROFILE: V1BanyanidpEnduserProfile,
        PathValues.V1_SECURITY_ROLES_ENDUSER_DEVICES: V1SecurityRolesEnduserDevices,
        PathValues.V1_MDM_INSERT_DEVICES: V1MdmInsertDevices,
        PathValues.V1_TRUSTSCORE_CONFIG_DEVICE_ORG_PREFERRED_APPS: V1TrustscoreConfigDeviceOrgPreferredApps,
        PathValues.V2_ENDUSER_GROUPS: V2EnduserGroups,
        PathValues.V2_INTEGRATION_DEVICE_IDENTITY_COMMAND: V2IntegrationDeviceIdentityCommand,
        PathValues.V2_REGISTERED_DOMAIN_ID: V2RegisteredDomainId,
        PathValues.V2_REGISTERED_DOMAIN: V2RegisteredDomain,
        PathValues.V1_ENDUSERS: V1Endusers,
        PathValues.V2_DEVICES: V2Devices,
        PathValues.V2_SATELLITE: V2Satellite,
        PathValues.V1_POLICY_ATTACHMENT_ATTACHED_TO_TYPE: V1PolicyAttachmentAttachedToType,
        PathValues.V1_ADMIN_LIST_USERS: V1AdminListUsers,
        PathValues.V2_CERT_UPDATE_PREPARE: V2CertUpdatePrepare,
        PathValues.V2_ENDUSER_FACING_AUTORUN_SERVICE: V2EnduserFacingAutorunService,
        PathValues.V1_ADMIN_LIST_ORGS: V1AdminListOrgs,
        PathValues.V1_MDM_OTDP: V1MdmOtdp,
        PathValues.V1_INSERT_DEFAULT_REGISTERED_SERVICES: V1InsertDefaultRegisteredServices,
        PathValues.V1_SERVICE_CONNECTION_TEST: V1ServiceConnectionTest,
        PathValues.V1_USER_ORG_DETAILS: V1UserOrgDetails,
        PathValues.V2_CLIENT_CERTIFICATE: V2ClientCertificate,
        PathValues.V1_ENDUSER_DEVICES_DATA: V1EnduserDevicesData,
        PathValues.V1_ENDUSER_DEVICES: V1EnduserDevices,
        PathValues.V1_EVENT_TYPES: V1EventTypes,
        PathValues.V1_SHIELD_CONFIG: V1ShieldConfig,
        PathValues.V2_API_KEY_SCOPE: V2ApiKeyScope,
        PathValues.V2_CLOUD_RESOURCE_SERVICE: V2CloudResourceService,
        PathValues.V2_ENDUSER_FACING_FAVORITE_SERVICE: V2EnduserFacingFavoriteService,
        PathValues.V1_TRUSTSCORE_CONFIG_DEVICE_TRUSTSCORE_FACTORS: V1TrustscoreConfigDeviceTrustscoreFactors,
        PathValues.V1_BANYANIDP_ADMIN_GROUP_USER: V1BanyanidpAdminGroupUser,
        PathValues.V1_ENDUSER_FACING_DEVICE_FEATURES: V1EnduserFacingDeviceFeatures,
        PathValues.V1_INVITE_CODE: V1InviteCode,
        PathValues.V1_INSERT_REGISTERED_SERVICE: V1InsertRegisteredService,
        PathValues.V1_SECURITY_EVENTS_TYPE_COUNT: V1SecurityEventsTypeCount,
        PathValues.V2_ACCESS_TIER: V2AccessTier,
        PathValues.V2_ACCESS_TIER_ID_REGISTERED_SERVICES: V2AccessTierIdRegisteredServices,
        PathValues.V2_CERT_UPDATE: V2CertUpdate,
        PathValues.V2_COMMAND_CENTER_SETTINGS: V2CommandCenterSettings,
        PathValues.V2_ENDUSER_FACING_AUTORUN_SERVICE_SERVICE_ID: V2EnduserFacingAutorunServiceServiceId,
        PathValues.V2_INTEGRATION_TEST_CREDENTIALS_CROWDSTRIKE: V2IntegrationTestCredentialsCrowdstrike,
        PathValues.SERVICE_TUNNEL_ID_SECURITY_POLICY_POLICY_ID: ServiceTunnelIdSecurityPolicyPolicyId,
        PathValues.V2_SHIELD_CONFIG: V2ShieldConfig,
        PathValues.V1_ENDUSER_FACING_ORG_DETAILS: V1EnduserFacingOrgDetails,
        PathValues.V1_DELETE_NETAGENT: V1DeleteNetagent,
        PathValues.V1_REGISTERED_SERVICES: V1RegisteredServices,
        PathValues.V1_DELETE_SECURITY_POLICY: V1DeleteSecurityPolicy,
        PathValues.V1_DELETE_SECURITY_ROLE: V1DeleteSecurityRole,
        PathValues.V2_CERT_REQUEST_DEVICE_ONLY_REGISTRATION: V2CertRequestDeviceOnlyRegistration,
        PathValues.V2_CLOUD_RESOURCE: V2CloudResource,
        PathValues.V2_ENDUSER_FACING_TUNNEL_CONFIG: V2EnduserFacingTunnelConfig,
        PathValues.V2_INTEGRATION_SENTINELONE: V2IntegrationSentinelone,
        PathValues.V2_SIGNUP_ORG_NAMES: V2SignupOrgNames,
        PathValues.V2_SATELLITE_FACING_CONFIG_SATELLITE_NAME: V2SatelliteFacingConfigSatelliteName,
        PathValues.SERVICE_TUNNEL_ID_SECURITY_POLICY: ServiceTunnelIdSecurityPolicy,
        PathValues.V1_TRUSTSCORE_CONFIG_DEVICE_TRUSTSCORE_TTL: V1TrustscoreConfigDeviceTrustscoreTtl,
        PathValues.V1_ENDUSER_FACING_APP_VERSION: V1EnduserFacingAppVersion,
        PathValues.V2_BUNDLE: V2Bundle,
        PathValues.V2_REGISTERED_DOMAIN_CHALLENGE: V2RegisteredDomainChallenge,
        PathValues.V1_BANYANIDP_ENDUSER_CONFIRMFORGOTPASSWORD: V1BanyanidpEnduserConfirmforgotpassword,
        PathValues.V1_MDM_DEVICE_INFO: V1MdmDeviceInfo,
        PathValues.V1_INSERT_SECURITY_ATTACH_POLICY: V1InsertSecurityAttachPolicy,
        PathValues.V2_ENDUSER: V2Enduser,
        PathValues.V2_ENDUSER_FACING_LOGIN_SERVICES: V2EnduserFacingLoginServices,
        PathValues.V2_REGISTERED_DOMAIN_ID_VALIDATE: V2RegisteredDomainIdValidate,
        PathValues.V2_TUNNEL_CIDR: V2TunnelCidr,
        PathValues.V1_BANYANIDP_ADMIN_USER_CHANGEPASSWORD: V1BanyanidpAdminUserChangepassword,
        PathValues.V1_ONE_TIME_SECURITY_KEY: V1OneTimeSecurityKey,
        PathValues.V1_DELETE_REGISTERED_SERVICE: V1DeleteRegisteredService,
        PathValues.V1_DISABLE_REGISTERED_SERVICE: V1DisableRegisteredService,
        PathValues.V1_UNREGISTERED_DEVICE_ENDUSERS: V1UnregisteredDeviceEndusers,
        PathValues.V2_INTEGRATION_SIGNAL: V2IntegrationSignal,
        PathValues.V2_SATELLITE_ID: V2SatelliteId,
        PathValues.V2_SATELLITE_FACING_SATELLITE_NAME_STATUS: V2SatelliteFacingSatelliteNameStatus,
        PathValues.V2_CONNECTOR_STATS: V2ConnectorStats,
        PathValues.V1_AUDIT_LOGS: V1AuditLogs,
        PathValues.V1_DEVICE_REFRESH_CERTS: V1DeviceRefreshCerts,
        PathValues.V1_NETAGENTS: V1Netagents,
        PathValues.V1_POLICY_ATTACHMENT: V1PolicyAttachment,
        PathValues.V1_SECURITY_ROLES: V1SecurityRoles,
        PathValues.V1_EVENTS_FEED: V1EventsFeed,
        PathValues.HEALTH_AUTHENTICATION: HealthAuthentication,
        PathValues.V1_MDM_RESEND_OTDP_MAIL: V1MdmResendOtdpMail,
        PathValues.INSERT_SAASAPP: InsertSaasapp,
        PathValues.V1_DELETE_SHIELD_CLUSTER: V1DeleteShieldCluster,
        PathValues.V1_DEVICE_ID_TOKEN: V1DeviceIdToken,
        PathValues.V2_DEPLOY_CONFIG_OTP_SKIP_ROLE: V2DeployConfigOtpSkipRole,
        PathValues.V2_ENDUSER_FACING_BUNDLE_BUNDLE_ID: V2EnduserFacingBundleBundleId,
        PathValues.V2_SERVICE_TUNNEL_ID: V2ServiceTunnelId,
        PathValues.V2_UPLOAD_ENDUSER_COUNTS_CSV: V2UploadEnduserCountsCsv,
        PathValues.V1_BANYANIDP_ENDUSER_SIGNIN: V1BanyanidpEnduserSignin,
        PathValues.V1_DELETE_SECURITY_ATTACH_POLICY: V1DeleteSecurityAttachPolicy,
        PathValues.V2_SIGNUP_RESEND_EMAIL: V2SignupResendEmail,
        PathValues.V2_SIGNUP_PROVISION_ORG_RETRY: V2SignupProvisionOrgRetry,
        PathValues.V2_STAGED_DEVICE_CERT_PASSWORD: V2StagedDeviceCertPassword,
        PathValues.V1_API_V1_ADMIN_SAML: V1ApiV1AdminSaml,
        PathValues.V1_DEVICE_UNREGISTER: V1DeviceUnregister,
        PathValues.V1_ADD_ORG: V1AddOrg,
        PathValues.V1_ORG_DETAILS: V1OrgDetails,
        PathValues.V2_COMMAND_CENTER_SETTINGS_ID: V2CommandCenterSettingsId,
        PathValues.V2_ONBOARDING_STATE: V2OnboardingState,
        PathValues.V2_SATELLITE_FACING_SATELLITE_NAME_IPTABLES: V2SatelliteFacingSatelliteNameIptables,
        PathValues.V1_BANYANIDP_ADMIN_USER: V1BanyanidpAdminUser,
        PathValues.V2_BUNDLE_BUNDLE_ID_SERVICE: V2BundleBundleIdService,
        PathValues.V2_BUNDLE_BUNDLE_ID_SERVICE_SERVICE_ID: V2BundleBundleIdServiceServiceId,
        PathValues.V1_BANYANIDP_ENDUSER_RESENDCONFIRMATIONCODE: V1BanyanidpEnduserResendconfirmationcode,
        PathValues.V1_ADMIN_DELETE_USER: V1AdminDeleteUser,
        PathValues.V1_TRUSTSCORE: V1Trustscore,
        PathValues.V1_ONE_CLICK_SUPPORT_BUNDLE: V1OneClickSupportBundle,
        PathValues.V1_ADMIN_UPDATE_USER: V1AdminUpdateUser,
        PathValues.V2_SERVICE_METADATA_SERVICE_ID: V2ServiceMetadataServiceId,
        PathValues.V2_SERVICE_METADATA_SERVICES: V2ServiceMetadataServices,
        PathValues.V2_ADMIN_CLIENT_CERTIFICATE: V2AdminClientCertificate,
        PathValues.V2_ENDUSER_ID: V2EnduserId,
        PathValues.V2_INTEGRATION_PARTNER: V2IntegrationPartner,
        PathValues.V1_API_V1_ADMIN_SETUP_SAML: V1ApiV1AdminSetupSaml,
        PathValues.V2_ENDUSER_FACING_BUNDLE_BUNDLE_ID_SERVICE: V2EnduserFacingBundleBundleIdService,
        PathValues.V2_ENDUSER_FACING_BUNDLE_BUNDLE_ID_SERVICE_SERVICE_ID: V2EnduserFacingBundleBundleIdServiceServiceId,
        PathValues.V2_ENDUSER_FACING_ORG_SUPPORT: V2EnduserFacingOrgSupport,
        PathValues.V1_BANYANIDP_ADMIN_GROUP: V1BanyanidpAdminGroup,
        PathValues.BANYANIDP_ADMIN_USER: BanyanidpAdminUser,
        PathValues.V1_BANYANIDP_ENDUSER_NEWPASSWORD: V1BanyanidpEnduserNewpassword,
        PathValues.V1_REFRESH_TOKEN: V1RefreshToken,
        PathValues.V1_SECURITY_EVENTS: V1SecurityEvents,
        PathValues.V1_INSERT_SECURITY_POLICY: V1InsertSecurityPolicy,
        PathValues.V2_ACCESS_TIER_ACCESS_TIER_ID_TUNNEL_CONFIG_TUNNEL_CONFIG_ID: V2AccessTierAccessTierIdTunnelConfigTunnelConfigId,
        PathValues.V2_SERVICE_BUNDLE_BUNDLEDSERVICEID: V2ServiceBundleBundledServiceId,
        PathValues.V1_ACTIVE_USERS: V1ActiveUsers,
        PathValues.V1_ADMIN_TRUSTSCORE_PROFILES: V1AdminTrustscoreProfiles,
        PathValues.V1_TRUSTSCORE_CONFIG_DEVICE_LATEST_OS: V1TrustscoreConfigDeviceLatestOs,
        PathValues.V1_BANYANIDP_ADMIN_USER_ENABLE: V1BanyanidpAdminUserEnable,
        PathValues.V1_BANYANIDP_ADMIN_USER_GROUP: V1BanyanidpAdminUserGroup,
        PathValues.V1_BANYANIDP_ADMIN_USER_PASSWORD: V1BanyanidpAdminUserPassword,
        PathValues.V1_DEVICE_REGISTER: V1DeviceRegister,
        PathValues.V1_DEVICES: V1Devices,
        PathValues.V1_DEVICES_STATS: V1DevicesStats,
        PathValues.V1_ENDUSERS_CSV: V1EndusersCsv,
        PathValues.V1_EVENTS_COUNT: V1EventsCount,
        PathValues.V1_HOSTS: V1Hosts,
        PathValues.V1_IMPERSONATE: V1Impersonate,
        PathValues.V1_API_V1_RESET_PASSWORD: V1ApiV1ResetPassword,
        PathValues.V1_SERVICE_HOSTNAME_MAPPING: V1ServiceHostnameMapping,
        PathValues.V1_MDM_UPDATE_DEVICE: V1MdmUpdateDevice,
        PathValues.V2_SUPERADMIN_VALIDATE_PRIVATE_KEY_RECORDS: V2SuperadminValidatePrivateKeyRecords,
        PathValues.V2_API_KEY: V2ApiKey,
        PathValues.V2_ACCESS_TIER_ACCESS_TIER_ID_CONFIG: V2AccessTierAccessTierIdConfig,
        PathValues.V2_ACCESS_TIER_ACCESS_TIER_ID_TEST: V2AccessTierAccessTierIdTest,
        PathValues.V2_ACCESS_TIER_FACING_ACCESS_TIER_NAME_CONFIG: V2AccessTierFacingAccessTierNameConfig,
        PathValues.V2_ACCESS_TIER_FACING_ACCESS_TIER_NAME_CERT_REQUEST: V2AccessTierFacingAccessTierNameCertRequest,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_MDM_DEPLOY_CONFIG_DEPLOY_KEY: V1MdmDeployConfigDeployKey,
        PathValues.V1_LATEST_OS: V1LatestOs,
        PathValues.V1_DELETE_DEVICE: V1DeleteDevice,
        PathValues.V1_ENDUSER_FACING_DEVICES: V1EnduserFacingDevices,
        PathValues.V1_ENDUSER_FACING_SERVICES: V1EnduserFacingServices,
        PathValues.V1_ENDUSER_FACING_SET_MAX_TRUST_LEVEL: V1EnduserFacingSetMaxTrustLevel,
        PathValues.V1_POLICY_POLICY_ID_ATTACHMENT: V1PolicyPolicyIDAttachment,
        PathValues.V1_SECURITY_POLICIES: V1SecurityPolicies,
        PathValues.V2_DEVICE_TRUSTSCORE_EXCLUSION: V2DeviceTrustscoreExclusion,
        PathValues.V2_ENDUSER_FACING_LOGS: V2EnduserFacingLogs,
        PathValues.V2_ENDUSER_FACING_INTEGRATION_DEVICE_IDENTITY_COMMAND: V2EnduserFacingIntegrationDeviceIdentityCommand,
        PathValues.V2_INTEGRATION_CROWDSTRIKE: V2IntegrationCrowdstrike,
        PathValues.V2_TUNNEL_CIDR_ID: V2TunnelCidrId,
        PathValues.V1_ALL_APPS: V1AllApps,
        PathValues.V1_BANYANIDP_ADMIN_USER_RESET: V1BanyanidpAdminUserReset,
        PathValues.V1_BANYANIDP_ENDUSER_FORGOTPASSWORD: V1BanyanidpEnduserForgotpassword,
        PathValues.V1_INSERT_PWLESS_CONFIG: V1InsertPwlessConfig,
        PathValues.V1_SEND_DEVICE_NOTIFICATION: V1SendDeviceNotification,
        PathValues.V1_SET_MAX_TRUST_LEVEL: V1SetMaxTrustLevel,
        PathValues.V1_ENDUSER_FACING_TRUSTSCORES: V1EnduserFacingTrustscores,
        PathValues.V1_UNREGISTERED_DEVICE_ENDUSERS_CSV: V1UnregisteredDeviceEndusersCsv,
        PathValues.V1_CERT_EXCHANGE: V1CertExchange,
        PathValues.V2_ENDUSER_FACING_CLIENT_CERT_ISSUE: V2EnduserFacingClientCertIssue,
        PathValues.V2_DEPLOY_CONFIG_OTP_SKIP_ELIGIBLE_ROLE: V2DeployConfigOtpSkipEligibleRole,
        PathValues.V1_EVENTS: V1Events,
        PathValues.V2_ACCESS_TIER_ID: V2AccessTierId,
        PathValues.V2_AUTH_USER_METADATA: V2AuthUserMetadata,
        PathValues.V2_REPORT: V2Report,
        PathValues.V2_DEVICES_CSV: V2DevicesCsv,
        PathValues.V2_CLOUD_RESOURCE_SERVICE_ID: V2CloudResourceServiceId,
        PathValues.V2_SIGNUP: V2Signup,
        PathValues.V2_SIGNUP_INTERNAL: V2SignupInternal,
        PathValues.V2_MOM_ORG: V2MomOrg,
        PathValues.V2_MOM_ORG_ORG_ID: V2MomOrgOrgId,
        PathValues.V1_ENDUSERS_STATS: V1EndusersStats,
        PathValues.V1_SECURITY_ATTACH_POLICIES: V1SecurityAttachPolicies,
        PathValues.V2_EVENT_DAILY_COUNTS: V2EventDailyCounts,
        PathValues.V1_CONFIG_URL: V1ConfigUrl,
        PathValues.V1_DELETE_ORG: V1DeleteOrg,
        PathValues.V2_BUNDLE_BUNDLE_ID: V2BundleBundleId,
        PathValues.V2_ENDUSER_FACING_SERVICE_TUNNEL: V2EnduserFacingServiceTunnel,
        PathValues.V2_EXTERNALCERT_ID_SERVICES: V2ExternalcertIdServices,
        PathValues.V2_INTEGRATION_SYNC_CONFIG: V2IntegrationSyncConfig,
        PathValues.V2_INTEGRATION_SYNC_STATS_DEVICE_CSV: V2IntegrationSyncStatsDeviceCsv,
        PathValues.V2_UNREGISTERED_DEVICE_ENDUSERS: V2UnregisteredDeviceEndusers,
        PathValues.V1_HOSTAGENTS_STATS: V1HostagentsStats,
        PathValues.V1_ENABLE_REGISTERED_SERVICE: V1EnableRegisteredService,
        PathValues.V1_SECURITYROLES_STATS: V1SecurityrolesStats,
        PathValues.V2_ACCESS_TIER_TUNNEL: V2AccessTierTunnel,
        PathValues.V2_SERVICE_BUNDLE: V2ServiceBundle,
        PathValues.V2_TUNNEL_RESOURCE_CT: V2TunnelResourceCt,
        PathValues.V2_TUNNEL_RESOURCE_DNS: V2TunnelResourceDns,
        PathValues.V2_TUNNEL_RESOURCE_ID: V2TunnelResourceId,
        PathValues.V2_TUNNEL_RESOURCE: V2TunnelResource,
        PathValues.V2_SIGNUP_CAPTCHA: V2SignupCaptcha,
        PathValues.V1_MDM_DEPLOY_CONFIG_OTP_SKIP_ROLES: V1MdmDeployConfigOtpSkipRoles,
        PathValues.V1_POLICIES_STATS: V1PoliciesStats,
        PathValues.V2_CLOUD_RESOURCE_ID: V2CloudResourceId,
        PathValues.V2_SERVICE_ACCOUNT_ID: V2ServiceAccountId,
        PathValues.V2_REGISTERED_DOMAIN_CHALLENGE_ID: V2RegisteredDomainChallengeId,
        PathValues.V2_SERVICE_ACCOUNT: V2ServiceAccount,
        PathValues.V1_ACCESS_TIERS_STATS: V1AccessTiersStats,
        PathValues.V1_SAML_METADATA: V1SamlMetadata,
        PathValues.V1_ADMIN_ADD_USER: V1AdminAddUser,
        PathValues.V1_DISABLE_SECURITY_ROLE: V1DisableSecurityRole,
        PathValues.V2_EXTERNALCERT_ID: V2ExternalcertId,
        PathValues.V2_EXTERNALCERT: V2Externalcert,
        PathValues.V2_GLOBAL_DOMAIN_DIRECTORY: V2GlobalDomainDirectory,
        PathValues.V2_REFRESH_TOKEN: V2RefreshToken,
        PathValues.V1_POLICY_ATTACHMENT_ATTACHED_TO_TYPE_ATTACHED_TO_ID: V1PolicyAttachmentAttachedToTypeAttachedToID,
        PathValues.V1_INSERT_SECURITY_ROLE: V1InsertSecurityRole,
        PathValues.V2_ACCESS_TIER_TUNNEL_ID: V2AccessTierTunnelId,
        PathValues.V2_ENDUSERS: V2Endusers,
        PathValues.V2_ENDUSER_FACING_BUNDLE: V2EnduserFacingBundle,
        PathValues.V1_BANYANIDP_ENDUSER_AUTHORIZE: V1BanyanidpEnduserAuthorize,
        PathValues.V1_CONFIG: V1Config,
        PathValues.V1_ENABLE_SECURITY_ROLE: V1EnableSecurityRole,
        PathValues.V2_EXTERNALCERT_ID_RETRYISSUANCE: V2ExternalcertIdRetryIssuance,
        PathValues.V2_SIGNUP_PROVISION_ORG: V2SignupProvisionOrg,
        PathValues.V2_SIGNUP_PROVISION_ORG_ORG_ID: V2SignupProvisionOrgOrgId,
        PathValues.V1_ORG_STATUS: V1OrgStatus,
        PathValues.V1_SERVICES_STATS: V1ServicesStats,
        PathValues.UNREGISTERED_DEVICE_ENDUSERS_STATS: UnregisteredDeviceEndusersStats,
        PathValues.V2_API_KEY_ID: V2ApiKeyId,
        PathValues.V2_ENDUSER_FACING_FAVORITE_SERVICE_SERVICE_ID: V2EnduserFacingFavoriteServiceServiceId,
        PathValues.V2_INTEGRATION: V2Integration,
        PathValues.V2_SERVICE_TUNNEL: V2ServiceTunnel,
        PathValues.V1_ACCESS_ACTIVITY: V1AccessActivity,
        PathValues.V1_CA_CERTS: V1CaCerts,
        PathValues.V1_DELETE_PWLESS_CONFIG: V1DeletePwlessConfig,
        PathValues.HEALTH: Health,
        PathValues.V1_UPDATE_ORG: V1UpdateOrg,
        PathValues.V2_INTEGRATION_SYNC_STATS: V2IntegrationSyncStats,
        PathValues.V2_INTEGRATION_TEST_CREDENTIALS: V2IntegrationTestCredentials,
        PathValues.V2_SUPERADMIN_UPLOAD_PRODUCT_ANALYTICS_CSV: V2SuperadminUploadProductAnalyticsCsv,
        PathValues.V1_MDM_DEPLOY_CONFIG: V1MdmDeployConfig,
        PathValues.V1_BANYANIDP_ENDUSER_PROFILE: V1BanyanidpEnduserProfile,
        PathValues.V1_SECURITY_ROLES_ENDUSER_DEVICES: V1SecurityRolesEnduserDevices,
        PathValues.V1_MDM_INSERT_DEVICES: V1MdmInsertDevices,
        PathValues.V1_TRUSTSCORE_CONFIG_DEVICE_ORG_PREFERRED_APPS: V1TrustscoreConfigDeviceOrgPreferredApps,
        PathValues.V2_ENDUSER_GROUPS: V2EnduserGroups,
        PathValues.V2_INTEGRATION_DEVICE_IDENTITY_COMMAND: V2IntegrationDeviceIdentityCommand,
        PathValues.V2_REGISTERED_DOMAIN_ID: V2RegisteredDomainId,
        PathValues.V2_REGISTERED_DOMAIN: V2RegisteredDomain,
        PathValues.V1_ENDUSERS: V1Endusers,
        PathValues.V2_DEVICES: V2Devices,
        PathValues.V2_SATELLITE: V2Satellite,
        PathValues.V1_POLICY_ATTACHMENT_ATTACHED_TO_TYPE: V1PolicyAttachmentAttachedToType,
        PathValues.V1_ADMIN_LIST_USERS: V1AdminListUsers,
        PathValues.V2_CERT_UPDATE_PREPARE: V2CertUpdatePrepare,
        PathValues.V2_ENDUSER_FACING_AUTORUN_SERVICE: V2EnduserFacingAutorunService,
        PathValues.V1_ADMIN_LIST_ORGS: V1AdminListOrgs,
        PathValues.V1_MDM_OTDP: V1MdmOtdp,
        PathValues.V1_INSERT_DEFAULT_REGISTERED_SERVICES: V1InsertDefaultRegisteredServices,
        PathValues.V1_SERVICE_CONNECTION_TEST: V1ServiceConnectionTest,
        PathValues.V1_USER_ORG_DETAILS: V1UserOrgDetails,
        PathValues.V2_CLIENT_CERTIFICATE: V2ClientCertificate,
        PathValues.V1_ENDUSER_DEVICES_DATA: V1EnduserDevicesData,
        PathValues.V1_ENDUSER_DEVICES: V1EnduserDevices,
        PathValues.V1_EVENT_TYPES: V1EventTypes,
        PathValues.V1_SHIELD_CONFIG: V1ShieldConfig,
        PathValues.V2_API_KEY_SCOPE: V2ApiKeyScope,
        PathValues.V2_CLOUD_RESOURCE_SERVICE: V2CloudResourceService,
        PathValues.V2_ENDUSER_FACING_FAVORITE_SERVICE: V2EnduserFacingFavoriteService,
        PathValues.V1_TRUSTSCORE_CONFIG_DEVICE_TRUSTSCORE_FACTORS: V1TrustscoreConfigDeviceTrustscoreFactors,
        PathValues.V1_BANYANIDP_ADMIN_GROUP_USER: V1BanyanidpAdminGroupUser,
        PathValues.V1_ENDUSER_FACING_DEVICE_FEATURES: V1EnduserFacingDeviceFeatures,
        PathValues.V1_INVITE_CODE: V1InviteCode,
        PathValues.V1_INSERT_REGISTERED_SERVICE: V1InsertRegisteredService,
        PathValues.V1_SECURITY_EVENTS_TYPE_COUNT: V1SecurityEventsTypeCount,
        PathValues.V2_ACCESS_TIER: V2AccessTier,
        PathValues.V2_ACCESS_TIER_ID_REGISTERED_SERVICES: V2AccessTierIdRegisteredServices,
        PathValues.V2_CERT_UPDATE: V2CertUpdate,
        PathValues.V2_COMMAND_CENTER_SETTINGS: V2CommandCenterSettings,
        PathValues.V2_ENDUSER_FACING_AUTORUN_SERVICE_SERVICE_ID: V2EnduserFacingAutorunServiceServiceId,
        PathValues.V2_INTEGRATION_TEST_CREDENTIALS_CROWDSTRIKE: V2IntegrationTestCredentialsCrowdstrike,
        PathValues.SERVICE_TUNNEL_ID_SECURITY_POLICY_POLICY_ID: ServiceTunnelIdSecurityPolicyPolicyId,
        PathValues.V2_SHIELD_CONFIG: V2ShieldConfig,
        PathValues.V1_ENDUSER_FACING_ORG_DETAILS: V1EnduserFacingOrgDetails,
        PathValues.V1_DELETE_NETAGENT: V1DeleteNetagent,
        PathValues.V1_REGISTERED_SERVICES: V1RegisteredServices,
        PathValues.V1_DELETE_SECURITY_POLICY: V1DeleteSecurityPolicy,
        PathValues.V1_DELETE_SECURITY_ROLE: V1DeleteSecurityRole,
        PathValues.V2_CERT_REQUEST_DEVICE_ONLY_REGISTRATION: V2CertRequestDeviceOnlyRegistration,
        PathValues.V2_CLOUD_RESOURCE: V2CloudResource,
        PathValues.V2_ENDUSER_FACING_TUNNEL_CONFIG: V2EnduserFacingTunnelConfig,
        PathValues.V2_INTEGRATION_SENTINELONE: V2IntegrationSentinelone,
        PathValues.V2_SIGNUP_ORG_NAMES: V2SignupOrgNames,
        PathValues.V2_SATELLITE_FACING_CONFIG_SATELLITE_NAME: V2SatelliteFacingConfigSatelliteName,
        PathValues.SERVICE_TUNNEL_ID_SECURITY_POLICY: ServiceTunnelIdSecurityPolicy,
        PathValues.V1_TRUSTSCORE_CONFIG_DEVICE_TRUSTSCORE_TTL: V1TrustscoreConfigDeviceTrustscoreTtl,
        PathValues.V1_ENDUSER_FACING_APP_VERSION: V1EnduserFacingAppVersion,
        PathValues.V2_BUNDLE: V2Bundle,
        PathValues.V2_REGISTERED_DOMAIN_CHALLENGE: V2RegisteredDomainChallenge,
        PathValues.V1_BANYANIDP_ENDUSER_CONFIRMFORGOTPASSWORD: V1BanyanidpEnduserConfirmforgotpassword,
        PathValues.V1_MDM_DEVICE_INFO: V1MdmDeviceInfo,
        PathValues.V1_INSERT_SECURITY_ATTACH_POLICY: V1InsertSecurityAttachPolicy,
        PathValues.V2_ENDUSER: V2Enduser,
        PathValues.V2_ENDUSER_FACING_LOGIN_SERVICES: V2EnduserFacingLoginServices,
        PathValues.V2_REGISTERED_DOMAIN_ID_VALIDATE: V2RegisteredDomainIdValidate,
        PathValues.V2_TUNNEL_CIDR: V2TunnelCidr,
        PathValues.V1_BANYANIDP_ADMIN_USER_CHANGEPASSWORD: V1BanyanidpAdminUserChangepassword,
        PathValues.V1_ONE_TIME_SECURITY_KEY: V1OneTimeSecurityKey,
        PathValues.V1_DELETE_REGISTERED_SERVICE: V1DeleteRegisteredService,
        PathValues.V1_DISABLE_REGISTERED_SERVICE: V1DisableRegisteredService,
        PathValues.V1_UNREGISTERED_DEVICE_ENDUSERS: V1UnregisteredDeviceEndusers,
        PathValues.V2_INTEGRATION_SIGNAL: V2IntegrationSignal,
        PathValues.V2_SATELLITE_ID: V2SatelliteId,
        PathValues.V2_SATELLITE_FACING_SATELLITE_NAME_STATUS: V2SatelliteFacingSatelliteNameStatus,
        PathValues.V2_CONNECTOR_STATS: V2ConnectorStats,
        PathValues.V1_AUDIT_LOGS: V1AuditLogs,
        PathValues.V1_DEVICE_REFRESH_CERTS: V1DeviceRefreshCerts,
        PathValues.V1_NETAGENTS: V1Netagents,
        PathValues.V1_POLICY_ATTACHMENT: V1PolicyAttachment,
        PathValues.V1_SECURITY_ROLES: V1SecurityRoles,
        PathValues.V1_EVENTS_FEED: V1EventsFeed,
        PathValues.HEALTH_AUTHENTICATION: HealthAuthentication,
        PathValues.V1_MDM_RESEND_OTDP_MAIL: V1MdmResendOtdpMail,
        PathValues.INSERT_SAASAPP: InsertSaasapp,
        PathValues.V1_DELETE_SHIELD_CLUSTER: V1DeleteShieldCluster,
        PathValues.V1_DEVICE_ID_TOKEN: V1DeviceIdToken,
        PathValues.V2_DEPLOY_CONFIG_OTP_SKIP_ROLE: V2DeployConfigOtpSkipRole,
        PathValues.V2_ENDUSER_FACING_BUNDLE_BUNDLE_ID: V2EnduserFacingBundleBundleId,
        PathValues.V2_SERVICE_TUNNEL_ID: V2ServiceTunnelId,
        PathValues.V2_UPLOAD_ENDUSER_COUNTS_CSV: V2UploadEnduserCountsCsv,
        PathValues.V1_BANYANIDP_ENDUSER_SIGNIN: V1BanyanidpEnduserSignin,
        PathValues.V1_DELETE_SECURITY_ATTACH_POLICY: V1DeleteSecurityAttachPolicy,
        PathValues.V2_SIGNUP_RESEND_EMAIL: V2SignupResendEmail,
        PathValues.V2_SIGNUP_PROVISION_ORG_RETRY: V2SignupProvisionOrgRetry,
        PathValues.V2_STAGED_DEVICE_CERT_PASSWORD: V2StagedDeviceCertPassword,
        PathValues.V1_API_V1_ADMIN_SAML: V1ApiV1AdminSaml,
        PathValues.V1_DEVICE_UNREGISTER: V1DeviceUnregister,
        PathValues.V1_ADD_ORG: V1AddOrg,
        PathValues.V1_ORG_DETAILS: V1OrgDetails,
        PathValues.V2_COMMAND_CENTER_SETTINGS_ID: V2CommandCenterSettingsId,
        PathValues.V2_ONBOARDING_STATE: V2OnboardingState,
        PathValues.V2_SATELLITE_FACING_SATELLITE_NAME_IPTABLES: V2SatelliteFacingSatelliteNameIptables,
        PathValues.V1_BANYANIDP_ADMIN_USER: V1BanyanidpAdminUser,
        PathValues.V2_BUNDLE_BUNDLE_ID_SERVICE: V2BundleBundleIdService,
        PathValues.V2_BUNDLE_BUNDLE_ID_SERVICE_SERVICE_ID: V2BundleBundleIdServiceServiceId,
        PathValues.V1_BANYANIDP_ENDUSER_RESENDCONFIRMATIONCODE: V1BanyanidpEnduserResendconfirmationcode,
        PathValues.V1_ADMIN_DELETE_USER: V1AdminDeleteUser,
        PathValues.V1_TRUSTSCORE: V1Trustscore,
        PathValues.V1_ONE_CLICK_SUPPORT_BUNDLE: V1OneClickSupportBundle,
        PathValues.V1_ADMIN_UPDATE_USER: V1AdminUpdateUser,
        PathValues.V2_SERVICE_METADATA_SERVICE_ID: V2ServiceMetadataServiceId,
        PathValues.V2_SERVICE_METADATA_SERVICES: V2ServiceMetadataServices,
        PathValues.V2_ADMIN_CLIENT_CERTIFICATE: V2AdminClientCertificate,
        PathValues.V2_ENDUSER_ID: V2EnduserId,
        PathValues.V2_INTEGRATION_PARTNER: V2IntegrationPartner,
        PathValues.V1_API_V1_ADMIN_SETUP_SAML: V1ApiV1AdminSetupSaml,
        PathValues.V2_ENDUSER_FACING_BUNDLE_BUNDLE_ID_SERVICE: V2EnduserFacingBundleBundleIdService,
        PathValues.V2_ENDUSER_FACING_BUNDLE_BUNDLE_ID_SERVICE_SERVICE_ID: V2EnduserFacingBundleBundleIdServiceServiceId,
        PathValues.V2_ENDUSER_FACING_ORG_SUPPORT: V2EnduserFacingOrgSupport,
        PathValues.V1_BANYANIDP_ADMIN_GROUP: V1BanyanidpAdminGroup,
        PathValues.BANYANIDP_ADMIN_USER: BanyanidpAdminUser,
        PathValues.V1_BANYANIDP_ENDUSER_NEWPASSWORD: V1BanyanidpEnduserNewpassword,
        PathValues.V1_REFRESH_TOKEN: V1RefreshToken,
        PathValues.V1_SECURITY_EVENTS: V1SecurityEvents,
        PathValues.V1_INSERT_SECURITY_POLICY: V1InsertSecurityPolicy,
        PathValues.V2_ACCESS_TIER_ACCESS_TIER_ID_TUNNEL_CONFIG_TUNNEL_CONFIG_ID: V2AccessTierAccessTierIdTunnelConfigTunnelConfigId,
        PathValues.V2_SERVICE_BUNDLE_BUNDLEDSERVICEID: V2ServiceBundleBundledServiceId,
        PathValues.V1_ACTIVE_USERS: V1ActiveUsers,
        PathValues.V1_ADMIN_TRUSTSCORE_PROFILES: V1AdminTrustscoreProfiles,
        PathValues.V1_TRUSTSCORE_CONFIG_DEVICE_LATEST_OS: V1TrustscoreConfigDeviceLatestOs,
        PathValues.V1_BANYANIDP_ADMIN_USER_ENABLE: V1BanyanidpAdminUserEnable,
        PathValues.V1_BANYANIDP_ADMIN_USER_GROUP: V1BanyanidpAdminUserGroup,
        PathValues.V1_BANYANIDP_ADMIN_USER_PASSWORD: V1BanyanidpAdminUserPassword,
        PathValues.V1_DEVICE_REGISTER: V1DeviceRegister,
        PathValues.V1_DEVICES: V1Devices,
        PathValues.V1_DEVICES_STATS: V1DevicesStats,
        PathValues.V1_ENDUSERS_CSV: V1EndusersCsv,
        PathValues.V1_EVENTS_COUNT: V1EventsCount,
        PathValues.V1_HOSTS: V1Hosts,
        PathValues.V1_IMPERSONATE: V1Impersonate,
        PathValues.V1_API_V1_RESET_PASSWORD: V1ApiV1ResetPassword,
        PathValues.V1_SERVICE_HOSTNAME_MAPPING: V1ServiceHostnameMapping,
        PathValues.V1_MDM_UPDATE_DEVICE: V1MdmUpdateDevice,
        PathValues.V2_SUPERADMIN_VALIDATE_PRIVATE_KEY_RECORDS: V2SuperadminValidatePrivateKeyRecords,
        PathValues.V2_API_KEY: V2ApiKey,
        PathValues.V2_ACCESS_TIER_ACCESS_TIER_ID_CONFIG: V2AccessTierAccessTierIdConfig,
        PathValues.V2_ACCESS_TIER_ACCESS_TIER_ID_TEST: V2AccessTierAccessTierIdTest,
        PathValues.V2_ACCESS_TIER_FACING_ACCESS_TIER_NAME_CONFIG: V2AccessTierFacingAccessTierNameConfig,
        PathValues.V2_ACCESS_TIER_FACING_ACCESS_TIER_NAME_CERT_REQUEST: V2AccessTierFacingAccessTierNameCertRequest,
    }
)
