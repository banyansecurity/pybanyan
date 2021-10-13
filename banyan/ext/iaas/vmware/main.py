from typing import List, ClassVar, Type, Optional, Union
from dataclasses import dataclass, field
import os
import ssl, requests, urllib3

try: 
    from vmware.vapi.vsphere.client import create_vsphere_client
    from com.vmware.vapi.std_client import DynamicID
    from com.vmware.vcenter_client import VM
    from com.vmware.vcenter.vm_client import Power
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise

@dataclass
class VmwareResourceModel:
    organization: str

    datacenter: str
    region: str

    type: str
    id: str
    name: str
    public_dns_name: str = ''
    public_ip: str = ''
    private_dns_name: str = ''
    private_ip: str = ''
    ports: str = ''
    tags: List = field(default_factory=list)

    PROVIDER = 'VMWARE'
    ACCOUNT = 'VPHERE'

class VmwareController:
    def __init__(self, datacenter: str = None, tag_name: str = None):
        try:
            server = os.environ["VSPHERE_SERVER"]
            username = os.environ["VSPHERE_USERNAME"]
            password = os.environ["VSPHERE_PASSWORD"]
            nossl = os.environ["VSPHERE_NOSSL"] != None
            
            session = None
            if nossl:
                session = requests.session()
                session.verify = False
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            self._vsphere_client = create_vsphere_client(server=server, username=username, password=password, session=session)
        except :
            print('VMwareSDKError > %s' % ex.args[0])
            raise
        self._datacenter_list = self._vsphere_client.vcenter.Datacenter.list()
        self._datacenter = datacenter
        self._tag_name = tag_name


    def list_vm(self):
        resource_type = 'vm'
        vcenter_client = self._vsphere_client.vcenter
        tagging_client = self._vsphere_client.tagging

        instances: List[VmwareResourceModel] = list()

        # get VMs by Datacenter
        for dc in list(self._datacenter_list):
            if self._datacenter and self._datacenter != dc.name:
                continue

            filter_spec = VM.FilterSpec(datacenters=set([dc.datacenter]))
            vm_list = vcenter_client.VM.list(filter_spec)

            for vm in list(vm_list):
                vm_model = vcenter_client.VM.get(vm.vm)
                #print(vm_model)
                if (vm.power_state != Power.State.POWERED_ON):
                    continue

                res = VmwareResourceModel(
                    datacenter = dc.name,
                    type = resource_type,
                    id = vm_model.identity.instance_uuid,
                    name = vm_model.name,
                )

                # Private IP via Guest Additions
                try:
                    guest_model = vcenter_client.vm.guest.Identity.get(vm.vm)
                    res.private_ip = guest_model.ip_address
                except Exception as ex:
                    print('Guest additions issue; could not detect IP for: %s' % vm_model.name)

                # VM tags are a different system w category & tag
                tags_obj = {}
                dynamic_id = DynamicID(type='VirtualMachine', id=vm.vm)
                tag_list = tagging_client.TagAssociation.list_attached_tags(dynamic_id)
                for tag_id in list(tag_list):
                    tag_model = tagging_client.Tag.get(tag_id)
                    category_model = tagging_client.Category.get(tag_model.category_id)
                    key = category_model.name + ':' + tag_model.name
                    tags_obj[key] = 'true'
                res.tags = tags_obj

                if self._tag_name and not res.tags.get(self._tag_name):
                    continue

                instances.append(res)

        return instances


if __name__ == '__main__':
    vmw = VmwareController(None, 'banyan:discovery')
    my_vms = vmw.list_vm()
    print(my_vms)