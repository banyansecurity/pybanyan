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

    def get(self, id: UUID, params: Dict[str, Any] = None) -> ApiKeyInfo:
        response_json = self._client.api_request('GET', f'/v2/api_key/{str(id)}', params=params)
        data = ApiKeyInfo.Schema().load(response_json)
        return data

    def create(self, obj: ApiKey) -> JsonListOrObj:
        response_json = self._client.api_request('POST', '/v2/api_key',
                                                 headers={'content-type': 'application/json'},
                                                 json=ApiKey.Schema().dump(obj))
        return response_json

    def update(self, obj: ApiKey) -> JsonListOrObj:
        response_json = self._client.api_request('PUT', '/v2/api_key',
                                                 headers={'content-type': 'application/json'},
                                                 json=ApiKey.Schema().dump(obj))
        return response_json

    def delete(self, id: UUID) -> JsonListOrObj:
        response_json = self._client.api_request('DELETE', f'/v2/api_key/{str(id)}')
        return response_json