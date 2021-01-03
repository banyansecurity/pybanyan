from banyan.api.base import ServiceBase
from banyan.model.policy import PolicyInfoOrName, PolicyAttachInfo
from banyan.model.service import ServiceInfo, Service, ServiceInfoOrName


class ServiceAPI(ServiceBase):
    class Meta:
        data_class = Service
        info_class = ServiceInfo
        arg_type = ServiceInfoOrName
        list_uri = '/registered_services'
        delete_uri = '/delete_registered_service'
        insert_uri = '/insert_registered_service'
        uri_param = 'ServiceID'
        obj_name = 'service'

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

    def test(self, service: ServiceInfoOrName) -> None:
        pass
