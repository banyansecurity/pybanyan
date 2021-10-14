from typing import List
from dataclasses import dataclass
import os, time

from banyan.ext.idp.base import IdpConf

from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient
from tabulate import tabulate


@dataclass
class AzureADApplicationModel:
    app_id: str
    name: str
    template: str
    principal_id: str = ''
    link: str = ''
    

class AzureADApplicationController:
    def __init__(self):
        _azure_subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
        _azure_tenant_id = os.getenv('AZURE_TENANT_ID')
        _azure_client_id = os.getenv('AZURE_CLIENT_ID')
        _azure_client_secret = os.getenv('AZURE_CLIENT_SECRET')
        if not _azure_subscription_id:
            _creds = IdpConf.get_creds('azure_ad')
            _azure_subscription_id = _creds['azure_subscription_id']
            _azure_tenant_id = _creds['azure_tenant_id']
            _azure_client_id = _creds['azure_client_id']
            _azure_client_secret = _creds['azure_client_secret']

        try:
            os.environ['AZURE_SUBSCRIPTION_ID'] = _azure_subscription_id
            os.environ['AZURE_TENANT_ID'] = _azure_tenant_id
            os.environ['AZURE_CLIENT_ID'] = _azure_client_id
            os.environ['AZURE_CLIENT_SECRET'] = _azure_client_secret            
            _credential = DefaultAzureCredential()     # needs env vars
            self._scopes = [AzureADApplicationController.SCOPE_FOR_SERVICE_ACCOUNTS]
            self._client = GraphClient(credential = _credential)    
        except Exception as ex:
            print('AzureSDKError > %s' % ex.args[0])
            raise

    SCOPE_FOR_SERVICE_ACCOUNTS = 'https://graph.microsoft.com/.default'
    CUSTOM_APP_TEMPLATE_ID = '8adf8e6e-67b2-4cf2-a259-e3dc5476c621'

    def list(self):
        response = self._client.get('/applications', scopes=self._scopes)
        apps = response.json()['value']

        applications: List[AzureADApplicationModel] = list()
        for app in apps:
            res = AzureADApplicationModel(
                app['appId'],
                app['displayName'],
                app['applicationTemplateId']
            )
            applications.append(res)

        results = list()
        for application in applications:
            response = self._client.get(
                f'/servicePrincipals?$search="appId:{application.app_id}"&$count=true',
                scopes = self._scopes,
                headers = {'ConsistencyLevel': 'eventual'}
            )
            if response.status_code == 200 and response.json()['@odata.count'] == 1:
                principal = response.json()['value'][0]
                application.principal_id = principal['id']
                if principal['loginUrl'] is not None:
                    application.link = principal['loginUrl']

            allvars = vars(application)
            allvars['link'] = allvars['link'][:50] # table display
            results.append(allvars)

        print(tabulate(results, headers="keys"))
        return applications


    def create_bookmark(self, name: str, url: str):
        response = self._client.post(
            f'/applicationTemplates/{AzureADApplicationController.CUSTOM_APP_TEMPLATE_ID}/instantiate',
            scopes = self._scopes,
            json = { 'displayName': name }
        )
        application = response.json()['application']
        principal = response.json()['servicePrincipal']
        principal_id = principal['id']

        timer = 0
        while True:
            print(f'Waiting to update Service Principal {principal_id}')
            time.sleep(5)

            response = self._client.get(f'/servicePrincipals/{principal_id}', scopes = self._scopes)
            if response.status_code != 200:
                print('Service Principal creation pending')
            else:
                print('Service Principal creation ok')

            response = self._client.patch(
                f'/servicePrincipals/{principal_id}',
                scopes = self._scopes,
                json = { 'loginURL': f'{url}', 'preferredSingleSignOnMode': 'notsupported' }
            )
            if response.status_code != 204:
                print('Service Principal patch pending')
            else:
                print('Service Principal patch ok')
                break

            timer = timer + 1
            if timer > 10:
                raise Exception('AzureAD Create Bookmark failed')

        res = AzureADApplicationModel(
            application['appId'],
            application['displayName'],
            application['applicationTemplateId'],
            principal['id'],
            principal['loginUrl']
        )        
        return res


    def assign(self, principal_id: str, group_name: str):
        group_id = ''
        response = self._client.get(
            f'/groups?$search="displayName:{group_name}"&$count=true',
            scopes = self._scopes,
            headers = {'ConsistencyLevel': 'eventual'}
        )
        if response.status_code == 200 and response.json()['@odata.count'] == 1:
            group = response.json()['value'][0]
            group_id = group['id']

        response = self._client.get(f'/servicePrincipals/{principal_id}', scopes = self._scopes)
        principal = response.json()
        principal_id = principal['id']
        app_role_id = principal['appRoles'][0]['id']

        response = self._client.post(
            f'/groups/{group_id}/appRoleAssignments',
            scopes = self._scopes,
            # f'/servicePrincipals/{principal_id}', # requires an AD plan
            json = { 
                'principalId': group_id,
                'resourceId': principal_id,
                'appRoleId': app_role_id
            }
        )
        assignment = response.json()
        return assignment


    def delete(self):
        raise NotImplementedError('We do not support this operation. Use the AzureAD console.')


if __name__ == '__main__':
    aad = AzureADApplicationController()
    apps = aad.list()
    print(apps)
