from typing import Dict, List

from banyan.core.exc import BanyanError
from banyan.model.policy import PolicyInfo, Policy, PolicyInfoOrName, PolicyAttachInfo
from banyan.model.service import ServiceInfoOrName


class PolicyAPI:
    def __init__(self, client):
        self._client = client
        self._cache: List[PolicyInfo] = list()
        self._by_name: Dict[str, PolicyInfo] = dict()
        self._by_id: Dict[str, PolicyInfo] = dict()

    def list(self) -> List[PolicyInfo]:
        response_json = self._client.api_request('GET', '/security_policies')
        data: List[PolicyInfo] = PolicyInfo.Schema().load(response_json, many=True)
        self._build_cache(data)
        return data

    def _build_cache(self, info: List[PolicyInfo]) -> None:
        self._cache = info
        self._by_name = {i.name: i for i in info}
        self._by_id = {i.id: i for i in info}

    def __getitem__(self, key: str) -> PolicyInfo:
        self._ensure_cache()
        try:
            return self._by_name[key]
        except KeyError:
            try:
                return self._by_id[key]
            except KeyError:
                raise BanyanError(f'policy name does not exist: {key}')

    def exists(self, policy_name: str) -> bool:
        self._ensure_cache()
        return policy_name in self._by_name.keys() or policy_name in self._by_id.keys()

    def _ensure_cache(self) -> None:
        if not self._cache:
            self.list()

    def _ensure_exists(self, policy_name: str) -> None:
        if not self.exists(policy_name):
            raise BanyanError(f'policy name does not exist: {policy_name}')

    def _ensure_does_not_exist(self, policy_name: str) -> None:
        if self.exists(policy_name):
            raise BanyanError(f'policy name already exists: {policy_name}')

    def find(self, policy: PolicyInfoOrName) -> PolicyInfo:
        if isinstance(policy, PolicyInfo):
            self._ensure_exists(policy.name)
            return policy
        else:
            return self.__getitem__(policy)

    def create(self, policy: Policy) -> PolicyInfo:
        self._ensure_does_not_exist(policy.name)
        response_json = self._client.api_request('POST',
                                                 '/insert_security_policy',
                                                 json=policy.Schema().dump(policy))
        return PolicyInfo.Schema().load(response_json)

    def update(self, policy: Policy) -> PolicyInfo:
        self._ensure_exists(policy.name)
        response_json = self._client.api_request('POST',
                                                 '/insert_security_policy',
                                                 json=policy.Schema.dump(policy))
        return PolicyInfo.Schema().load(response_json)

    def delete(self, policy: PolicyInfo) -> str:
        policy = self.find(policy)
        json_response = self._client.api_request('DELETE',
                                                 '/delete_security_policy',
                                                 params={'PolicyID': policy.id})
        return json_response['Message']

    def attach(self, policy: PolicyInfoOrName, service: ServiceInfoOrName, enforcing: bool) -> PolicyAttachInfo:
        from banyan.api.services import ServiceAPI
        policy = self.find(policy)
        service = ServiceAPI(self._client).find(service)
        json_response = self._client.api_request('POST', '/insert_security_attach_policy',
                                                 params={
                                                     'PolicyID': policy.id,
                                                     'ServiceID': service.id,
                                                     'Enabled': str(enforcing).upper()
                                                 })
        return PolicyAttachInfo.Schema().load(json_response)

    def detach(self, policy: PolicyInfoOrName, service: ServiceInfoOrName) -> PolicyAttachInfo:
        from banyan.api.services import ServiceAPI
        policy = self.find(policy)
        service = ServiceAPI(self._client).find(service)
        json_response = self._client.api_request('DELETE', '/delete_security_attach_policy',
                                                 params={
                                                     'PolicyID': policy.id,
                                                     'ServiceID': service.id
                                                 })
        return PolicyAttachInfo.Schema().load(json_response)
