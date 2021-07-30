from typing import List
from uuid import UUID

import copy
from time import sleep

from cement import Controller, ex

from banyan.controllers.base import Base

from banyan.api import BanyanApiClient
from banyan.model.cloud_resource_service import CloudResourceService, CloudResourceServiceDetails


class CloudResourceServiceController(Controller):
    class Meta:
        label = 'cloud_resource_serice'
        aliases = ['crs']
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage cloud resources and service'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client

    @ex(help='list cloud_resource_service',
        arguments=[
            (['--service_id'],
             {
                'help': 'Filter by service_id.'
            }),
        ])
    def list(self):
        # todo: add filter service_id, cloud_resource_id, order_by
        d_resources: List[CloudResourceServiceDetails] = self._client._cloud_resource_service.list()
        results = list()
        headers = ['ID', 'Cloud Resource ID', 'Service ID', 'Port',
                   'Resource Type', 'Status', 'Cluster Name']
        for res in d_resources:
            new_res = [res.id, res.cloud_resource_id, res.service_id, res.port,
                       res.resource_type, res.status, res.cluster_name]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')
