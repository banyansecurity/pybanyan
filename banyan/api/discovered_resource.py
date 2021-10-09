from typing import Dict, List, Any, Union
from uuid import UUID

import json

from banyan.api.base import ServiceBase
from banyan.model import BanyanApiObject
from banyan.model.discovered_resource import DiscoveredResource, DiscoveredResourceInfo, DiscoveredResourceAssociateInfo
from banyan.model.service import ServiceInfoOrName
from banyan.api.service import ServiceAPI

JsonListOrObj = Union[List, Dict]

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

    def create(self, obj: DiscoveredResource) -> JsonListOrObj:
        response_json = self._client.api_request('POST',
                                                 '/v2/cloud_resource',
                                                 headers={'content-type': 'application/json'},
                                                 json=DiscoveredResource.Schema().dump(obj))
        return response_json

    def update(self, obj: DiscoveredResource) -> JsonListOrObj:
        response_json = self._client.api_request('PUT',
                                                 '/v2/cloud_resource',
                                                 headers={'content-type': 'application/json'},
                                                 json=DiscoveredResource.Schema().dump(obj))
        return response_json

    def update_status(self, id: UUID, status: str) -> JsonListOrObj:
        obj = {
            "status": status
        }
        response_json = self._client.api_request('PATCH',
                                                 '/v2/cloud_resource/%s' % str(id),
                                                 headers={'content-type': 'application/json'},
                                                 json=obj)
        return response_json

    def delete(self, id: UUID) -> JsonListOrObj:
        response_json = self._client.api_request('DELETE', 
                                                 '/v2/cloud_resource/%s' % str(id))
        return response_json

    def associate(self, id: UUID, service: ServiceInfoOrName) -> JsonListOrObj:
        service = ServiceAPI(self._client).find(service)
        obj = {
            'cloud_resource_id': id,
            'service_id': service.id
        }
        json_response = self._client.api_request('POST',
                                                 '/v2/cloud_resource_service',
                                                 headers={'content-type': 'application/json'},
                                                 json=obj)
        return json_response
    
    def dissociate(self, publish_id: UUID) -> JsonListOrObj:
        response_json = self._client.api_request('DELETE', 
                                                 '/v2/cloud_resource_service/%s' % str(publish_id))
        return response_json

    def associations(self,  id: str = None) -> List[DiscoveredResourceAssociateInfo]:
        params = {}
        if id is not None:
            params = {
                'cloud_resource_id': id
            }
        response_json = self._client.paged_request('GET', 
                                                 '/v2/cloud_resource_service',
                                                 params=params)
        data = DiscoveredResourceAssociateInfo.Schema().load(response_json, many=True)
        return data        