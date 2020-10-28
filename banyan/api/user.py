from typing import List

from banyan.api.base import ServiceBase
from banyan.model.user_device import User, TrustScore


class UserAPI(ServiceBase):
    class Meta:
        data_class = User
        info_class = User
        arg_type = str
        list_uri = '/endusers'
        delete_uri = None
        insert_uri = None
        uri_param = 'Email'
        obj_name = 'user'
        supports_paging = True

    def set_max_trustlevel(self, obj: User, max_level: str, reason: str, ext_source: str) -> str:
        self._ensure_exists(obj.email)
        response_json = self._client.api_request('POST',
                                                 '/set_max_trust_level',
                                                 params={self.Meta.uri_param: obj.email},
                                                 json={
                                                     'Level': max_level,
                                                     'Reason': reason,
                                                     'ExtSource': ext_source
                                                 })
        return TrustScore.Schema().load(response_json)

    def get_trustscores(self, obj: User) -> List[TrustScore]:
        self._ensure_exists(obj.email)
        response_json = self._client.api_request('GET',
                                                 '/trustscore',
                                                 params={self.Meta.uri_param: obj.email})
        return TrustScore.Schema().load(response_json, many=True)
