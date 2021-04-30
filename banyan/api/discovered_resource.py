from typing import Dict, List, Any

from banyan.api.base import ServiceBase
from banyan.model import BanyanApiObject
from banyan.model.discovered_resource import DiscoveredResource, DiscoveredResourceInfo


class DiscoveredResourceAPI(ServiceBase):
    class Meta:
        data_class = DiscoveredResource
        info_class = DiscoveredResourceInfo
        api_v2 = True
        list_uri = '/cloud_resource/inventory'

    def list(self, params: Dict[str, Any] = None) -> list:
        response_json = self._client.api_request('GET', 
                                                 '/cloud_resource/inventory',
                                                 params=params)
        data: List[DiscoveredResourceInfo] = list()
        if response_json["data"] is not None:
            data = DiscoveredResourceInfo.Schema().load(response_json["data"], many=True)
        return data

    def create(self, obj: DiscoveredResource) -> str:
        response_json = self._client.api_request('POST',
                                                 '/cloud_resource/inventory',
                                                 headers={'content-type': 'application/json'},
                                                 json=DiscoveredResource.Schema().dump(obj))
        return response_json["data"]

    def update(self, obj: BanyanApiObject) -> str:
        raise NotImplementedError('The Banyan API does not support this operation')

    def delete(self, obj: BanyanApiObject) -> str:
        raise NotImplementedError('The Banyan API does not support this operation')
