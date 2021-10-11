from typing import List, ClassVar, Type, Optional, Union
from dataclasses import dataclass, field
import os, re
import ssl, requests

try: 
    from vmware.vapi.vsphere.client import create_vsphere_client
    from com.vmware.vapi.std_client import DynamicID
    from pyVim.connect import SmartConnect, Disconnect
    from pyVmomi import vim, vmodl    
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise

@dataclass
class VmwareResourceModel:
    datacenter: str
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

class VmwareController:
    def __init__(self, datacenter: str = None, tag_name: str = None):
        try:
            server = os.environ["VSPHERE_SERVER"]
            username = os.environ["VSPHERE_USERNAME"]
            password = os.environ["VSPHERE_PASSWORD"]
            nossl = os.environ["VSPHERE_NOSSL"] != None
            session = None
            context = None
            if nossl:
                session = self.get_unverified_session()
                context = self.get_unverified_context()
            
            # new rest apis - tags
            self._vsphere_client = create_vsphere_client(
                server=server,
                username=username,
                password=password,
                session=session)

            # old soap - vms
            self._service_instance = SmartConnect(
                host=server,
                user=username,
                pwd=password,
                sslContext=context)                
        except Exception as ex:
            print('VMwareSDKError > %s' % ex.args[0])
            raise
        self._datacenter = datacenter
        self._tag_name = tag_name

    def get_unverified_context(self):
        context = None
        if hasattr(ssl, '_create_unverified_context'):
            context = ssl._create_unverified_context()
        return context

    def get_unverified_session(self):
        session = requests.session()
        session.verify = False
        requests.packages.urllib3.disable_warnings()
        return session


    def list_vm(self):
        resource_type = 'vm'
        
        vm_list = self._vsphere_client.vcenter.VM.list()

        instances: List[VmwareResourceModel] = list()
        for vm in list(vm_list):
            vm_model = self._vsphere_client.vcenter.VM.get(vm.vm)
            guest_model = self._vsphere_client.vcenter.vm.guest.Identity.get(vm.vm)

            res = VmwareResourceModel(
                datacenter = '',
                type = resource_type,
                id = vm_model.identity.instance_uuid,
                name = vm_model.name,
                private_ip = guest_model.ip_address,
                tags = tags_obj
            )

            # vm tags are a different system w category & tag
            tags_obj = {}
            dynamic_id = DynamicID(type='VirtualMachine', id=vm.vm)
            tag_list = self._vsphere_client.tagging.TagAssociation.list_attached_tags(dynamic_id)
            for tag_id in list(tag_list):
                tag_model = self._vsphere_client.tagging.Tag.get(tag_id)
                category_model = self._vsphere_client.tagging.Category.get(tag_model.category_id)
                key = category_model.name + ':' + tag_model.name
                tags_obj[key] = 'true'

            instances.append(res)

        return instances


if __name__ == '__main__':
    vmw = VmwareController()
    my_vms = vmw.list_vm()
    print(my_vms)