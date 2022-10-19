from openapi_client.paths.v2_integration_signal.get import ApiForget
from openapi_client.paths.v2_integration_signal.put import ApiForput
from openapi_client.paths.v2_integration_signal.post import ApiForpost
from openapi_client.paths.v2_integration_signal.delete import ApiFordelete


class V2IntegrationSignal(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
