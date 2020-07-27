from cement import Controller, ex


class PolicyController(Controller):
    class Meta:
        label = 'policy'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage authorization policies for users and workloads'

    @ex(help='create a new policy')
    def create(self):
        pass

    @ex(help='delete a policy')
    def delete(self):
        pass

    @ex(help='list policies')
    def list(self):
        pass

    @ex(help='update an existing policy')
    def update(self):
        pass

    @ex(help='enable a policy')
    def enable(self):
        pass

    @ex(help='disable a policy')
    def disable(self):
        pass

    @ex(help='show services attached to a policy')
    def list_attached(self):
        pass