from pathlib import Path
import configparser
from typing import Dict, List
from dataclasses import dataclass, field

@dataclass
class IaasAccount:
    type: str
    id: str

@dataclass
class IaasRegion:
    type: str
    id: str

@dataclass
class IaasInstance:
    type: str
    id: str
    name: str = ''
    public_dns_name: str = ''
    public_ip: str = ''
    private_dns_name: str = ''
    private_ip: str = ''
    ports: List = field(default_factory=list)

@dataclass
class IaasResource:
    provider: str
    account: IaasAccount
    region: IaasRegion
    instance: IaasInstance
    tags: Dict

class IaasController:
    def __init__(self):
        self._provider = 'iaas'

    @property
    def provider(self) -> str:
        return self._provider.upper()


# IaaS credentials in named sections in ~/.banyan.conf file
class IaasConf:
    PROVIDERS = {
        'aws': [
            'aws_access_key_id', 
            'aws_secret_access_key'
        ],
        'azure': [
            'azure_subscription_id',
            'azure_tenant_id',
            'azure_client_id',
            'azure_client_secret'
        ],
        'gcp': [
            'google_application_credentials'
        ],
        'oci': [
            'user',
            'fingerprint',
            'tenancy',
            'region',
            'key_file'
        ],
        'vmware': [
            'vsphere_server',
            'vsphere_username',
            'vsphere_password',
            'vsphere_nossl'
        ]
    }
    PATH = Path.home() / '.banyan.conf'

    @staticmethod
    def get_creds(provider: str):
        try:
            vars = IaasConf.PROVIDERS[provider]
            cp = configparser.ConfigParser()
            if IaasConf.PATH.exists():
                cp.read(IaasConf.PATH)
                creds = dict()
                for var in vars:
                    creds[var] = cp.get(provider, var)
                return creds
        except Exception as ex:
            print('ReadConfFileError > %s' % ex.args[0])
            raise
