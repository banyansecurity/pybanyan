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

    def list(self, params: Dict[str, Any] = None) -> list:
        list_func = self._client.api_request
        try:
            if self.Meta.supports_paging:
                list_func = self._client.paged_request
        except AttributeError:
            pass
        response_json = list(list_func('GET', self.Meta.list_uri, params=params))
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

    def create(self, obj: Resource) -> Resource:
        if not self.Meta.insert_uri:
            raise BanyanError(f'{self.Meta.obj_name} API does not support creating objects')
        self._ensure_does_not_exist(obj.name)
        response_json = self._client.api_request('POST',
                                                 self.Meta.insert_uri,
                                                 json=obj.Schema().dump(obj))
        new_obj = self.Meta.info_class.Schema().load(response_json)

        if self._cache:
            self._cache.append(new_obj)
            self._by_name[new_obj.name.lower()] = new_obj
            self._by_id[str(new_obj.id).lower()] = new_obj

        return new_obj

    def update(self, obj: Resource) -> Resource:
        if not self.Meta.insert_uri:
            raise BanyanError(f'{self.Meta.obj_name} API does not support updating objects')
        self._ensure_exists(obj.name)
        response_json = self._client.api_request('POST',
                                                 self.Meta.insert_uri,
                                                 json=obj.Schema().dump(obj))
        updated_obj = self.Meta.info_class.Schema().load(response_json)

        if self._cache:
            old_obj = self._by_id[str(obj.id).lower()]
            self._cache.remove(old_obj)
            self._cache.append(updated_obj)
            self._by_name[updated_obj.name.lower()] = updated_obj
            self._by_id[str(updated_obj.id).lower()] = updated_obj

        return updated_obj

    def delete(self, obj: ResourceOrName) -> str:
        if not self.Meta.delete_uri:
            raise BanyanError(f'{self.Meta.obj_name} API does not support deleting objects')
        obj = self.find(obj)
        assert isinstance(obj, Resource)
        json_response = self._client.api_request('DELETE',
                                                 self.Meta.delete_uri,
                                                 params={self.Meta.uri_param: str(obj.id)})
        if self._cache:
            self._cache.remove(obj)
            del self._by_name[obj.name.lower()]
            del self._by_id[str(obj.id).lower()]

        return json_response['Message']
