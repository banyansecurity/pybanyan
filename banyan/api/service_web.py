from typing import Dict, List, Union, Iterable, Any, Callable

from banyan.api.base import ApiBase
from banyan.model.policy import PolicyInfo, PolicyInfoOrName, PolicyAttachInfo
from banyan.model.service import ServiceInfo, Service, ServiceInfoOrName

class ServiceWebAPI(ApiBase):
    class Meta:
        data_class = Service
        info_class = ServiceInfo
        arg_type = ServiceInfoOrName
        list_uri = '/registered_services'
        delete_uri = '/delete_registered_service'
        insert_uri = '/insert_registered_service'
        uri_param = 'ServiceID'
        obj_name = 'service'

    def list(self, params: Dict[str, Any] = None) -> list:
        list_func = self._client.api_request
        response_json = list(list_func('GET', self.Meta.list_uri, params=params))
        data: List[ServiceInfo] = self.Meta.info_class.Schema().load(response_json, many=True)        
        filtered_data = []
        for svc in data:
            if svc.oidc_enabled:
                filtered_data.append(svc)
        self._build_cache(filtered_data)
        return filtered_data

    def enable(self, service: ServiceInfoOrName) -> str:
        service = self.find(service)
        json_response = self._client.api_request('POST',
                                                 '/enable_registered_service',
                                                 params={'ServiceID': service.id})
        return json_response['Message']

    def disable(self, service: ServiceInfoOrName) -> str:
        service = self.find(service)
        json_response = self._client.api_request('POST',
                                                 '/disable_registered_service',
                                                 params={'ServiceID': service.id})
        return json_response['Message']

    def attach(self, service: ServiceInfoOrName, policy: PolicyInfoOrName, enforcing: bool) -> PolicyAttachInfo:
        from banyan.api.policy import PolicyAPI
        return PolicyAPI(self._client).attach(policy, service, enforcing)

    def detach(self, service: ServiceInfoOrName, policy: PolicyInfoOrName) -> str:
        from banyan.api.policy import PolicyAPI
        return PolicyAPI(self._client).detach(policy, service)

    def attached_policy(self, service: ServiceInfoOrName) -> PolicyInfo:
        from banyan.model.policy import PolicyAttachInfo
        service = self.find(service)
        json_response = self._client.api_request('GET', f'/policy/attachment/service/{service.id}')
        return PolicyAttachInfo.Schema().load(json_response[0]) if len(json_response) > 0 else None
