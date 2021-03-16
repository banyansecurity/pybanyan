import datetime
from cement import Controller, ex
from banyan.api.cloud_inventory import CloudInventoryAPI
from banyan.controllers.base import Base
# from banyan.lib.service import DEFAULT_TIMEOUT, DEFAULT_DNS_SERVER, ServiceTest

DEFAULT_TIMEOUT = 0.5
DEFAULT_DNS_SERVER = '8.8.8.8'


class InventoryController(Controller):
    class Meta:
        label = 'inventory'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'Sync and list your cloud inventory to Banyan'

    @property
    def _client(self) -> CloudInventoryAPI:
        return self.app.client.inventory

    # include_tags=None, tag_name=None, tag_value=None, resource_type=None
    @ex(help='List cloud inventory, filter by inventory type, tag',
        arguments=[
            (
                ['-t', '--include_tags'],
                {
                    'action': 'store_true',
                    'help': 'Include tags.',
                    'dest': 'include_tags',
                }),
            (
                ['-n', '--tag_name'],
                {
                    'metavar': 'bnn-service-name',
                    'help': 'Filter by Tag Name.',
                    'dest': 'tag_name',
                }),
            (
                ['-v', '--tag_value'],
                {
                    'metavar': 'bnn-http-service',
                    'help': 'Filter by Tag Value.',
                    'dest': 'tag_value',
                }),
            (
                ['-r', '--resource_type'],
                {
                    'metavar': 'ec2',
                    'help': 'Filter by Resource Type ex - ec2, rds, lb.',
                    'dest': 'resource_type',
                    'choices': ['ec2', 'rds', 'lb'],
                }),
            (
                ['-o', '--output-format'],
                {
                    'metavar': 'table',
                    'help': 'desired output format (table, json)',
                    'dest': 'output',
                    'choices': ['json', 'table'],
                })
        ])
    def list(self):
        include_tags = self.app.pargs.include_tags
        tag_name = self.app.pargs.tag_name
        tag_value = self.app.pargs.tag_value
        resource_type = self.app.pargs.resource_type
        output_type = "json" if not self.app.pargs.output else self.app.pargs.output.lower()
        resources = self._client.list(
            include_tags=include_tags, tag_name=tag_name, tag_value=tag_value, resource_type=resource_type)

        if output_type == 'table':
            results = list()
            headers = ['ID', 'Resource ID', 'Name', 'DNS/IP',
                       'Region', 'Last Updated']

            for resource in resources:
                address = resource['public_ip'] if resource['public_ip'] else resource['public_dns_name']
                address = (address[:20] + '..') if len(
                    address) > 22 else address

                resource_id = (resource['resource_id'][:15] + '..') if len(
                    resource['resource_id']) > 17 else resource['resource_id']

                new_row = [resource['id'], resource_id, resource['resource_name'],
                           address, resource['region'],
                           datetime.datetime.fromtimestamp(
                               resource['updated_at'] // 1e9).strftime(Base.TABLE_DATE_FORMAT)]
                if include_tags and resource['tags']:
                    headers.append('Tags')
                    tags = []
                    for tag in resource['tags']:
                        tags.append(f"{tag['name']} : {tag['value']}")
                    new_row.append(tags)

                results.append(new_row)
            results.sort(key=lambda x: x[0])
            self.app.render(results, handler='tabulate',
                            headers=headers, tablefmt='simple')
        else:
            self.app.render(resources, handler='json', indent=4)

    @ex(help='Sync cloud inventory, Sync by inventory type',
        arguments=[
            (
                ['-r', '--resource_type'],
                {
                    'choices': ['ec2', 'rds', 'lb', 'all'],
                    'metavar': 'rds',
                    'help': 'Filter by Resource Type ex - ec2, rds, lb, all',
                    'dest': 'resource_type',
                })
        ])
    def sync(self):
        resource_type = "" if not self.app.pargs.resource_type else self.app.pargs.resource_type.lower()
        self.app.log.info(f'sync inventory type {resource_type}')
        response = []
        if resource_type == 'ec2':
            response = self.app.ec2.sync()
        elif resource_type == 'lb':
            response = self.app.lb.sync()
        elif resource_type == 'rds':
            response = self.app.rds.sync()
        elif resource_type == 'all':
            response_ec2 = self.app.ec2.sync()
            response.append(response_ec2)
            response_lb = self.app.lb.sync()
            response.append(response_lb)
            response_rds = self.app.rds.sync()
            response.append(response_rds)
        else:
            self.app.log.error(
                f'invalid sync inventory type {resource_type}, valid options are ec2, lb or rds')
        if self.app.debug is True:
            self.app.render(response, handler='json', indent=4)
