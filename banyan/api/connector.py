from typing import Dict, List, Any, Union
from uuid import UUID

from banyan.api.base import ApiBase
from banyan.model.connector import Connector, ConnectorInfo

JsonListOrObj = Union[List, Dict]

class ConnectorAPI(ApiBase):
    class Meta:
        data_class = Connector
        info_class = ConnectorInfo

    def list(self, params: Dict[str, Any] = None) -> List[ConnectorInfo]:
        response_json = self._client.api_request('GET', 
                                                 '/v2/satellite',
                                                 params=params)
        data = ConnectorInfo.Schema().load(response_json["satellites"], many=True)
        return data

    def get(self, id: UUID):
        response_json = self._client.api_request('GET', 
                                                 '/v2/satellite/%s' % str(id))
        data = ConnectorInfo.Schema().load(response_json)
        return data

    def create(self, obj: Connector) -> JsonListOrObj:
        response_json = self._client.api_request('POST',
                                                 '/v2/satellite',
                                                 headers={'content-type': 'application/json'},
                                                 json=Connector.Schema().dump(obj))
        return response_json

    def update(self, id: UUID, obj: Connector) -> JsonListOrObj:
        response_json = self._client.api_request('PUT',
                                                 '/v2/satellite/%s' % str(id),
                                                 headers={'content-type': 'application/json'},
                                                 json=Connector.Schema().dump(obj))
        return response_json

    def delete(self, id: UUID) -> JsonListOrObj:
        response_json = self._client.api_request('DELETE', 
                                                 '/v2/satellite/%s' % str(id))
        return response_json


