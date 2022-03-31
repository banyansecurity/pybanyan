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
from .core.exc import BanyanError

# configuration defaults
CONFIG = init_defaults('banyan')
CONFIG['banyan']['api_url'] = BanyanApiClient.DEFAULT_API_URL
CONFIG['banyan']['refresh_token'] = None


def extend_client(app: App) -> None:
    api_url = app.config.get('banyan', 'api_url')
    refresh_token = app.config.get('banyan', 'refresh_token')
    client = BanyanApiClient(api_url, refresh_token, debug=app.debug)
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
            CloudResourceController,
            ServiceInfraController,
            ServiceWebController,
            ServiceController,
            RoleController,
            PolicyController,
            ShieldController,
            NetagentController,
            UserController,
            DeviceController,
            AdminController,
            EventV2Controller,
            AuditController,
            ExportController
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
