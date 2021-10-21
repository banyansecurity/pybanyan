from typing import List
import os

from banyan.ext.iaas.base import IaasAccount, IaasResource, IaasInstance, IaasRegion, IaasConf, IaasController

import oci


class OciController(IaasController):
    def __init__(self, filter_by_compartment_name: str, filter_by_region: str = None, filter_by_tag_name: str = None):
        self._provider = 'oci'

        if not os.getenv('OCI_CLI_USER'):
            _creds = IaasConf.get_creds(self._provider)
            os.environ['OCI_CLI_USER'] = _creds['user']
            os.environ['OCI_CLI_FINGERPRINT'] = _creds['fingerprint']
            os.environ['OCI_CLI_TENANCY'] = _creds['tenancy']
            os.environ['OCI_CLI_REGION'] = _creds['region']
            os.environ['OCI_CLI_KEY_FILE'] = _creds['key_file']

        try:
            self._config = {
                "user": os.getenv('OCI_CLI_USER'),
                "fingerprint": os.getenv('OCI_CLI_FINGERPRINT'),
                "tenancy": os.getenv('OCI_CLI_TENANCY'),
                "region": os.getenv('OCI_CLI_REGION'),               
                "key_file": os.getenv('OCI_CLI_KEY_FILE')
            }
            oci.config.validate_config(self._config)
            self._tenancy = self._config.get('tenancy')     # for clients
            identity_client = oci.identity.IdentityClient(self._config)
        except Exception as ex:
            print('OCISDKError > %s' % ex.args[0])
            raise
        self._filter_by_compartment_name = filter_by_compartment_name
        self._filter_by_region = filter_by_region
        self._filter_by_tag_name = filter_by_tag_name

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
            if self._filter_by_compartment_name != 'all' and self._filter_by_compartment_name != cmpt_name:
                continue

            vm_list = compute_client.list_instances(compartment_id=cmpt_id).data
            for vm in vm_list:
                #print(vm)
                #TODO: filter by region

                vnic_attachments = compute_client.list_vnic_attachments(compartment_id=cmpt_id, instance_id=vm.id).data
                # assume only 1 NIC
                vnic = network_client.get_vnic(vnic_attachments[0].vnic_id).data
                #print(vnic)
                private_ip = vnic.private_ip
                public_ip = ''
                if vnic.public_ip:
                    public_ip = vnic.public_ip

                # OCI has 2 types of tags - freeform and defined
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
                )

                res_acct = IaasAccount('compartment', cmpt_name)
                res_regn = IaasRegion('region', vm.region)

                res = IaasResource(
                    provider = self._provider,
                    account = res_acct,
                    region = res_regn,
                    instance = res_inst,
                    tags = res_tags
                )
                instances.append(res)

        return instances


if __name__ == '__main__':
    orl = OciController('all')
    my_vms = orl.list_vm()
    print(my_vms)