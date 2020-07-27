from cement import Controller, ex


class RoleController(Controller):
    class Meta:
        label = 'role'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage user and workload roles'

    @ex(help='create a new role')
    def create(self):
        pass

    @ex(help='delete a service')
    def delete(self):
        pass

    @ex(help='list registered services')
    def list(self):
        pass

    @ex(help='update an existing role')
    def update(self):
        pass

    @ex(help='enable a service')
    def enable(self):
        pass

    @ex(help='disable a service')
    def disable(self):
        pass
