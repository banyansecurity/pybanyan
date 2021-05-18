from dataclasses import dataclass
from typing import List, ClassVar, Type, Optional, Union
import os, json, time

try:
    from azure.identity import DefaultAzureCredential
    from msgraphcore import GraphSession
    from tabulate import tabulate
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise

@dataclass
class AzureADApplicationModel:
    class Meta:
        help = "AzureAD Application Model"

    app_id: str
    name: str
    template: str
    principal_id: str = ''
    link: str = ''
    

class AzureADApplicationController:
    class Meta:
        help = "AzureAD Application Controller"

    SCOPE_FOR_SERVICE_ACCOUNTS = 'https://graph.microsoft.com/.default'
    CUSTOM_APP_TEMPLATE_ID = '8adf8e6e-67b2-4cf2-a259-e3dc5476c621'

    def list(self):
        try:
            credential = DefaultAzureCredential()
            scopes = [AzureADApplicationController.SCOPE_FOR_SERVICE_ACCOUNTS]
            graph_session = GraphSession(credential, scopes)    
        except Exception as ex:
            print('MSGraphClientError > %s' % ex.args[0])
            raise
    
        response = graph_session.get('/applications')
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
            response = graph_session.get(
                f'/servicePrincipals?$search="appId:{application.app_id}"&$count=true',
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
        try:
            credential = DefaultAzureCredential()
            scopes = [AzureADApplicationController.SCOPE_FOR_SERVICE_ACCOUNTS]
            graph_session = GraphSession(credential, scopes)    
        except Exception as ex:
            print('MSGraphClientError > %s' % ex.args[0])
            raise

        response = graph_session.post(
            f'/applicationTemplates/{AzureADApplicationController.CUSTOM_APP_TEMPLATE_ID}/instantiate',
            json = { 'displayName': name }
        )
        application = response.json()['application']
        principal = response.json()['servicePrincipal']
        principal_id = principal['id']

        timer = 0
        while True:
            print(f'Waiting to update Service Principal {principal_id}')
            time.sleep(5)

            response = graph_session.get(f'/servicePrincipals/{principal_id}')
            if response.status_code != 200:
                print('Service Principal creation pending')
            else:
                print('Service Principal creation ok')

            response = graph_session.patch(
                f'/servicePrincipals/{principal_id}',
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
        try:
            credential = DefaultAzureCredential()
            scopes = [AzureADApplicationController.SCOPE_FOR_SERVICE_ACCOUNTS]
            graph_session = GraphSession(credential, scopes)    
        except Exception as ex:
            print('MSGraphClientError > %s' % ex.args[0])
            raise

        group_id = ''
        response = graph_session.get(
            f'/groups?$search="displayName:{group_name}"&$count=true',
            headers = {'ConsistencyLevel': 'eventual'}
        )
        if response.status_code == 200 and response.json()['@odata.count'] == 1:
            group = response.json()['value'][0]
            group_id = group['id']

        response = graph_session.get(f'/servicePrincipals/{principal_id}')
        principal = response.json()
        principal_id = principal['id']
        app_role_id = principal['appRoles'][0]['id']

        response = graph_session.post(
            f'/groups/{group_id}/appRoleAssignments',
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
