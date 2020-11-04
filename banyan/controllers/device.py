from typing import List

from cement import Controller, ex

from banyan.api import DeviceAPI
from banyan.controllers.base import Base
from banyan.model.user_device import Device, TrustScore, TrustLevel


class DeviceController(Controller):
    class Meta:
        label = 'device'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage devices'

    @property
    def _client(self) -> DeviceAPI:
        return self.app.client.devices

    @ex(help='list devices')
    def list(self):
        devices: List[Device] = self._client.list()
        results = list()
        headers = ['Device Name', 'Serial Number', 'Platform', 'Ownership', 'Trust Score', 'Banned', 'Last Login']
        for device in devices:
            new_row = [device.device_friendly_name, device.serial_number, device.platform,
                       device.ownership, device.trust_data.level, device.is_banned,
                       device.last_login.strftime(Base.TABLE_DATE_FORMAT) if device.last_login else 'None']
            results.append(new_row)
        results.sort(key=lambda x: x[0])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='show detailed information about a device',
        arguments=[
            (['serial_number'],
             {
                 'help': 'Serial number of the device.'
             }),
        ])
    def get(self):
        serial_number = self.app.pargs.serial_number
        device = self._client.find(serial_number)
        device_json = Device.Schema().dump(device)
        # colorized_json = highlight(policy_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(device_json, handler='json', indent=2, sort_keys=True)

    # TODO: implement /mdm/update_device?SerialNumber=X
    @ex(help='update device status')
    def update(self):
        pass

    # TODO: implement /delete_device?Email=X&SerialNumber=Y
    @ex(help='delete a device')
    def delete(self):
        pass

    # TODO: implement /device/unregister
    @ex(help='unregister a device')
    def unregister(self):
        pass

    # TODO: implement /devices/stats
    @ex(help='display statistics about registered devices')
    def summary(self):
        pass

    @ex(help='ban a device (prevent it from accessing network resources)',
        arguments=[
            (['serial_number'],
             {
                 'help': 'Serial number of the device.'
             }),
        ])
    def ban(self):
        serial_number = self.app.pargs.serial_number
        device = self._client.find(serial_number)
        self.app.print(self._client.ban(device))

    @ex(help='remove the banned status from a device',
        arguments=[
            (['serial_number'],
             {
                 'help': 'Serial number of the device.'
             }),
        ])
    def unban(self):
        serial_number = self.app.pargs.serial_number
        device = self._client.find(serial_number)
        self.app.print(self._client.unban(device))

    @ex(help='set the maximum trust level for a device',
        arguments=[
            (['serial_number'],
             {
                 'help': 'Serial number of the device.'
             }),
            (['--trust-level'],
             {
                 'choices': TrustLevel.choices(),
                 'required': True,
                 'help': 'Maximum trust level for this device.'
             }
             ),
            (['--reason'],
             {
                 'required': True,
                 'help': 'Explanation to be displayed in console and to the end user.'
             }),
            (['--ext-source'],
             {
                 'required': True,
                 'help': 'Name of the external data source (e.g. CarbonBlack, CrowdStrike, etc).'
             }),
        ])
    def set_max_trust(self):
        serial_number = self.app.pargs.serial_number
        device = self._client.find(serial_number)
        trust = self._client.set_max_trustlevel(device, self.app.pargs.trust_level,
                                                self.app.pargs.reason, self.app.pargs.ext_source)
        trust_json = TrustScore.Schema().dump(trust)
        self.app.render(trust_json, handler='json', indent=2, sort_keys=True)

    @ex(help='show details about the device\'s trust score calculation',
        arguments=[
            (['serial_number'],
             {
                 'help': 'Serial number of the device.'
             }),
        ])
    def get_trust(self):
        serial_number = self.app.pargs.serial_number
        device = self._client.find(serial_number)
        trust = self._client.get_trustscores(device)
        trust_json = TrustScore.Schema().dump(trust, many=True)
        # colorized_json = highlight(policy_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(trust_json, handler='json', indent=2, sort_keys=True)
