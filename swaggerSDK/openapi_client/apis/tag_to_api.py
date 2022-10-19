import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.enduser_facing_api import EnduserFacingApi
from openapi_client.apis.tags.audit_log_api import AuditLogApi
from openapi_client.apis.tags.customerfacingnamespace_api import CUSTOMERFACINGNAMESPACEApi
from openapi_client.apis.tags.device_api import DeviceApi
from openapi_client.apis.tags.registered_service_api import RegisteredServiceApi
from openapi_client.apis.tags.security_policy_api import SecurityPolicyApi
from openapi_client.apis.tags.security_role_api import SecurityRoleApi
from openapi_client.apis.tags.enduser_api import EnduserApi
from openapi_client.apis.tags.event_api import EventApi
from openapi_client.apis.tags.netagent_api import NetagentApi
from openapi_client.apis.tags.security_event_api import SecurityEventApi
from openapi_client.apis.tags.bundle_api import BundleApi
from openapi_client.apis.tags.trustscore_integration_api import TrustscoreIntegrationApi
from openapi_client.apis.tags.service_bundle_api import ServiceBundleApi
from openapi_client.apis.tags.access_activity_api import AccessActivityApi
from openapi_client.apis.tags.access_tier_api import AccessTierApi
from openapi_client.apis.tags.access_tier_tunnel_api import AccessTierTunnelApi
from openapi_client.apis.tags.deprecated_api import DeprecatedApi
from openapi_client.apis.tags.api_key_api import ApiKeyApi
from openapi_client.apis.tags.app_deployment_api import AppDeploymentApi
from openapi_client.apis.tags.auth_user_metadata_api import AuthUserMetadataApi
from openapi_client.apis.tags.banyanidp_api import BanyanidpApi
from openapi_client.apis.tags.basic_report_api import BasicReportApi
from openapi_client.apis.tags.certificate_api import CertificateApi
from openapi_client.apis.tags.cloud_resource_api import CloudResourceApi
from openapi_client.apis.tags.cloud_resource_service_api import CloudResourceServiceApi
from openapi_client.apis.tags.command_center_setting_api import CommandCenterSettingApi
from openapi_client.apis.tags.superadmin_api import SuperadminApi
from openapi_client.apis.tags.externalcert_api import ExternalcertApi
from openapi_client.apis.tags.global_domain_directory_api import GlobalDomainDirectoryApi
from openapi_client.apis.tags.health_api import HealthApi
from openapi_client.apis.tags.invite_code_api import InviteCodeApi
from openapi_client.apis.tags.org_api import OrgApi
from openapi_client.apis.tags.saml_api import SamlApi
from openapi_client.apis.tags.product_analytics_api import ProductAnalyticsApi
from openapi_client.apis.tags.refresh_token_api import RefreshTokenApi
from openapi_client.apis.tags.registered_domain_api import RegisteredDomainApi
from openapi_client.apis.tags.service_connection_test_api import ServiceConnectionTestApi
from openapi_client.apis.tags.saasapp_api import SaasappApi
from openapi_client.apis.tags.satellite_api import SatelliteApi
from openapi_client.apis.tags.satellite_facing_api import SatelliteFacingApi
from openapi_client.apis.tags.service_tunnel_api import ServiceTunnelApi
from openapi_client.apis.tags.sentinelone_api import SentineloneApi
from openapi_client.apis.tags.service_account_api import ServiceAccountApi
from openapi_client.apis.tags.service_metadata_api import ServiceMetadataApi
from openapi_client.apis.tags.shield_api import ShieldApi
from openapi_client.apis.tags.signup_api import SignupApi
from openapi_client.apis.tags.trustscore_api import TrustscoreApi
from openapi_client.apis.tags.trustscore_exclusion_api import TrustscoreExclusionApi
from openapi_client.apis.tags.tunnel_cidr_api import TunnelCidrApi
from openapi_client.apis.tags.tunnel_resource_api import TunnelResourceApi
from openapi_client.apis.tags.unregistered_device_api import UnregisteredDeviceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ENDUSER_FACING: EnduserFacingApi,
        TagValues.AUDIT_LOG: AuditLogApi,
        TagValues.CUSTOMER_FACING_NAMESPACE: CUSTOMERFACINGNAMESPACEApi,
        TagValues.DEVICE: DeviceApi,
        TagValues.REGISTERED_SERVICE: RegisteredServiceApi,
        TagValues.SECURITY_POLICY: SecurityPolicyApi,
        TagValues.SECURITY_ROLE: SecurityRoleApi,
        TagValues.ENDUSER: EnduserApi,
        TagValues.EVENT: EventApi,
        TagValues.NETAGENT: NetagentApi,
        TagValues.SECURITY_EVENT: SecurityEventApi,
        TagValues.BUNDLE: BundleApi,
        TagValues.TRUSTSCORE_INTEGRATION: TrustscoreIntegrationApi,
        TagValues.SERVICE_BUNDLE: ServiceBundleApi,
        TagValues.ACCESS_ACTIVITY: AccessActivityApi,
        TagValues.ACCESS_TIER: AccessTierApi,
        TagValues.ACCESS_TIER_TUNNEL: AccessTierTunnelApi,
        TagValues.DEPRECATED: DeprecatedApi,
        TagValues.API_KEY: ApiKeyApi,
        TagValues.APP_DEPLOYMENT: AppDeploymentApi,
        TagValues.AUTH_USER_METADATA: AuthUserMetadataApi,
        TagValues.BANYANIDP: BanyanidpApi,
        TagValues.BASIC_REPORT: BasicReportApi,
        TagValues.CERTIFICATE: CertificateApi,
        TagValues.CLOUD_RESOURCE: CloudResourceApi,
        TagValues.CLOUD_RESOURCE_SERVICE: CloudResourceServiceApi,
        TagValues.COMMAND_CENTER_SETTING: CommandCenterSettingApi,
        TagValues.SUPERADMIN: SuperadminApi,
        TagValues.EXTERNALCERT: ExternalcertApi,
        TagValues.GLOBAL_DOMAIN_DIRECTORY: GlobalDomainDirectoryApi,
        TagValues.HEALTH: HealthApi,
        TagValues.INVITE_CODE: InviteCodeApi,
        TagValues.ORG: OrgApi,
        TagValues.SAML: SamlApi,
        TagValues.PRODUCT_ANALYTICS: ProductAnalyticsApi,
        TagValues.REFRESH_TOKEN: RefreshTokenApi,
        TagValues.REGISTERED_DOMAIN: RegisteredDomainApi,
        TagValues.SERVICE_CONNECTION_TEST: ServiceConnectionTestApi,
        TagValues.SAASAPP: SaasappApi,
        TagValues.SATELLITE: SatelliteApi,
        TagValues.SATELLITE_FACING: SatelliteFacingApi,
        TagValues.SERVICE_TUNNEL: ServiceTunnelApi,
        TagValues.SENTINELONE: SentineloneApi,
        TagValues.SERVICE_ACCOUNT: ServiceAccountApi,
        TagValues.SERVICE_METADATA: ServiceMetadataApi,
        TagValues.SHIELD: ShieldApi,
        TagValues.SIGNUP: SignupApi,
        TagValues.TRUSTSCORE: TrustscoreApi,
        TagValues.TRUSTSCORE_EXCLUSION: TrustscoreExclusionApi,
        TagValues.TUNNEL_CIDR: TunnelCidrApi,
        TagValues.TUNNEL_RESOURCE: TunnelResourceApi,
        TagValues.UNREGISTERED_DEVICE: UnregisteredDeviceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ENDUSER_FACING: EnduserFacingApi,
        TagValues.AUDIT_LOG: AuditLogApi,
        TagValues.CUSTOMER_FACING_NAMESPACE: CUSTOMERFACINGNAMESPACEApi,
        TagValues.DEVICE: DeviceApi,
        TagValues.REGISTERED_SERVICE: RegisteredServiceApi,
        TagValues.SECURITY_POLICY: SecurityPolicyApi,
        TagValues.SECURITY_ROLE: SecurityRoleApi,
        TagValues.ENDUSER: EnduserApi,
        TagValues.EVENT: EventApi,
        TagValues.NETAGENT: NetagentApi,
        TagValues.SECURITY_EVENT: SecurityEventApi,
        TagValues.BUNDLE: BundleApi,
        TagValues.TRUSTSCORE_INTEGRATION: TrustscoreIntegrationApi,
        TagValues.SERVICE_BUNDLE: ServiceBundleApi,
        TagValues.ACCESS_ACTIVITY: AccessActivityApi,
        TagValues.ACCESS_TIER: AccessTierApi,
        TagValues.ACCESS_TIER_TUNNEL: AccessTierTunnelApi,
        TagValues.DEPRECATED: DeprecatedApi,
        TagValues.API_KEY: ApiKeyApi,
        TagValues.APP_DEPLOYMENT: AppDeploymentApi,
        TagValues.AUTH_USER_METADATA: AuthUserMetadataApi,
        TagValues.BANYANIDP: BanyanidpApi,
        TagValues.BASIC_REPORT: BasicReportApi,
        TagValues.CERTIFICATE: CertificateApi,
        TagValues.CLOUD_RESOURCE: CloudResourceApi,
        TagValues.CLOUD_RESOURCE_SERVICE: CloudResourceServiceApi,
        TagValues.COMMAND_CENTER_SETTING: CommandCenterSettingApi,
        TagValues.SUPERADMIN: SuperadminApi,
        TagValues.EXTERNALCERT: ExternalcertApi,
        TagValues.GLOBAL_DOMAIN_DIRECTORY: GlobalDomainDirectoryApi,
        TagValues.HEALTH: HealthApi,
        TagValues.INVITE_CODE: InviteCodeApi,
        TagValues.ORG: OrgApi,
        TagValues.SAML: SamlApi,
        TagValues.PRODUCT_ANALYTICS: ProductAnalyticsApi,
        TagValues.REFRESH_TOKEN: RefreshTokenApi,
        TagValues.REGISTERED_DOMAIN: RegisteredDomainApi,
        TagValues.SERVICE_CONNECTION_TEST: ServiceConnectionTestApi,
        TagValues.SAASAPP: SaasappApi,
        TagValues.SATELLITE: SatelliteApi,
        TagValues.SATELLITE_FACING: SatelliteFacingApi,
        TagValues.SERVICE_TUNNEL: ServiceTunnelApi,
        TagValues.SENTINELONE: SentineloneApi,
        TagValues.SERVICE_ACCOUNT: ServiceAccountApi,
        TagValues.SERVICE_METADATA: ServiceMetadataApi,
        TagValues.SHIELD: ShieldApi,
        TagValues.SIGNUP: SignupApi,
        TagValues.TRUSTSCORE: TrustscoreApi,
        TagValues.TRUSTSCORE_EXCLUSION: TrustscoreExclusionApi,
        TagValues.TUNNEL_CIDR: TunnelCidrApi,
        TagValues.TUNNEL_RESOURCE: TunnelResourceApi,
        TagValues.UNREGISTERED_DEVICE: UnregisteredDeviceApi,
    }
)
