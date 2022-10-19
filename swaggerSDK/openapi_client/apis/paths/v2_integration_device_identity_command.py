from openapi_client.paths.v2_integration_device_identity_command.get import ApiForget
from openapi_client.paths.v2_integration_device_identity_command.put import ApiForput
from openapi_client.paths.v2_integration_device_identity_command.post import ApiForpost
from openapi_client.paths.v2_integration_device_identity_command.delete import ApiFordelete


class V2IntegrationDeviceIdentityCommand(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
