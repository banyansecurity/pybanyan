from typing import List, Dict, ClassVar, Type, Optional, Union
from dataclasses import dataclass, field
import os

try:
    import oci
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


class OciController:
    def __init__(self, filter_by_compartment: str, filter_by_region: str = None, filter_by_tag_name: str = None):
        try:
            self._config = oci.config.from_file()
            self._tenancy = self._config.get('tenancy')
            identity_client = oci.identity.IdentityClient(self._config)
        except Exception as ex:
            print('OCISDKError > %s' % ex.args[0])
            raise
        self._filter_by_compartment = filter_by_compartment
        self._filter_by_region = filter_by_region
        self._filter_by_tag_name = filter_by_tag_name

        self._provider = 'OCI'
        self._account = IaasLevel('tenant', self._tenancy, 'root')
        try:
            # all compartments from root, parent is in compartment_id
            self._compartment_list = identity_client.list_compartments(compartment_id=self._tenancy, compartment_id_in_subtree=True).data
        except Exception as ex:
            print('OciControllerError > %s' % ex.args[0])
            raise
        

    def list_vm(self):
        res_type = 'vm'
        compute_client = oci.core.ComputeClient(self._config)
        network_client = oci.core.VirtualNetworkClient(self._config)

        instances: List[IaasResource] = list()
        for compartment_obj in self._compartment_list:
            #print(compartment_obj)
            cmpt_id = compartment_obj.id
            cmpt_name = compartment_obj.name
            if self._filter_by_compartment != 'all' and self._filter_by_compartment != cmpt_name:
                continue

            vm_list = compute_client.list_instances(compartment_id=cmpt_id).data
            for vm in vm_list:
                #print(vm)
                vnic_attachments = compute_client.list_vnic_attachments(compartment_id=cmpt_id, instance_id=vm.id).data
                # assume only 1 NIC
                vnic = network_client.get_vnic(vnic_attachments[0].vnic_id).data
                #print(vnic)
                private_ip = vnic.private_ip
                public_ip = ''
                if vnic.public_ip:
                    public_ip = vnic.public_ip

                res_tags = dict()
                res_tags.update(vm.freeform_tags)
                for key, subkeyval in vm.defined_tags.items():
                    for subkey, val in subkeyval.items():
                        newkey = key + '-' + subkey
                        res_tags[newkey] = val

                res_inst = IaasInstance(
                    type = res_type,
                    id =  vm.id,
                    name = vm.display_name,
                    private_ip = private_ip,
                    public_ip = public_ip,
                    tags = res_tags
                )

                res_parent = IaasLevel('compartment', compartment_obj.id, compartment_obj.name)
                res_loc = IaasLocation('region', vm.region, '')

                res = IaasResource(
                    provider = self._provider,
                    account = self._account,
                    parent = res_parent,
                    location = res_loc,
                    instance = res_inst
                )
                instances.append(res)

        return instances


if __name__ == '__main__':
    orl = OciController('all')
    my_vms = orl.list_vm()
    print(my_vms)