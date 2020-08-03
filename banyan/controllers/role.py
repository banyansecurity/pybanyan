from typing import List

from cement import Controller, ex

from banyan.api.role import RoleAPI
from banyan.controllers.base import Base
from banyan.model.role import RoleInfo, Role


class RoleController(Controller):
    class Meta:
        label = 'role'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage user and workload roles'

    @property
    def _client(self) -> RoleAPI:
        return self.app.client.roles

    @ex(help='list roles')
    def list(self):
        roles: List[RoleInfo] = self._client.list()
        results = list()
        headers = ['Name', 'ID', 'Created', 'Last Updated']
        for role in roles:
            new_row = [role.role_name, role.role_id,
                       role.created_at.strftime(Base.TABLE_DATE_FORMAT),
                       role.last_updated_at.strftime(Base.TABLE_DATE_FORMAT)]
            results.append(new_row)
        results.sort(key=lambda x: x[0])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='show the definition of a role',
        arguments=[
            (['role_name'],
             {
                 'metavar': 'role_name_or_id',
                 'help': 'Name or ID of the role to display.'
             }),
        ])
    def get(self):
        info: RoleInfo = self._client[self.app.pargs.role_name]
        role_json = Role.Schema().dump(info.role)
        # colorized_json = highlight(policy_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(role_json, handler='json', indent=2, sort_keys=True)

    @ex(help='create a new role from a JSON specification',
        arguments=[
            (['role_spec'],
             {
                 'help': 'JSON blob describing the new role to be created, or a filename '
                         'containing JSON prefixed by "@" (example: @service.json).'
             }),
        ])
    def create(self):
        spec = Base.get_json_input(self.app.pargs.role_spec)
        role = Role.Schema().load(spec)
        role_id = self._client.create(role)
        self.app.print(f'Role ID: {role_id}')

    @ex(help='update an existing role',
        arguments=[
            (['policy_spec'],
             {
                 'help': 'JSON blob describing the role to be updated, or a filename '
                         'containing JSON prefixed by "@" (example: @service.json).'
             }),
        ])
    def update(self):
        policy_spec = Base.get_json_input(self.app.pargs.role_spec)
        policy = Role.Schema().load(policy_spec)
        policy_info = self._client.update(policy)
        self.app.render(RoleInfo.Schema().dump(policy_info), handler='json', indent=2, sort_keys=True)

    @ex(help='delete a role',
        arguments=[
            (['role_name'],
             {
                 'metavar': 'role_name_or_id',
                 'help': 'Name or ID of the role to delete.'
             }),
        ])
    def delete(self):
        role: RoleInfo = self._client[self.app.pargs.role_name]
        self.app.print(self._client.delete(role))

    @ex(help='enable a role',
        arguments=[
            (['role_name'],
             {
                 'metavar': 'role_name_or_id',
                 'help': 'Name or ID of the role to delete.'
             }),
        ])
    def enable(self):
        role: RoleInfo = self._client[self.app.pargs.role_name]
        self.app.print(self._client.enable(role))

    @ex(help='disable a role',
        arguments=[
            (['role_name'],
             {
                 'metavar': 'role_name_or_id',
                 'help': 'Name or ID of the role to delete.'
             }),
        ])
    def disable(self):
        role: RoleInfo = self._client[self.app.pargs.role_name]
        self.app.print(self._client.disable(role))
