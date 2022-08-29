from typing import Dict, List, Any, Union
from uuid import UUID

from banyan.api.base import ApiBase
from banyan.model.access_tier import AccessTier, AccessTierInfo

JsonListOrObj = Union[List, Dict]

class AccessTierAPI(ApiBase):
    class Meta:
        data_class = AccessTier
        info_class = AccessTierInfo

    def list(self, params: Dict[str, Any] = None) -> List[AccessTierInfo]:
        response_json = self._client.api_request('GET', 
                                                 '/v2/access_tier',
                                                 params=params)
        data = AccessTierInfo.Schema().load(response_json["access_tiers"], many=True)
        return data

    def get(self, id: UUID):
        response_json = self._client.api_request('GET', 
                                                 '/v2/access_tier/%s' % str(id))
        data = AccessTierInfo.Schema().load(response_json)
        return data

    def create(self, obj: AccessTier) -> JsonListOrObj:
        response_json = self._client.api_request('POST',
                                                 '/v2/access_tier',
                                                 headers={'content-type': 'application/json'},
                                                 json=AccessTier.Schema().dump(obj))
        return response_json

    def update(self, id: UUID, obj: AccessTier) -> JsonListOrObj:
        response_json = self._client.api_request('PUT',
                                                 '/v2/access_tier/%s' % str(id),
                                                 headers={'content-type': 'application/json'},
                                                 json=AccessTier.Schema().dump(obj))
        return response_json

    def delete(self, id: UUID) -> JsonListOrObj:
        response_json = self._client.api_request('DELETE', 
                                                 '/v2/access_tier/%s' % str(id))
        return response_json

