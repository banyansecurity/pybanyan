from datetime import datetime
from typing import List

from banyan.api.base import ServiceBase, Resource
from banyan.model import BanyanApiObject
from banyan.model.event_v2 import EventV2, EventOrID


class EventV2API(ServiceBase):
    class Meta:
        data_class = EventV2
        info_class = EventV2
        arg_type = EventOrID
        list_uri = '/events'
        uri_param = 'EventID'
        obj_name = 'event'
        supports_paging = True

    def create(self, obj: BanyanApiObject) -> str:
        raise NotImplementedError('The Banyan API does not support this operation')

    def update(self, obj: BanyanApiObject) -> str:
        raise NotImplementedError('The Banyan API does not support this operation')

    def delete(self, obj: BanyanApiObject) -> str:
        raise NotImplementedError('The Banyan API does not support this operation')

    def list(self, before_dt: datetime = None, after_dt: datetime = None, order: str = None,
             event_type: str = None, subtype: str = None, action: str = None,
             email_address: str = None, device_id: str = None, device_serial: str = None,
             container_id: str = None, service_name: str = None, event_id: str = None) -> list:
        params = ServiceBase.args_to_html_params([
            (before_dt, 'before', lambda: int(before_dt.timestamp() * 1000)),
            (after_dt, 'after', lambda: int(after_dt.timestamp() * 1000)),
            (order, 'order', order),
            (event_type, 'type', event_type),
            (subtype, 'sub_type', subtype),
            (action, 'action', action),
            (email_address, 'user_email', email_address),
            (device_id, 'device_id', device_id),
            (device_serial, 'serialnumber', device_serial),
            (container_id, 'workload_container_id', container_id),
            (service_name, 'service_name', service_name),
            (event_id, 'id', event_id),
        ])
        response_json = self._client.paged_request('GET', self.Meta.list_uri, params=params)
        data: List[Resource] = self.Meta.info_class.Schema().load(response_json, many=True)
        self._build_cache(data)
        return data
