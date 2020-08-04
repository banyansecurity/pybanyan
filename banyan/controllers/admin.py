from cement import Controller, ex


class AdminController(Controller):
    class Meta:
        label = 'admin'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage administrator accounts'

    # @property
    # def _client(self) -> RoleAPI:
    #     return self.app.client.roles

    # TODO: implement
    @ex(help='list administrators')
    def list(self):
        pass

    # TODO: implement /admin/add_user
    @ex(help='create an administrator')
    def create(self):
        pass

    # TODO: implement /admin/delete_user
    @ex(help='delete an administrator')
    def delete(self):
        pass

    # TODO: implement /admin/update_user
    @ex(help='update settings for an existing administrator')
    def update(self):
        pass

    # TODO: implement /admin/saml
    @ex(help='get SAML SSO configuration for administrator login')
    def saml(self):
        pass

    # TODO: implement /admin/setup_saml
    @ex(help='set SAML SSO configuration for administrator login')
    def setup_saml(self):
        pass
