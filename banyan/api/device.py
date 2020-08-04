from typing import List

from banyan.api.base import ServiceBase
from banyan.core.exc import BanyanError
from banyan.model.user_device import Device, TrustScore


class DeviceAPI(ServiceBase):
    UPDATE_FIELDS = ['architecture', 'model', 'platform', 'ownership', 'is_banned']

    class Meta:
        data_class = Device
        info_class = Device
        arg_type = str
        list_uri = '/devices'
        delete_uri = '/delete_device'
        insert_uri = '/mdm/update_device'
        uri_param = 'SerialNumber'
        obj_name = 'device'

    def create(self, obj: Device):
        raise BanyanError('devices cannot be created via the API')

    def update(self, obj: Device) -> str:
        self._ensure_exists(obj.serial_number)
        response_json = self._client.api_request('POST',
                                                 self.Meta.insert_uri,
                                                 params={self.Meta.uri_param: obj.serial_number},
                                                 json=obj.Schema(only=DeviceAPI.UPDATE_FIELDS).dump(obj))
        return response_json['Message']

    def ban(self, obj: Device) -> str:
        obj.is_banned = True
        return self.update(obj)

    def unban(self, obj: Device) -> str:
        obj.is_banned = False
        return self.update(obj)

    def set_max_trustlevel(self, obj: Device, max_level: str, reason: str, ext_source: str) -> str:
        self._ensure_exists(obj.serial_number)
        response_json = self._client.api_request('POST',
                                                 '/set_max_trust_level',
                                                 params={self.Meta.uri_param: obj.serial_number},
                                                 json={
                                                     'Level': max_level,
                                                     'Reason': reason,
                                                     'ExtSource': ext_source
                                                 })
        return TrustScore.Schema().load(response_json)

    def get_trustscores(self, obj: Device) -> List[TrustScore]:
        self._ensure_exists(obj.serial_number)
        response_json = self._client.api_request('GET',
                                                 '/trustscore',
                                                 params={self.Meta.uri_param: obj.serial_number})
        return TrustScore.Schema().load(response_json, many=True)
