from typing import Dict, List, Any
from uuid import UUID

import json

from banyan.api.base import ServiceBase
from banyan.model import BanyanApiObject
from banyan.model.discovered_resource import DiscoveredResource, DiscoveredResourceInfo


class DiscoveredResourceAPI(ServiceBase):
    class Meta:
        data_class = DiscoveredResource
        info_class = DiscoveredResourceInfo
        supports_paging = True
        list_uri = '/v2/cloud_resource'

    def get(self, id: UUID, params: Dict[str, Any] = None) -> DiscoveredResourceInfo:
        response_json = self._client.api_request('GET', 
                                                 '/v2/cloud_resource/%s' % str(id),
                                                 params=params)
        data = DiscoveredResourceInfo.Schema().load(response_json)
        return data

    def create(self, obj: DiscoveredResource) -> str:
        response_json = self._client.api_request('POST',
                                                 '/v2/cloud_resource',
                                                 headers={'content-type': 'application/json'},
                                                 json=DiscoveredResource.Schema().dump(obj))
        return response_json

    def update(self, obj: DiscoveredResource) -> str:
        response_json = self._client.api_request('PUT',
                                                 '/v2/cloud_resource',
                                                 headers={'content-type': 'application/json'},
                                                 json=DiscoveredResource.Schema().dump(obj))
        return response_json

    def update_status(self, id: UUID, status: str) -> str:
        obj = {
            "status": status
        }
        response_json = self._client.api_request('PATCH',
                                                 '/v2/cloud_resource/%s' % str(id),
                                                 headers={'content-type': 'application/json'},
                                                 json=obj)
        return response_json

    def delete(self, id: UUID) -> str:
        response_json = self._client.api_request('DELETE', 
                                                 '/v2/cloud_resource/%s' % str(id))
        return response_json
