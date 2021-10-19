
# Azure

Banyan uses the [Microsoft Graph SDK for Python](https://github.com/microsoftgraph/msgraph-sdk-python-core) to bookmark Services into your Azure AD SSO catalog.

If you installed `pybanyan` using `pip`, get the Azure AD extra:
```console
$ pip install pybanyan[azure_ad]
```


## Authentication

Create a Service Principal via the [Azure Portal](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) or the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli).

Assign the following built-in roles to your Service Principal to interact with the Graph API:
- Application.ReadWrite.All
- Group.Read.All
- GroupMember.ReadWrite.All

Grab the [credentials](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd#what-the-create-for-rbac-command-does) for your Service Principal.

Add a section named `azure_ad` in the `~/.banyan.conf` file with your Service Principal credentials:
```ini
[banyan]
api_url = ...
refresh_token = ...

[azure_ad]
azure_subscription_id = "id of your Azure subscription"
azure_tenant_id = "id of the application's Azure Active Directory tenant"
azure_client_id = "id of an Azure Active Directory application"
azure_client_secret = "one of the application's client secrets"
```

## Test

Confirm you are set up correctly by running:

```bash
python -m banyan.ext.idp.azure_ad
```

You should see a list of your AzureAD applications.


## Bookmark

You can now create an AzureAD Linked Sign-on from a web service:

```bash
banyan service bookmark-aad
```
