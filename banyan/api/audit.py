from datetime import datetime
from typing import List

from banyan.api.base import ServiceBase, Resource
from banyan.model import BanyanApiObject
from banyan.model.audit import AuditEvent


class AuditAPI(ServiceBase):
    class Meta:
        data_class = AuditEvent
        info_class = AuditEvent
        arg_type = str
        list_uri = '/audit_logs'
        uri_param = ''
        obj_name = 'audit log'
        supports_paging = True

    def create(self, obj: BanyanApiObject) -> str:
        raise NotImplementedError('The Banyan API does not support this operation')

    def update(self, obj: BanyanApiObject) -> str:
        raise NotImplementedError('The Banyan API does not support this operation')

    def delete(self, obj: BanyanApiObject) -> str:
        raise NotImplementedError('The Banyan API does not support this operation')

    def list(self, before_dt: datetime = None, after_dt: datetime = None,
             event_type: str = None, action: str = None, admin_email: str = None) -> list:
        params = ServiceBase.args_to_html_params([
            (before_dt, 'end_time', int(before_dt.timestamp() * 1000000000) if before_dt else None),
            (after_dt, 'start_time', int(after_dt.timestamp() * 1000000000) if after_dt else None),
            (event_type, 'type', event_type),
            (action, 'action', action),
            (admin_email, 'admin_email', admin_email),
        ])
        response_json = self._client.api_request('GET', self.Meta.list_uri, params=params)
        data: List[Resource] = self.Meta.info_class.Schema().load(response_json, many=True)
        self._build_cache(data)
        return data
