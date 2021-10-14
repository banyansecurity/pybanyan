# Azure

Banyan uses the [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python) to synchronize Azure resources into Banyan's inventory.

If you installed `pybanyan` using `pip`, get the Azure extra:
```console
$ pip install pybanyan[azure_cloud]
```

## Authentication

Create a Service Principal via the [Azure Portal](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) or the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli).

Assign the following built-in role to your Service Principal:
- Reader 

Grab the [credentials](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd#what-the-create-for-rbac-command-does) for your Service Principal.

Add a section named `azure` in the `~/.banyan.conf` file with your Service Principal credentials:
```ini
[banyan]
api_url = ...
refresh_token = ...

[azure]
azure_subscription_id = "id of your Azure subscription"
azure_tenant_id = "id of the application's Azure Active Directory tenant"
azure_client_id = "id of an Azure Active Directory application"
azure_client_secret = "one of the application's client secrets"
```

## Multiple Resource Groups

You can discover resources across multiple resource groups in the Azure subscription.


## Test

Run the test command to verify access:

```
banyan cloud-resource test-azure
```

## Synchronize

Run the sync command to synchronize your Iaas resources:

```bash
banyan cloud-resource sync-azure
```