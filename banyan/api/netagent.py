from typing import List

from banyan.api.base import ServiceBase
from banyan.model import Resource
from banyan.model.netagent import Netagent


class NetagentAPI(ServiceBase):
    class Meta:
        data_class = Netagent
        info_class = Netagent
        arg_type = str
        list_uri = '/netagents'
        delete_uri = None
        insert_uri = None
        uri_param = None
        obj_name = 'netagent'

    def list(self) -> list:
        response_json = list(self._client.api_request('GET', self.Meta.list_uri))
        data: List[Resource] = self.Meta.info_class.Schema().load(response_json, many=True)
        self._build_cache(data)
        return data

    def active(self) -> List[Netagent]:
        agents: List[Netagent] = self.list()
        return [x for x in agents if x.status == 'REPORTING']
