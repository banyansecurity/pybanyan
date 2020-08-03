from banyan.api.base import ServiceBase
from banyan.model import BanyanApiObject
from banyan.model.role import Role, RoleInfo, RoleInfoOrName


class RoleAPI(ServiceBase):
    class Meta:
        data_class = Role
        info_class = RoleInfo
        arg_type = RoleInfoOrName
        list_uri = '/security_roles'
        delete_uri = '/delete_security_role'
        insert_uri = '/insert_security_role'
        uri_param = 'RoleID'
        obj_name = 'role'

    def enable(self, role: RoleInfoOrName) -> str:
        role = self.find(role)
        json_response = self._client.api_request('POST',
                                                 '/enable_security_role',
                                                 params={'RoleID': str(role.id)})
        return json_response['Message']

    def disable(self, role: RoleInfoOrName) -> str:
        role = self.find(role)
        json_response = self._client.api_request('POST',
                                                 '/disable_security_role',
                                                 params={'RoleID': str(role.id)})
        return json_response['Message']

    def create(self, obj: BanyanApiObject) -> str:
        self._ensure_does_not_exist(obj.name)
        response_json = self._client.api_request('POST',
                                                 self.Meta.insert_uri,
                                                 json=obj.Schema().dump(obj))
        return response_json['RoleID']
