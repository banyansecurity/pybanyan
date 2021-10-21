import json
import sys
from typing import List
import copy

from cement import Controller
from cement.utils.version import get_version_banner

from ..core.version import get_version

from banyan.ext.iaas.base import IaasResource
from banyan.model.cloud_resource import CloudResource

VERSION_BANNER = """
API library and command-line interface for Banyan Security %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    TABLE_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    class Meta:
        label = 'base'
        title = 'Commands'

        usage = 'banyan [options] <command> <subcommand> [<subcommand> ...] [parameters]'
        # text displayed at the top of --help output
        description = 'API library and command-line interface for Banyan Security'

        # text displayed at the bottom of --help output
        # epilog = 'Usage: banyan command1 --foo bar'

        # controller level arguments. ex: 'banyan --version'
        arguments = [
            # add a version banner
            (['--version', '-v'],
             {'action': 'version',
              'version': VERSION_BANNER}),
            (['--api-url'],
             {'help': 'URL for the Banyan API server. Can also be configured via the BANYAN_API_URL '
                      'environment variable.'}),
            (['--refresh-token'],
             {'help': 'API token used for the initial authentication to the Banyan API server. Can also be '
                      'configured via the BANYAN_REFRESH_TOKEN environment variable.'}),
            (['--insecure-tls', '-k'],
             {'action': 'store_true',
             'help': 'Allow connections to API servers with invalid TLS certificates.'}),
            (['--output-format', '-o'],
             {'choices': ['table', 'json', 'yaml'],
              'help': 'desired output format (table, json, yaml)'}),
        ]

    def _post_argument_parsing(self):
        super()._post_argument_parsing()
        self.app.client.insecure_tls = self.app.pargs.insecure_tls
        if self.app.pargs.api_url:
            self.app.client.api_url = self.app.pargs.api_url
        if self.app.pargs.refresh_token:
            self.app.client.refresh_token = self.app.pargs.refresh_token

    def _default(self):
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @staticmethod
    def get_json_input(arg: str):
        if arg[0] == '@':
            arg = open(arg[1:]).read()
        elif arg == '-':
            arg = sys.stdin.read()
        else:
            arg = arg.encode('utf-8')
        return json.loads(arg)       

    @staticmethod
    def wait_for_input(wait: bool, text: str):
        print('\n--> %s:' % text)
        if not wait:
            return
        user_input = input('press enter to continue, type "stop" to stop ...\n')
        if 'stop' in user_input:
            raise RuntimeError('User terminated workflow')

    @staticmethod
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

    @staticmethod
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
        #self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')
        return results

    @staticmethod
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
            cloud_provider = res.provider.upper(),
            account = res.account.id,
            region = res.region.id,

            resource_type = res.instance.type.lower(),
            resource_id = res.instance.id,
            resource_name = res.instance.name,
            public_dns_name = res.instance.public_dns_name,
            public_ip = res.instance.public_ip,
            private_dns_name = res.instance.private_dns_name,
            private_ip = res.instance.private_ip,
            ports = (',').join(res.instance.ports),

            tags = res_tags
        )
        return cloud_res

    @staticmethod
    def sanitize_alls(params):
        sanitized = {}
        for key, val in params.items():
            if val == 'all':
                val = None
            sanitized[key] = val
        return sanitized
