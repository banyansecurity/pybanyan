import datetime
from cement import Controller, ex
from banyan.core.exc import BanyanError
from banyan.api.resource import ResourceAPI
from banyan.controllers.base import Base
from banyan.bcolors import bcolors
# from banyan.lib.service import DEFAULT_TIMEOUT, DEFAULT_DNS_SERVER, ServiceTest

DEFAULT_TIMEOUT = 0.5
DEFAULT_DNS_SERVER = '8.8.8.8'


class ResourceController(Controller):
    class Meta:
        label = 'resource'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'Manage automatically securing infrastructure behind Banyan'

    @property
    def _client(self) -> ResourceAPI:
        return self.app.client.resource

    @ex(help='find matching resources and service by tag.',
        arguments=[
            (
                ['-o', '--output-format'],
                {
                    'metavar': 'table',
                    'help': 'desired output format (table, json)',
                    'dest': 'output',
                    'choices': ['json', 'table'],
                })
        ])
    def search(self):
        output_type = "json" if not self.app.pargs.output else self.app.pargs.output.lower()
        api_result = None
        try:
            api_result = self._client.findAutoMatch()
        except BanyanError as err:
            self.app.log.error(repr(err))
            return

        if api_result is not None:
            if output_type == 'table':
                for result in api_result['data']:
                    service_id = result["service_id"]
                    print(
                        '\n-------------------------------- **************** ---------------------------------------')
                    print(
                        f'{bcolors.OKBLUE}Service ID: {service_id} {bcolors.ENDC}')
                    print(
                        f'{bcolors.OKBLUE}Tag Name: {result["name"]} \t Tag Value: {result["value"]}{bcolors.ENDC}')

                    print(
                        f'{bcolors.HEADER}Add & Remove Commands: \nbanyan resource add -n {result["name"]} -v',
                        f'{result["value"]} \nbanyan resource remove -n {result["name"]} -v {result["value"]}{bcolors.ENDC}')
                    results = list()
                    headers = ['Resource ID', 'Name',
                               'Private DNS/IP', 'Service Name']

                    for resource in result['resources']:
                        address = resource['private_ip'] if resource['private_ip'] else resource['private_dns_name']
                        address = (address[:20] + '..') if len(
                            address) > 22 else address

                        resource_id = (resource['resource_id'][:15] + '..') if len(
                            resource['resource_id']) > 17 else resource['resource_id']

                        if(resource['service_id'] != ""):
                            new_row = [bcolors.UNDERLINE + resource_id, resource['resource_name'],
                                       address, resource['service_id'] + ' *' + bcolors.ENDC]
                        else:
                            new_row = [resource_id, resource['resource_name'],
                                       address, resource['service_id']]
                        results.append(new_row)

                    results.sort(key=lambda x: x[0])
                    self.app.render(results, handler='tabulate',
                                    headers=headers, tablefmt='simple')
            else:
                self.app.render(api_result, handler='json', indent=4)

    @ex(help='Auto sync and match cloud resources and registered service by tag',
        arguments=[
            (
                ['-r', '--resource_type'],
                {
                    'choices': ['ec2', 'rds', 'lb', 'all'],
                    'metavar': 'rds',
                    'help': 'Sync by Resource Type ex - ec2, rds, lb, all',
                    'dest': 'resource_type',
                }),
        ])
    def auto(self):
        resource_type = "all" if not self.app.pargs.resource_type else self.app.pargs.resource_type.lower()
        self.app.log.info(f'sync resource type {resource_type}')
        response = []
        try:
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
                    f'invalid sync resource type {resource_type}, valid options are ec2, lb or rds')
        except BanyanError as err:
            self.app.log.error(repr(err))
            return

        api_result = None
        try:
            api_result = self._client.findAutoMatch()
        except BanyanError as err:
            self.app.log.error(repr(err))
            return

        if api_result is not None:
            for result in api_result['data']:
                service_id = result["service_id"]
                print('adding resources to the service')
                try:
                    print(
                        '\n-------------------------------- **************** ---------------------------------------')
                    print(
                        f'{bcolors.OKGREEN}Service ID: {service_id} {bcolors.ENDC}')
                    print(
                        f'{bcolors.OKCYAN}Tag Name: {result["name"]} \t Tag Value: {result["value"]}{bcolors.ENDC}')

                    result = self._client.add(
                        tag_name=result["name"], tag_value=result["value"])
                    if result['error_code'] > 0:
                        self.app.log.error(result['error_description'])
                    else:
                        self.app.log.info(result)
                except BanyanError as err:
                    self.app.log.error(
                        'failed to add resources to the service', repr(err))

    @ex(help='Find cloud resource and registered service by tag',
        arguments=[
            (
                ['-n', '--tag_name'],
                {
                    'metavar': 'service tag name',
                    'help': 'Filter by Tag Name.',
                    'dest': 'tag_name',
                }),
            (
                ['-v', '--tag_value'],
                {
                    'metavar': 'service tag value',
                    'help': 'Filter by Tag Value.',
                    'dest': 'tag_value',
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
    def find(self):
        tag_name = self.app.pargs.tag_name
        tag_value = self.app.pargs.tag_value
        output_type = "json" if not self.app.pargs.output else self.app.pargs.output.lower()
        api_result = None
        try:
            api_result = self._client.find(
                tag_name=tag_name, tag_value=tag_value)
        except BanyanError as err:
            self.app.log.error(repr(err))
            return

        if api_result is not None:
            if output_type == 'table':
                result = api_result['data']
                service_id = result["service_id"]
                self.app.log.debug(f'Found service: {service_id}')
                print(
                    '\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print(
                    f'{bcolors.OKGREEN}Service ID: {service_id} {bcolors.ENDC}\n')
                results = list()
                headers = ['ID', 'Resource ID', 'Name', 'DNS/IP',
                           'Region', 'Last Updated', 'Service ID']

                for resource in result['resources']:
                    serviceID = resource['service_id']
                    address = resource['private_ip'] if resource['private_ip'] else resource['private_dns_name']
                    address = (address[:20] + '..') if len(
                        address) > 22 else address

                    resource_id = (resource['resource_id'][:15] + '..') if len(
                        resource['resource_id']) > 17 else resource['resource_id']
                    if(serviceID != ""):
                        new_row = [bcolors.OKBLUE + resource['id'], resource_id, resource['resource_name'],
                                   address, resource['region'],
                                   datetime.datetime.fromtimestamp(
                            resource['updated_at'] // 1e9).strftime(Base.TABLE_DATE_FORMAT),
                            serviceID + ' *' + bcolors.ENDC]
                    else:
                        new_row = [resource['id'], resource_id, resource['resource_name'],
                                   address, resource['region'],
                                   datetime.datetime.fromtimestamp(
                            resource['updated_at'] // 1e9).strftime(Base.TABLE_DATE_FORMAT), serviceID]
                    results.append(new_row)

                results.sort(key=lambda x: x[0])
                self.app.render(results, handler='tabulate',
                                headers=headers, tablefmt='simple')
            else:
                self.app.render(api_result, handler='json', indent=4)

    @ex(help='Add cloud resource to a registered service by tag',
        arguments=[
            (
                ['-n', '--tag_name'],
                {
                    'metavar': 'service tag name',
                    'help': 'Filter by Tag Name.',
                    'dest': 'tag_name',
                }),
            (
                ['-v', '--tag_value'],
                {
                    'metavar': 'service tag value',
                    'help': 'Filter by Tag Value.',
                    'dest': 'tag_value',
                }),
            (
                ['-c', '--confirm'],
                {
                    'metavar': 'confirm',
                    'help': 'desired output format (Yes, No)',
                    'dest': 'confirm',
                    'choices': ['Yes', 'No'],
                })
        ])
    def add(self):
        tag_name = self.app.pargs.tag_name
        tag_value = self.app.pargs.tag_value
        confirm = "no" if not self.app.pargs.confirm else self.app.pargs.confirm.lower()
        try:
            response = self._client.find(
                tag_name=tag_name, tag_value=tag_value)
        except BanyanError as err:
            self.app.log.error(repr(err))
            return
        result = response['data']
        if confirm == 'no':
            results = list()
            headers = ['Resource ID', 'Name', 'DNS/IP',
                       'Region', 'Last Updated']

            service_id = result["service_id"]
            resource_ids = []
            print(
                '------------------------------------------------------------------------')
            print(f'{bcolors.OKBLUE}Matched Service {bcolors.ENDC}')
            print(f'{bcolors.OKGREEN}{service_id}{bcolors.ENDC}')
            print(
                '------------------------------------------------------------------------')
            print(
                f'{bcolors.OKBLUE}Matched Resources {bcolors.ENDC}')
            for resource in result['resources']:
                resource_ids.append(resource['id'])
                address = resource['private_ip'] if resource['private_ip'] else resource['private_dns_name']
                address = (address[:50] + '..') if len(
                    address) > 52 else address

                resource_id = (resource['resource_id'][:30] + '..') if len(
                    resource['resource_id']) > 32 else resource['resource_id']

                new_row = [resource_id, resource['resource_name'],
                           address, resource['region'],
                           datetime.datetime.fromtimestamp(
                    resource['updated_at'] // 1e9).strftime(Base.TABLE_DATE_FORMAT)]
                results.append(new_row)

            results.sort(key=lambda x: x[0])
            self.app.render(results, handler='tabulate',
                            headers=headers, tablefmt='simple')

            try:
                user_option = input(
                    f'{bcolors.OKCYAN}Please confirm to add above resources to the service: {bcolors.OKGREEN}"{service_id}"{bcolors.ENDC} {bcolors.OKCYAN} - yes/[no]: {bcolors.ENDC}')
                if user_option == 'yes':
                    print('adding resources to the service')
                    try:
                        result = self._client.add(
                            tag_name=tag_name, tag_value=tag_value)
                        if result['error_code'] > 0:
                            self.app.log.error(result['error_description'])
                        else:
                            self.app.log.info(result)
                    except BanyanError as err:
                        self.app.log.error(
                            'failed to add resources to the service', repr(err))
                else:
                    print('user has aborted the operation')
            except Exception as err:  # pylint: disable=broad-except
                self.app.log.error(err)
        else:
            print('todo: continue to add the IP address to service \n')

    @ex(help='Remove cloud resource from a registered service by tag',
        arguments=[
            (
                ['-n', '--tag_name'],
                {
                    'metavar': 'service tag name',
                    'help': 'Filter by Tag Name.',
                    'dest': 'tag_name',
                }),
            (
                ['-v', '--tag_value'],
                {
                    'metavar': 'service tag value',
                    'help': 'Filter by Tag Value.',
                    'dest': 'tag_value',
                }),
            (
                ['-c', '--confirm'],
                {
                    'metavar': 'confirm',
                    'help': 'desired output format (Yes, No)',
                    'dest': 'confirm',
                    'choices': ['Yes', 'No'],
                })
        ])
    def remove(self):
        tag_name = self.app.pargs.tag_name
        tag_value = self.app.pargs.tag_value
        confirm = "no" if not self.app.pargs.confirm else self.app.pargs.confirm.lower()
        try:
            response = self._client.find(
                tag_name=tag_name, tag_value=tag_value)
        except BanyanError as err:
            self.app.log.error(repr(err))
            return
        result = response['data']
        if confirm == 'no':
            results = list()
            headers = ['Resource ID', 'Name', 'DNS/IP',
                       'Region', 'Last Updated']

            service_id = result["service_id"]
            resource_ids = []
            print(
                '------------------------------------------------------------------------')
            print(f'{bcolors.OKBLUE}Matched Service {bcolors.ENDC}')
            print(f'{bcolors.OKGREEN}{service_id}{bcolors.ENDC}')
            print(
                '------------------------------------------------------------------------')
            print(
                f'{bcolors.OKBLUE}Matched Resources {bcolors.ENDC}')
            for resource in result['resources']:
                resource_ids.append(resource['id'])
                address = resource['private_ip'] if resource['private_ip'] else resource['private_dns_name']
                address = (address[:50] + '..') if len(
                    address) > 52 else address

                resource_id = (resource['resource_id'][:30] + '..') if len(
                    resource['resource_id']) > 32 else resource['resource_id']

                new_row = [resource_id, resource['resource_name'],
                           address, resource['region'],
                           datetime.datetime.fromtimestamp(
                    resource['updated_at'] // 1e9).strftime(Base.TABLE_DATE_FORMAT)]
                results.append(new_row)

            results.sort(key=lambda x: x[0])
            self.app.render(results, handler='tabulate',
                            headers=headers, tablefmt='simple')

            try:
                user_option = input(
                    f'{bcolors.OKCYAN}Please confirm to remove above resources from the service: {bcolors.OKGREEN}"{service_id}"{bcolors.ENDC} {bcolors.OKCYAN} - yes/[no]: {bcolors.ENDC}')
                if user_option == 'yes':
                    print('removing resources from the service')
                    try:
                        result = self._client.remove(
                            tag_name=tag_name, tag_value=tag_value)
                        if result['error_code'] > 0:
                            self.app.log.error(result['error_description'])
                        else:
                            self.app.log.info(result)
                    except BanyanError as err:
                        self.app.log.error(
                            'failed to remove resources from the service', repr(err))
                else:
                    print('user has aborted the operation')
            except Exception as err:  # pylint: disable=broad-except
                self.app.log.error(err)
        else:
            print('todo: continue to remove the IP address to service \n')
