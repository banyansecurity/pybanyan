from pathlib import Path
import configparser

# IDP credentials in named sections in ~/.banyan.conf file
class IdpConf:
    PROVIDERS = {
        'okta': [
            'org_url',
            'token'
        ],
        'azure_ad': [
            'azure_subscription_id',
            'azure_tenant_id',
            'azure_client_id',
            'azure_client_secret'
        ]
    }
    PATH = Path.home() / '.banyan.conf'

    @staticmethod
    def get_creds(provider: str):
        try:
            vars = IdpConf.PROVIDERS[provider]
            cp = configparser.ConfigParser()
            if IdpConf.PATH.exists():
                cp.read(IdpConf.PATH)
                creds = dict()
                for var in vars:
                    creds[var] = cp.get(provider, var)
                return creds
        except Exception as ex:
            print('ReadConfFileError > %s' % ex.args[0])
            raise
