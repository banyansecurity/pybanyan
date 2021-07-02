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
        api_v2 = True
        list_uri = '/cloud_resource'

    def list(self, params: Dict[str, Any] = None) -> list:
        response_json = self._client.api_request('GET', 
                                                 '/cloud_resource',
                                                 params=params)
        data: List[DiscoveredResourceInfo] = list()
        if response_json["data"] is not None:
            data = DiscoveredResourceInfo.Schema().load(response_json["data"], many=True)
        return data

    def get(self, id: UUID, params: Dict[str, Any] = None) -> DiscoveredResourceInfo:
        response_json = self._client.api_request('GET', 
                                                 '/cloud_resource/%s' % str(id),
                                                 params=params)
        data = DiscoveredResourceInfo.Schema().load(response_json["data"])
        return data

    def create(self, obj: DiscoveredResource) -> str:
        response_json = self._client.api_request('POST',
                                                 '/cloud_resource',
                                                 headers={'content-type': 'application/json'},
                                                 json=DiscoveredResource.Schema().dump(obj))
        return response_json["data"]

    def update(self, obj: DiscoveredResource) -> str:
        response_json = self._client.api_request('PUT',
                                                 '/cloud_resource',
                                                 headers={'content-type': 'application/json'},
                                                 json=DiscoveredResource.Schema().dump(obj))
        return response_json["data"]

    def update_status(self, id: UUID, status: str) -> str:
        obj = {
            "status": status
        }
        response_json = self._client.api_request('PATCH',
                                                 '/cloud_resource/%s' % str(id),
                                                 headers={'content-type': 'application/json'},
                                                 json=obj)
        return response_json["data"]

    def delete(self, id: UUID) -> str:
        response_json = self._client.api_request('DELETE', 
                                                 '/cloud_resource/%s' % str(id))
        return response_json["data"]
