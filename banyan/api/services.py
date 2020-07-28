from typing import Dict, List

from banyan.core.exc import BanyanError
from banyan.model.policy import PolicyInfoOrName, PolicyAttachInfo
from banyan.model.service import ServiceInfo, Service, ServiceInfoOrName


class ServiceAPI:
    def __init__(self, client):
        self._client = client
        self._cache: List[ServiceInfo] = list()
        self._by_name: Dict[str, ServiceInfo] = dict()
        self._by_id: Dict[str, ServiceInfo] = dict()

    def list(self) -> List[ServiceInfo]:
        response_json = self._client.api_request('GET', '/registered_services')
        data: List[ServiceInfo] = ServiceInfo.Schema().load(response_json, many=True)
        self._build_cache(data)
        return data

    def _build_cache(self, info: List[ServiceInfo]) -> None:
        self._cache = info
        self._by_name = {i.name: i for i in info}
        self._by_id = {i.id: i for i in info}

    def __getitem__(self, key: str) -> ServiceInfo:
        self._ensure_cache()
        try:
            return self._by_name[key]
        except KeyError:
            try:
                return self._by_id[key]
            except KeyError:
                raise BanyanError(f'service name does not exist: {key}')

    def exists(self, service_name: str) -> bool:
        self._ensure_cache()
        return service_name in self._by_name.keys() or service_name in self._by_id.keys()

    def _ensure_cache(self) -> None:
        if not self._cache:
            self.list()

    def _ensure_exists(self, service_name: str) -> None:
        if not self.exists(service_name):
            raise BanyanError(f'service name does not exist: {service_name}')

    def _ensure_does_not_exist(self, service_name: str) -> None:
        if self.exists(service_name):
            raise BanyanError(f'service name already exists: {service_name}')

    def find(self, service: ServiceInfoOrName) -> ServiceInfo:
        if isinstance(service, ServiceInfo):
            self._ensure_exists(service.name)
            return service
        else:
            return self.__getitem__(service)

    def create(self, service: Service) -> ServiceInfo:
        self._ensure_does_not_exist(service.name)
        js = service.Schema().dump(service)
        response_json = self._client.api_request('POST',
                                                 '/insert_registered_service',
                                                 json=service.Schema().dump(service))
        return ServiceInfo.Schema().load(response_json)

    def update(self, service: Service) -> ServiceInfo:
        self._ensure_exists(service.name)
        response_json = self._client.api_request('POST',
                                                 '/insert_registered_service',
                                                 json=service.Schema.dump(service))
        return ServiceInfo.Schema().load(response_json)

    def delete(self, service: ServiceInfoOrName) -> str:
        service = self.find(service)
        json_response = self._client.api_request('DELETE',
                                                 '/delete_registered_service',
                                                 params={'ServiceID': service.id})
        return json_response['Message']

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
        from banyan.api.policies import PolicyAPI
        return PolicyAPI(self._client).attach(policy, service, enforcing)

    def detach(self, service: ServiceInfoOrName, policy: PolicyInfoOrName) -> PolicyAttachInfo:
        from banyan.api.policies import PolicyAPI
        return PolicyAPI(self._client).detach(policy, service)
