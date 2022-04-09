from banyan.api.base import ApiBase
from banyan.model.api_key import ApiKey, ApiKeyInfo

class ApiKeyAPI(ApiBase):
    class Meta:
        data_class = ApiKey
        info_class = ApiKeyInfo
        list_uri = '/v2/api_key'
        