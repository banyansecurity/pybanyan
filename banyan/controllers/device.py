from cement import Controller, ex

from banyan.api import DeviceAPI
from banyan.controllers.base import Base
from banyan.model.user_device import Device, DeviceV2, TrustScore, TrustLevel


class DeviceController(Controller):
    class Meta:
        label = 'device'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage devices'

    @property
    def _client(self) -> DeviceAPI:
        return self.app.client.devices

    @ex(help='list devices',
        arguments=[
            (['--inactive'],
             {
                 'action': 'store_true',
                 'help': 'Include inactive devices.'
             }),
        ]) 
    def list(self):
        params = {"active": "true"}
        if self.app.pargs.inactive:
            params = {} 
        devices = self._client.list(params=params)
        results = list()
        headers = ['Device Name', 'Serial Number', 'Platform', 'Ownership', 'MDM', 'MDM Vendor', 'Trust Level', 'Trust Status', 'Last Login']
        for device in devices:
            new_row = [Base.trunc(device.device_friendly_name, 12, True), device.serial_number, device.platform,
                       device.ownership, device.mdm_present, device.mdm_vendor_name,
                       device.trust_level, device.trust_status,
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
        device = self._client.get_single(serial_number)
        device_json = DeviceV2.Schema().dump(device)
        # colorized_json = highlight(policy_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(device_json, handler='json', indent=2, sort_keys=True)

    @ex(help='update device attributes to set MDM vendor presence',
        arguments=[
            (['serial_number'],
             {
                 'help': 'Serial number of the device.'
             }),
             (['--mdm_present'], 
             {
                 'required': True,
                 'choices': ["true", "True", "false", "False"],
                 'help': 'Set MDM present to true/false.'
             }),
             (['--mdm_vendor_name'],
             {
                 'required': True,        
                 'help': 'Set MDM vendor name.'        
             })
        ])        
    def update(self):
        # get the device first
        serial_number = self.app.pargs.serial_number
        device = self._client.get_single(serial_number)
        device.mdm_present = self.app.pargs.mdm_present.lower() == "true"
        device.mdm_vendor_name = self.app.pargs.mdm_vendor_name
        print(self._client.update(device))
        device_json = DeviceV2.Schema().dump(device)
        self.app.render(device_json, handler='json', indent=2, sort_keys=True)

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
