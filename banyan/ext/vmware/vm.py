from typing import List, ClassVar, Type, Optional, Union
from dataclasses import dataclass
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
class VmModel:
    class Meta:
        help = "VMware vSphere VM Model"

    id: str
    name: str
    private_ip: str
    tags: List
    cloud_provider: str = 'VMware'
    type: str = 'VM'
    datacenter: str = 'datacenter1'
    public_ip: str = ''

class VmController:
    class Meta:
        help = "VMware vSphere VM Controller"

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

    def list(self):
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
            vsphere_client = create_vsphere_client(
                server=server,
                username=username,
                password=password,
                session=session)

            # old soap - vms
            service_instance = SmartConnect(
                host=server,
                user=username,
                pwd=password,
                sslContext=context)                
               
        except Exception as ex:
            print('VMwareSDKError > %s' % ex.args[0])
            raise
        
        instances: List[VmModel] = list()
        vm_list = vsphere_client.vcenter.VM.list()
        for vm in list(vm_list):
            vm_model = vsphere_client.vcenter.VM.get(vm.vm)
            guest_model = vsphere_client.vcenter.vm.guest.Identity.get(vm.vm)

            # vm tags are a different system w categort & tag
            tags_obj = {}
            dynamic_id = DynamicID(type='VirtualMachine', id=vm.vm)
            tag_list = vsphere_client.tagging.TagAssociation.list_attached_tags(dynamic_id)
            for tag_id in list(tag_list):
                tag_model = vsphere_client.tagging.Tag.get(tag_id)
                category_model = vsphere_client.tagging.Category.get(tag_model.category_id)
                key = category_model.name + ':' + tag_model.name
                tags_obj[key] = 'true'

            res = VmModel(
                vm_model.identity.instance_uuid,
                vm_model.name,
                guest_model.ip_address,
                tags_obj
            )
            instances.append(res)

        return instances


if __name__ == '__main__':
    vmc = VmController()
    my_vms = vmc.list()
    print(my_vms)