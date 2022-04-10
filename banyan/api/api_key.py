from typing import Dict, List, Any, Union
from uuid import UUID
from banyan.api.base import ApiBase
from banyan.model.api_key import ApiKey, ApiKeyInfo

JsonListOrObj = Union[List, Dict]

class ApiKeyAPI(ApiBase):
    class Meta:
        data_class = ApiKey
        info_class = ApiKeyInfo
        list_uri = '/v2/api_key'
        obj_name = 'api_key'
