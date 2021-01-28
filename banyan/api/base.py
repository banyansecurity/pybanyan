from abc import ABC
from typing import Dict, List, Union, Iterable, Any, Callable

from banyan.core.exc import BanyanError
from banyan.model import InfoBase, BanyanApiObject, Resource, ResourceOrName

InfoObjectOrName = Union[InfoBase, str]


class ServiceBase(ABC):
    class Meta:
        data_class = BanyanApiObject
        info_class = Resource
        arg_type = ResourceOrName
        list_uri = '/undeclared'
        delete_uri = '/undeclared'
        insert_uri = '/undeclared'
        uri_param = 'ObjectID'
        obj_name = 'object'
        supports_paging = False

    def __init__(self, client):
        self._client = client
        self._cache: List[Resource] = list()
        self._by_name: Dict[str, Resource] = dict()
        self._by_id: Dict[str, Resource] = dict()

    def list(self) -> list:
        list_func = self._client.api_request
        try:
            if self.Meta.supports_paging:
                list_func = self._client.paged_request
        except AttributeError:
            pass
        response_json = list(list_func('GET', self.Meta.list_uri))
        data: List[Resource] = self.Meta.info_class.Schema().load(response_json, many=True)
        self._build_cache(data)
        return data

    def _build_cache(self, info: List[Resource]) -> None:
        self._cache = info
        self._by_name = {i.name.lower(): i for i in info}
        self._by_id = {str(i.id).lower(): i for i in info}

    def __getitem__(self, key: str):
        self._ensure_cache()
        try:
            return self._by_name[key.lower()]
        except KeyError:
            try:
                return self._by_id[key.lower()]
            except KeyError:
                raise BanyanError(f'{self.Meta.obj_name} name or ID does not exist: {key}')

    def exists(self, name: str) -> bool:
        self._ensure_cache()
        return name.lower() in self._by_name.keys() or name.lower() in self._by_id.keys()

    def _ensure_cache(self) -> None:
        if not self._cache:
            self.list()

    def _ensure_exists(self, name: str) -> None:
        if not self.exists(name):
            raise BanyanError(f'{self.Meta.obj_name} name does not exist: {name}')

    def _ensure_does_not_exist(self, name: str) -> None:
        if self.exists(name):
            raise BanyanError(f'{self.Meta.obj_name} name already exists: {name}')

    @staticmethod
    def args_to_html_params(args: Iterable) -> Dict[str, Any]:
        params = dict()
        for arg, key, val in args:
            if arg:
                params[key] = val() if isinstance(val, Callable) else val
        return params

    def find(self, obj: ResourceOrName):
        if isinstance(obj, Resource):
            self._ensure_exists(obj.name)
            return obj
        else:
            return self.__getitem__(obj)

    def create(self, obj: BanyanApiObject):
        if not self.Meta.insert_uri:
            raise BanyanError(f'{self.Meta.obj_name} API does not support creating objects')
        self._ensure_does_not_exist(obj.name)
        response_json = self._client.api_request('POST',
                                                 self.Meta.insert_uri,
                                                 json=obj.Schema().dump(obj))
        return self.Meta.info_class.Schema().load(response_json)

    def update(self, obj: BanyanApiObject):
        if not self.Meta.insert_uri:
            raise BanyanError(f'{self.Meta.obj_name} API does not support updating objects')
        self._ensure_exists(obj.name)
        response_json = self._client.api_request('POST',
                                                 self.Meta.insert_uri,
                                                 json=obj.Schema().dump(obj))
        return self.Meta.info_class.Schema().load(response_json)

    def delete(self, obj: ResourceOrName):
        if not self.Meta.delete_uri:
            raise BanyanError(f'{self.Meta.obj_name} API does not support deleting objects')
        obj = self.find(obj)
        json_response = self._client.api_request('DELETE',
                                                 self.Meta.delete_uri,
                                                 params={self.Meta.uri_param: str(obj.id)})
        return json_response['Message']
