from openapi_client.paths.v2_auth_user_metadata.get import ApiForget
from openapi_client.paths.v2_auth_user_metadata.put import ApiForput
from openapi_client.paths.v2_auth_user_metadata.delete import ApiFordelete


class V2AuthUserMetadata(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
