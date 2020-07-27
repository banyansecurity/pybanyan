from banyan.model.service import ServiceInfo, Service
from typing import Dict, List, Optional, Union
from banyan.core.exc import BanyanError


class ServiceAPI:
    def __init__(self, client):
        self._client = client
        self._cache: Optional[Dict[str, ServiceInfo]] = None

    def list(self) -> List[ServiceInfo]:
        response_json = self._client.api_request('GET', '/registered_services')
        data = [ServiceInfo.Schema().load(obj) for obj in response_json]
        self._build_cache(data)
        return data

    def _build_cache(self, info: List[ServiceInfo]) -> None:
        self._cache = {i.name: i for i in info}

    def __getitem__(self, key: str) -> ServiceInfo:
        self._ensure_cache()
        try:
            return self._cache[key]
        except KeyError:
            raise BanyanError(f'service name does not exist: {key}')

    def exists(self, service_name: str) -> bool:
        self._ensure_cache()
        return service_name in self._cache.keys()

    def _ensure_cache(self) -> None:
        if not self._cache:
            self.list()

    def _ensure_exists(self, service_name: str) -> None:
        if not self.exists(service_name):
            raise BanyanError(f'service name does not exist: {service_name}')

    def _ensure_does_not_exist(self, service_name: str) -> None:
        if self.exists(service_name):
            raise BanyanError(f'service name already exists: {service_name}')

    def insert(self, service: Service) -> ServiceInfo:
        self._ensure_does_not_exist(service.name)
        sj = service.as_json()
        response_json = self._client.api_request('POST', '/insert_registered_service', json=service.as_json())
        return ServiceInfo.from_json(response_json)

    def update(self, service: Service) -> ServiceInfo:
        self._ensure_exists(service.name)
        response_json = self._client.api_request('POST', '/insert_registered_service', json=service.as_json())
        return ServiceInfo.from_json(response_json)

    def _service_info_or_name(self, service: Union[ServiceInfo, str]) -> ServiceInfo:
        if isinstance(service, ServiceInfo):
            self._ensure_exists(service.name)
            return service
        else:
            return self[service]

    def delete(self, service: Union[ServiceInfo, str]) -> str:
        service = self._service_info_or_name(service)
        json_response = self._client.api_request('DELETE', '/delete_registered_service',
                                                 params={'ServiceID': service.service_id})
        return json_response['Message']

    def enable(self, service: Union[ServiceInfo, str]) -> str:
        service = self._service_info_or_name(service)
        json_response = self._client.api_request('POST', '/enable_registered_service',
                                                 params={'ServiceID': service.service_id})
        return json_response['Message']

    def disable(self, service: Union[ServiceInfo, str]) -> str:
        service = self._service_info_or_name(service)
        json_response = self._client.api_request('POST', '/disable_registered_service',
                                                 params={'ServiceID': service.service_id})
        return json_response['Message']

