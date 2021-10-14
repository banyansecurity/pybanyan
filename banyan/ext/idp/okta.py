from typing import List
from dataclasses import dataclass
import os
import asyncio, functools

from banyan.ext.idp.base import IdpConf

from okta.client import Client as OktaClient
from okta.models import BookmarkApplicationSettingsApplication, BookmarkApplicationSettings, BookmarkApplication, ApplicationGroupAssignment
from tabulate import tabulate


@dataclass
class OktaApplicationModel:
    id: str
    label: str
    sign_on_mode: str
    status: str
    link: str = ''


class OktaApplicationController:
    def __init__(self):
        _okta_org_url = os.getenv('OKTA_ORG_URL')
        _okta_token = os.getenv('OKTA_TOKEN')
        if not _okta_org_url:
            _creds = IdpConf.get_creds('okta')
            _okta_org_url = _creds['org_url']
            _okta_token = _creds['token']

        try:
            config = {
                'orgUrl': _okta_org_url,
                'token': _okta_token,
                'raiseException': True
            }         
            self._client = OktaClient(config)
        except Exception as ex:
            print('OktaClientError > %s' % ex.args[0])
            raise            

    # no async needed -> https://gist.github.com/phizaz/20c36c6734878c6ec053245a477572ec
    def force_sync(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            res = fn(*args, **kwargs)
            if asyncio.iscoroutine(res):
                return asyncio.get_event_loop().run_until_complete(res)
            return res

        return wrapper


    @force_sync
    async def list(self):
        params = {'limit': 200}
        apps, resp, err = await self._client.list_applications(params)

        applications: List[OktaApplicationModel] = list()
        for app in apps:
            res = OktaApplicationModel( app.id,
                                        app.label,
                                        app.sign_on_mode,
                                        app.status
            )
            if 'appLinks' in app.links and len(app.links['appLinks']):
                res.link = app.links['appLinks'][0]['href']

            applications.append(res)

        results = list()
        for application in applications:
            allvars = vars(application)
            allvars['link'] = allvars['link'][:50] # table display
            results.append(allvars)

        print(tabulate(results, headers="keys"))
        return results


    @force_sync
    async def create_bookmark(self, label: str, url: str):
        # only support BookmarkApplication
        bookmark_app_settings_app = BookmarkApplicationSettingsApplication({
            'requestIntegration': False,
            'url': url
        })

        bookmark_app_settings = BookmarkApplicationSettings({
            'app': bookmark_app_settings_app
        })

        bookmark_app_model = BookmarkApplication({
            'label': label,
            'settings': bookmark_app_settings,
        })

        app, resp, err = await self._client.create_application(bookmark_app_model)
        return app


    @force_sync
    async def assign(self, app_id: str, group_name: str):
        params = {'q': group_name}
        app, resp, err = await self._client.list_groups(params)
        print (app, resp, err)
        group_id = ''
        if len(app):
            group_id = app[0].id
        if not group_id:
            raise Exception('Group not found')
        
        application_group_assignment = ApplicationGroupAssignment()
        app, resp, err = await self._client.create_application_group_assignment(app_id, group_id, application_group_assignment)
        return app


    def delete(self):
        raise NotImplementedError('We do not support this operation. Use the Okta console.')


if __name__ == '__main__':
    okta = OktaApplicationController()
    apps = okta.list()
    print(apps)
