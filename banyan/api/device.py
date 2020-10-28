from typing import List

from banyan.api.base import ServiceBase
from banyan.core.exc import BanyanError
from banyan.model.user_device import Device, TrustScore


class DeviceAPI(ServiceBase):
    """
    API service for dealing with end-user devices (laptops, tablets, phones, etc).

    """

    # TODO: include name or device_friendly_name?
    _UPDATE_FIELDS = ['architecture', 'model', 'platform', 'ownership', 'is_banned']

    class Meta:
        """
        :meta private:
        """
        data_class = Device
        info_class = Device
        arg_type = str
        list_uri = '/devices'
        delete_uri = '/delete_device'
        insert_uri = '/mdm/update_device'
        uri_param = 'SerialNumber'
        obj_name = 'device'
        supports_paging = True

    def create(self, obj: Device):
        """
        Raises an exception. Devices cannot be created via API. They must be registered by installing the
        Banyan App on a device.

        :param obj: A device which will definitely not be created.
        :type obj: Device
        :raises: :py:exc:`BanyanError`
        """
        raise BanyanError('devices cannot be created via the API')

    def update(self, obj: Device) -> str:
        """
        Updates a limited set of properties belonging to a device. The properties that can be updated are:

        * Device hardware data: :py:data:`architecture`, :py:data:`model`, and :py:data:`platform`.
        * Corporate ownership status: :py:data:`ownership`.
        * Banned status: :py:data:`is_banned`.
        * User-friendly device name: :py:data:`device_friendly_name`.

        Changes to any other fields in the :py:class:`Device` object will be ignored.

        :param obj: The device to be updated.
        :type obj: Device
        :return: Message from the server indicating success or failure.
        :rtype: str
        """
        self._ensure_exists(obj.serial_number)
        response_json = self._client.api_request('POST',
                                                 self.Meta.insert_uri,
                                                 params={self.Meta.uri_param: obj.serial_number},
                                                 json=obj.Schema(only=DeviceAPI._UPDATE_FIELDS).dump(obj))
        return response_json['Message']

    def ban(self, obj: Device) -> str:
        """
        Bans a device, preventing it from accessing sites controlled by Banyan.

        :param obj: The device to be banned.
        :type obj: Device
        :return: Message from the server indicating success or failure.
        :rtype: str
        """
        obj.is_banned = True
        return self.update(obj)

    def unban(self, obj: Device) -> str:
        """
        Un-bans a device, allowing it to resume accessing sites controlled by Banyan.

        .. note:: After a device is unbanned, it must send updated Trust Factors to the server
           before it will be allowed to access anything. This happens automatically about once an hour,
           or can be forced manually by clicking the "Send Device Features" link in the app settings.

        :param obj: The device to be unbanned.
        :type obj: Device
        :return: Message from the server indicating success or failure.
        :rtype: str
        """
        obj.is_banned = False
        return self.update(obj)

    def set_max_trustlevel(self, obj: Device, max_level: str, reason: str, ext_source: str) -> str:
        """
        Overrides the maximum trust score a device will be allowed to have.

        :param obj: The device to be updated.
        :type obj: Device
        :param max_level: One of the :py:class:`TrustLevel` constants (:py:const:`ALWAYS_DENY`,
            :py:const:`LOW`, :py:const:`MEDIUM`, :py:const:`HIGH`, or :py:const:`ALWAYS_ALLOW`).
        :type max_level: str
        :param reason: Message indicating why the trust score was affected. This may be displayed to
            the user inside the app.
        :type reason: str
        :param ext_source: Name of the external source affecting the trust level (e.g. "CrowdStrike",
            "Carbon Black", etc).
        :type ext_source: str
        :return: Message from the server indicating success or failure.
        :rtype: str
        """
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
        """
        Returns the detailed list of Trust Factors that make up the device's Trust Score.

        In general, you will want to use the score in the `trust_data` field of the :py:class:`Device`
        object. When additional detail is required, this method may be used instead.

        :param obj: The device to be updated.
        :type obj: Device
        :return: a list of :py:class:`TrustScore` objects. Most devices will have one score
            with a `TrustType` of "Device". If a device's maximum trust score has been limited by
            a previous call to :py:meth:`set_max_trustlevel`, there will be an additional score
            with a `TrustType` of "External".
        :rtype: List[TrustScore]
        """
        self._ensure_exists(obj.serial_number)
        response_json = self._client.api_request('GET',
                                                 '/trustscore',
                                                 params={self.Meta.uri_param: obj.serial_number})
        return TrustScore.Schema().load(response_json, many=True)
