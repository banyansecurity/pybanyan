from banyan.api.base import ApiBase
from banyan.model.connector import Connector, ConnectorInfo

class ConnectorAPI(ApiBase):
    class Meta:
        data_class = Connector
        info_class = ConnectorInfo
        supports_paging = True
        list_uri = '/v2/satellite'
