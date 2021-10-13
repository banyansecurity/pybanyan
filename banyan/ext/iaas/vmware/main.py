from typing import List
import os
import requests, urllib3

try: 
    from vmware.vapi.vsphere.client import create_vsphere_client
    from com.vmware.vapi.std_client import DynamicID
    from com.vmware.vcenter_client import VM
    from com.vmware.vcenter.vm_client import Power
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise

try:
    from ..model import *
except:
    # trying to run "python main.py"
    import sys
    sys.path.append('..')
    from model import *


class VmwareController:
    def __init__(self, filter_by_datacenter: str, filter_by_tag_name: str = None):
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
        self._filter_by_datacenter = filter_by_datacenter
        self._filter_by_tag_name = filter_by_tag_name

        self._provider = 'VMWARE'
        self._account = IaasLevel('vsphere', server, '')
        try:
            self._datacenter_list = self._vsphere_client.vcenter.Datacenter.list()
        except Exception as ex:
            print('VmwareControllerError > %s' % ex.args[0])
            raise


    def list_vm(self):
        resource_type = 'vm'
        vcenter_client = self._vsphere_client.vcenter
        tagging_client = self._vsphere_client.tagging

        instances: List[IaasResource] = list()
        for dc in list(self._datacenter_list):
            if self._filter_by_datacenter != 'all' and self._filter_by_datacenter != dc.name:
                continue

            filter_spec = VM.FilterSpec(datacenters=set([dc.datacenter]))
            vm_list = vcenter_client.VM.list(filter_spec)

            for vm in list(vm_list):
                vm_model = vcenter_client.VM.get(vm.vm)
                #print(vm_model)
                if (vm.power_state != Power.State.POWERED_ON):
                    continue

                # Private IP via Guest Additions
                try:
                    guest_model = vcenter_client.vm.guest.Identity.get(vm.vm)
                    res_private_ip = guest_model.ip_address
                except Exception as ex:
                    print('Guest additions issue; could not detect IP for: %s' % vm_model.name)

                # VM tags are a different system w category & tag
                res_tags = dict()
                dynamic_id = DynamicID(type='VirtualMachine', id=vm.vm)
                tag_list = tagging_client.TagAssociation.list_attached_tags(dynamic_id)
                for tag_id in list(tag_list):
                    tag_model = tagging_client.Tag.get(tag_id)
                    category_model = tagging_client.Category.get(tag_model.category_id)
                    key = category_model.name + ':' + tag_model.name
                    res_tags[key] = 'true'

                if self._filter_by_tag_name and not res_tags.get(self._filter_by_tag_name):
                    continue

                res_inst = IaasInstance(
                    type = resource_type,
                    id = vm_model.identity.instance_uuid,
                    name = vm_model.name,
                )

                res_parent = IaasLevel('datacenter', dc.name, '')

                res = IaasResource(
                    provider = self._provider,
                    account = self._account,
                    parent = res_parent,
                    location = None,
                    instance = res_inst
                )
                instances.append(res)

        return instances


if __name__ == '__main__':
    vmw = VmwareController('all', 'banyan:discovery')
    my_vms = vmw.list_vm()
    print(my_vms)