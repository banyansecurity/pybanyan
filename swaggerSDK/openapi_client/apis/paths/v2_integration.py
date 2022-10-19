from openapi_client.paths.v2_integration.get import ApiForget
from openapi_client.paths.v2_integration.put import ApiForput
from openapi_client.paths.v2_integration.post import ApiForpost
from openapi_client.paths.v2_integration.delete import ApiFordelete


class V2Integration(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
