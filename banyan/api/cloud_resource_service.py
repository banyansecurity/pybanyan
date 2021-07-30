from typing import Dict, List, Any
from uuid import UUID
from banyan.api.base import ServiceBase
from banyan.model.cloud_resource_service import CloudResourceService, CloudResourceServiceDetails
from banyan.model.service import ServiceInfoOrName


class CloudResourceServiceAPI(ServiceBase):
    class Meta:
        data_class = CloudResourceService
        info_class = CloudResourceServiceDetails
        list_uri = '/cloud_resource_service'
        uri_param = 'id'
        obj_name = 'cloudresourceservice'

    def list(self, params: Dict[str, Any] = None) -> list:
        response_json = self._client.api_request('GET',
                                                 '/cloud_resource_service',
                                                 params=params)
        data: List[CloudResourceServiceDetails] = list()
        if response_json["data"] is not None:
            data = CloudResourceServiceDetails.Schema().load(response_json["data"]["result"], many=True)
        return data

    def get(self, id: UUID) -> CloudResourceServiceDetails:
        response_json = self._client.api_request('GET',
                                                 '/cloud_resource_service/%s' % str(id))
        data = CloudResourceServiceDetails.Schema().load(response_json["data"])
        return data

    def create(self, obj: CloudResourceService) -> str:
        response_json = self._client.api_request('POST',
                                                 '/cloud_resource_service',
                                                 headers={'content-type': 'application/json'},
                                                 json=CloudResourceService.Schema().dump(obj))
        return response_json["data"]

    def delete(self, id: UUID) -> str:
        response_json = self._client.api_request('DELETE',
                                                 '/cloud_resource_service/%s' % str(id))
        return response_json["data"]
