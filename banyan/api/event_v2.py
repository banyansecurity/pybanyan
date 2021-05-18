from datetime import datetime, timedelta
from typing import List, Dict, Any, Set
from uuid import UUID

from semver import deprecated

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

    def count(self, before_dt: datetime = None, after_dt: datetime = None, order: str = None,
              event_type: str = None, subtype: str = None, action: str = None,
              email_address: str = None, device_id: str = None, device_serial: str = None,
              container_id: str = None, service_name: str = None, event_id: str = None) -> int:
        params = self._make_params(before_dt, after_dt, order, event_type, subtype, action, email_address,
                                   device_id, device_serial, container_id, service_name, event_id)
        return self._count(params)

    def _count(self, params: Dict[str, Any]) -> int:
        response_json = self._client.api_request('GET', '/events/count', params=params)
        return response_json['data']

    @deprecated(replace='banyan.api.event_v2.list')
    def list2(self, before_dt: datetime = None, after_dt: datetime = None, order: str = None,
              event_type: str = None, subtype: str = None, action: str = None,
              email_address: str = None, device_id: str = None, device_serial: str = None,
              container_id: str = None, service_name: str = None, event_id: str = None) -> List[Resource]:
        params = self._make_params(before_dt, after_dt, order, event_type, subtype, action, email_address,
                                   device_id, device_serial, container_id, service_name, event_id)
        return self._list_paged(params)

    def list(self, before_dt: datetime = None, after_dt: datetime = None, order: str = None,
             event_type: str = None, subtype: str = None, action: str = None,
             email_address: str = None, device_id: str = None, device_serial: str = None,
             container_id: str = None, service_name: str = None, event_id: str = None, limit: int = None) -> list:
        params = self._make_params(before_dt, after_dt, order, event_type, subtype, action, email_address,
                                   device_id, device_serial, container_id, service_name, event_id, limit)
        if before_dt and after_dt:
            return self._list_daterange(params)
        elif before_dt:
            params['after'] = int((datetime.now() - timedelta(days=7)).timestamp() * 1000)
            return self._list_daterange(params)
        elif after_dt:
            params['before'] = int(datetime.now().timestamp() * 1000)
            return self._list_daterange(params)
        else:
            return self._list_paged(params)

    # noinspection PyProtectedMember
    def _list_daterange(self, params: Dict[str, Any]) -> List[Resource]:
        params['order'] = 'asc'
        all_data: List[EventV2] = list()
        event_ids: Set[UUID] = set()
        count = self._count(params)
        if count == 10001:
            count = -1
        schema = self.Meta.info_class.Schema()
        callback = self._client.progress_callback
        if callback:
            callback('GET', self.Meta.list_uri, 0, count, all_data)
        while params['after'] < params['before']:
            response_json = self._client.api_request('GET', self.Meta.list_uri, params=params)
            data: List[EventV2] = schema.load(response_json['data'], many=True)
            data = list(filter(lambda x: x.event_id not in event_ids, data))
            if len(data) == 0:
                break
            all_data.extend(data)
            event_ids.update([x.event_id for x in data])
            params['after'] = int(data[-1].created_at.timestamp() * 1000)
            if callback:
                callback('GET', self.Meta.list_uri, len(all_data), count, data)
        self._build_cache(all_data)
        return all_data

    def _list_paged(self, params: Dict[str, Any]) -> List[Resource]:
        response_json = self._client.paged_request('GET', self.Meta.list_uri, params=params)
        data: List[EventV2] = self.Meta.info_class.Schema().load(response_json, many=True)
        self._build_cache(data)
        return data

    @staticmethod
    def _make_params(before_dt: datetime = None, after_dt: datetime = None, order: str = None,
                     event_type: str = None, subtype: str = None, action: str = None,
                     email_address: str = None, device_id: str = None, device_serial: str = None,
                     container_id: str = None, service_name: str = None, event_id: str = None,
                     limit: int = None) -> Dict[str, Any]:
        return ServiceBase.args_to_html_params([
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
            (limit, 'limit', limit),
        ])
