import logging

from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal

from banyan.api import BanyanApiClient
from banyan.controllers.admin import AdminController
from banyan.controllers.audit import AuditController
from banyan.controllers.base import Base
from banyan.controllers.device import DeviceController
from banyan.controllers.event import EventV2Controller
from banyan.controllers.export import ExportController
from banyan.controllers.netagent import NetagentController
from banyan.controllers.policy import PolicyController
from banyan.controllers.role import RoleController
from banyan.controllers.service import ServiceController
from banyan.controllers.service_web import ServiceWebController
from banyan.controllers.service_infra import ServiceInfraController
from banyan.controllers.shield import ShieldController
from banyan.controllers.user import UserController
from banyan.controllers.cloud_resource import CloudResourceController
from banyan.controllers.api_key import ApiKeyController
from banyan.controllers.connector import ConnectorController
from banyan.controllers.access_tier import AccessTierController
from banyan.controllers.service_tunnel import ServiceTunnelController

from .core.exc import BanyanError

# configuration defaults
CONFIG = init_defaults('banyan')
CONFIG['banyan']['api_url'] = BanyanApiClient.DEFAULT_API_URL
CONFIG['banyan']['refresh_token'] = None
CONFIG['banyan']['api_key'] = None


def extend_client(app: App) -> None:
    api_url = app.config.get('banyan', 'api_url')
    refresh_token = app.config.get('banyan', 'refresh_token')
    api_key = app.config.get('banyan', 'api_key')
    credential = api_key or refresh_token
    client = BanyanApiClient(api_url, credential, debug=app.debug)
    app.extend('client', client)


def set_logging(app: App) -> None:
    if app.debug:
        logging.basicConfig(level=logging.DEBUG)


class MyApp(App):
    """Banyan CLI primary application."""

    class Meta:
        label = 'banyan'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            # 'yaml',
            'colorlog',
            'json',
            'tabulate',
            # 'scrub',
            'print',
            # 'jinja2',
        ]

        hooks = [
            ('post_setup', extend_client),
            ('post_setup', set_logging)
        ]

        # configuration handler
        # config_handler = 'yaml'

        # configuration file suffix
        # config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'tabulate'

        # register handlers
        handlers = [
            Base,
            UserController,
            ServiceWebController,
            ServiceTunnelController,
            ServiceInfraController,
            RoleController,
            PolicyController,
            ExportController,
            EventV2Controller,
            DeviceController,
            ConnectorController,
            CloudResourceController,
            AuditController,
            ApiKeyController,
            AccessTierController,
            ShieldController,
            ServiceController,
            NetagentController,
        ]


class MyAppTest(TestApp, MyApp):
    """A sub-class of MyApp that is better suited for testing."""

    class Meta:
        label = 'banyan'


def main():
    with MyApp() as app:
        try:
            app.run()

        except AssertionError as ex:
            print('AssertionError > %s' % ex.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except BanyanError as ex:
            print('BanyanError > %s' % ex.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as ex:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % ex)
            app.exit_code = 0


if __name__ == '__main__':
    main()
