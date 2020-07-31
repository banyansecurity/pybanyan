import json
import sys

from cement import Controller
from cement.utils.version import get_version_banner

from ..core.version import get_version

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
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
            (['--api-url'],
             {'help': 'URL for the Banyan API server. Can also be configured via the BANYAN_API_URL '
                      'environment variable.'}),
            (['--refresh-token'],
             {'help': 'API token used for the initial authentication to the Banyan API server. Can also be '
                      'configured via the BANYAN_REFRESH_TOKEN environment variable.'}),
            (['--output-format', '-o'],
             {'choices': ['table', 'json', 'yaml'],
              'help': 'desired output format (table, json, yaml)'}),
        ]

    def _post_argument_parsing(self):
        super()._post_argument_parsing()
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
