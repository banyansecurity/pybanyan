import os
from typing import List
import copy
from time import sleep
from banyan.api import BanyanApiClient
from banyan.model.cloud_resource import CloudResource, CloudResourceInfo
from banyan.ext.iaas.base import IaasResource

from flask import Flask

app = Flask(__name__)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))


@app.route('/')
def handler():
    print("hanlder method being called")
    project = os.getenv('PROJECT')
    zone = os.getenv('ZONE')
    api_url = os.getenv('api_url')
    refresh_token = os.getenv('refresh_token')

    client = BanyanApiClient(api_url, refresh_token, debug=True)
    print("project: ", project)
    print("zone: ", zone)
    print("api_url: ", api_url)
    print("refresh_token: ", refresh_token)
    msg = sync_aws(banyan_api_client=client, project='banyan-dev', zone='us-west1')
    print(msg)
    return msg


def sync_aws(banyan_api_client, project, resource_type='all', zone=None, tag_name=None):
    try:
        from banyan.ext.iaas.gcp import GcpController
    except Exception as ex:
        raise NotImplementedError("GCP Client Libraries for Python not configured correctly > %s" % ex.args[0])
    try:
        instances: List[IaasResource] = list()
        gcp = GcpController(project, zone, tag_name)
        if resource_type == 'vm' or resource_type == 'all':
            instances += gcp.list_vm()

        print("instances", instances)
        if len(instances) == 0:
            return '--> No GCP resources to sync'

        params = {'cloud_provider': gcp.provider, 'resource_type': resource_type,
                  'account': project, 'region': zone}
        synced_resources: List[CloudResourceInfo] = banyan_api_client.cloud_resources.list(
            params=sanitize_alls(params))
        added_instances = added_iaas_resources(instances, synced_resources)

        new_results = tabulate_iaas_resources(added_instances)
        # self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')
        if len(new_results) == 0:
            return '--> No new GCP resources to sync'

        for instance in added_instances:
            res = convert_iaas_resource(instance)
            banyan_api_client.cloud_resources.create(res)
            print('\n--> Added GCP resource id(name): %s(%s)' % (res.resource_id, res.resource_name))
            sleep(0.05)

        return '--> Sync with GCP successful.'
    except Exception as ex:
        print(ex)
        return "GCP sync failed"


def added_iaas_resources(res_list: List[IaasResource], inv_list: List[CloudResource]) -> List[IaasResource]:
    added: List[IaasResource] = list()
    for res in res_list:
        exists = False
        for inv in inv_list:
            if res.instance.id == inv.resource_id:
                exists = True
                break
        if not exists:
            added.append(res)
    return added


def tabulate_iaas_resources(res_list: List[IaasResource], del_keys: List = []):
    results = list()
    for res in res_list:
        allvars = vars(copy.copy(res.instance))
        allvars['provider'] = res.provider
        allvars['account'] = res.account.id
        allvars['region'] = res.region.id
        # truncate
        for key, val in allvars.items():
            if val:
                allvars[key] = val[:16]
        # tags num
        allvars['tags'] = len(res.tags)
        # rm keys that don't print well
        for del_key in del_keys:
            allvars.pop(del_key)
        results.append(allvars)
    # self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')
    return results


def convert_iaas_resource(res: IaasResource) -> CloudResource:
    res_tags = []
    for key, val in res.tags.items():
        res_tag = {
            'name': key,
            'value': val
        }
        res_tags.append(res_tag)

    # enforce capitalization conventions, ports in a comma-separated string
    cloud_res = CloudResource(
        cloud_provider=res.provider.upper(),
        account=res.account.id,
        region=res.region.id,

        resource_type=res.instance.type.lower(),
        resource_id=res.instance.id,
        resource_name=res.instance.name,
        public_dns_name=res.instance.public_dns_name,
        public_ip=res.instance.public_ip,
        private_dns_name=res.instance.private_dns_name,
        private_ip=res.instance.private_ip,
        ports=(',').join(res.instance.ports),

        tags=res_tags
    )
    return cloud_res


def sanitize_alls(params):
    sanitized = {}
    for key, val in params.items():
        if val == 'all':
            val = None
        sanitized[key] = val
    return sanitized
