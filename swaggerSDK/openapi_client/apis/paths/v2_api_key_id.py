from openapi_client.paths.v2_api_key_id.get import ApiForget
from openapi_client.paths.v2_api_key_id.put import ApiForput
from openapi_client.paths.v2_api_key_id.delete import ApiFordelete


class V2ApiKeyId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
