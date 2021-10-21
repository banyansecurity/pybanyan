from typing import List
from time import sleep
import os

from banyan.api import BanyanApiClient
from banyan.model.cloud_resource import CloudResourceInfo
from banyan.controllers.base import Base
from banyan.ext.iaas.gcp import GcpController
from banyan.ext.iaas.base import IaasResource

from flask import Flask

# sync_gcp
app = Flask(__name__)
@app.route('/')
def handler():
    print("--> entering Cloud Functions handler")

    # env vars: BANYAN_API_URL, BANYAN_REFRESH_TOKEN
    bnn = BanyanApiClient()

    resource_type = os.getenv('RESOURCE_TYPE')
    project = os.getenv('PROJECT', 'all')
    zone = os.getenv('ZONE', 'all')
    tag_name = os.getenv('TAG_NAME', '')
    rt = resource_type.lower()

    # env vars: GOOGLE_CLOUD_FUNCTIONS (so GcpController knows not to look for config file)
    gcp = GcpController(project, zone, tag_name)

    instances: List[IaasResource] = list()
    if resource_type == 'vm' or resource_type == 'all':
        instances += gcp.list_vm()

    if len(instances) == 0:
        print('--> No AWS resources to sync')
        return

    params = {'cloud_provider': gcp.provider, 'resource_type': rt, 'account': project, 'region': zone}
    synced_resources: List[CloudResourceInfo] = bnn.cloud_resources.list(params=Base.sanitize_alls(params))
    added_instances = Base.added_iaas_resources(instances, synced_resources)

    if len(added_instances) == 0:
        print('--> No new GCP resources to sync')
        return

    for instance in added_instances:
        res = Base.convert_iaas_resource(instance)
        bnn.cloud_resources.create(res)
        print('\n--> Added GCP resource id(name): %s(%s)' % (res.resource_id, res.resource_name))
        sleep(0.05)

    print('\n--> Sync with GCP successful.')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
