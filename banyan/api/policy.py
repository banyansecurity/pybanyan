from banyan.api.base import ServiceBase
from banyan.model.policy import PolicyInfo, Policy, PolicyInfoOrName, PolicyAttachInfo
from banyan.model.service import ServiceInfoOrName


class PolicyAPI(ServiceBase):
    class Meta:
        data_class = Policy
        info_class = PolicyInfo
        arg_type = PolicyInfoOrName
        list_uri = '/security_policies'
        delete_uri = '/delete_security_policy'
        insert_uri = '/insert_security_policy'
        uri_param = 'PolicyID'
        obj_name = 'policy'

    def attach(self, policy: PolicyInfoOrName, service: ServiceInfoOrName, enforcing: bool) -> PolicyAttachInfo:
        from banyan.api.service import ServiceAPI
        policy = self.find(policy)
        service = ServiceAPI(self._client).find(service)
        json_response = self._client.api_request('POST', '/insert_security_attach_policy',
                                                 params={
                                                     'PolicyID': policy.id,
                                                     'ServiceID': service.id,
                                                     'Enabled': str(enforcing).upper()
                                                 })
        return PolicyAttachInfo.Schema().load(json_response)

    def detach(self, policy: PolicyInfoOrName, service: ServiceInfoOrName) -> str:
        from banyan.api.service import ServiceAPI
        policy = self.find(policy)
        service = ServiceAPI(self._client).find(service)
        json_response = self._client.api_request('DELETE', '/delete_security_attach_policy',
                                                 params={
                                                     'PolicyID': policy.id,
                                                     'ServiceID': service.id
                                                 })
        return json_response['Message']
