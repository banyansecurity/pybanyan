from banyan.api.base import ApiBase
from banyan.api.service import ApiBase
from banyan.model.policy import PolicyInfo, PolicyInfoOrName, PolicyAttachInfo
from banyan.model.service import ServiceInfo, Service, ServiceInfoOrName

import json

import openapi_client

class ServiceAPI(ApiBase):
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
        query_params = {
        'ServiceID': service.id,
        }
        try:
            api_instance = self._client.get_openapi_instance('v1')
            response = api_instance.v1_enable_registered_service_post(query_params=query_params,skip_deserialization=True).response
        except openapi_client.ApiException as e:
            print("Exception when calling CUSTOMERFACINGNAMESPACEApi->v1_enable_registered_service_post: %s\n" % e)    
        except AttributeError:
            pass     
        json_response = json.loads(response.data)
        return json_response['Message']

    def disable(self, service: ServiceInfoOrName) -> str:        
        service = self.find(service)
        query_params = {
        'ServiceID': service.id,
        }
        try:
            api_instance = self._client.get_openapi_instance('v1')
            response = api_instance.v1_disable_registered_service_post(query_params=query_params,skip_deserialization=True).response
        except openapi_client.ApiException as e:
            print("Exception when calling CUSTOMERFACINGNAMESPACEApi->v1_disable_registered_service_post: %s\n" % e)    
        except AttributeError:
            pass     
        json_response = json.loads(response.data)
        return json_response['Message']

    def attach(self, service: ServiceInfoOrName, policy: PolicyInfoOrName, enforcing: bool) -> PolicyAttachInfo:
        from banyan.api.policy import PolicyAPI
        return PolicyAPI(self._client).attach(policy, service, enforcing)

    def detach(self, service: ServiceInfoOrName, policy: PolicyInfoOrName) -> str:
        from banyan.api.policy import PolicyAPI
        return PolicyAPI(self._client).detach(policy, service)

    def test(self, service: ServiceInfoOrName) -> None:
        pass

    def attached_policy(self, service: ServiceInfoOrName) -> PolicyInfo:
        from banyan.model.policy import PolicyAttachInfo
        service = self.find(service)
        json_response = self._client.api_request('GET', f'/policy/attachment/service/{service.id}')
        return PolicyAttachInfo.Schema().load(json_response[0]) if len(json_response) > 0 else None
