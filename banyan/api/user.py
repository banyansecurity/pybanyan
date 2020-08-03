from banyan.api.base import ServiceBase
from banyan.model.user_device import User


class UserAPI(ServiceBase):
    class Meta:
        data_class = User
        info_class = User
        arg_type = str
        list_uri = '/endusers'
        delete_uri = None
        insert_uri = None
        uri_param = None
        obj_name = 'user'

