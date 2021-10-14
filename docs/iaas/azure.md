# Azure

## 1. Python SDK

Install the [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python):

```bash
pip install -r requirements.txt
```

## 2. Credentials

Create a Service Principal via the [Azure Portal](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) or the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli).

Assign the following built-in role to your Service Principal:
- Reader 

Grab the [credentials](https://docs.microsoft.com/en-us/azure/developer/python/configure-local-development-environment?tabs=cmd#what-the-create-for-rbac-command-does) for your Service Principal.

Add a section named `iaas-azure` in the `~/.banyan.conf` file with these credentials:
```ini
[banyan]
api_url = ...
refresh_token = ...

[iaas-aws]
azure_subscription_id = "id of your Azure subscription"
azure_tenant_id = "id of the application's Azure Active Directory tenant"
azure_client_id = "id of an Azure Active Directory application"
azure_client_secret = "one of the application's client secrets"
```

## 3. Test

Confirm you are set up correctly, by running:

```bash
python main.py
```

You should see a list of your Azure VM and LB resources.

---

## Development Notes

1. The `az ad sp create-for-rbac --name localtest-sp-rbac --skip-assignment` command generates JSON output similar to the following values.

  {
    "appId": "12345678-1111-2222-3333-1234567890ab",
    "displayName": "localtest-sp-rbac",
    "name": "http://localtest-sp-rbac",
    "password": "abcdef00-4444-5555-6666-1234567890ab",
    "tenant": "00112233-7777-8888-9999-aabbccddeeff"
  }
  
In this output, `tenant` is the `tenant_id`, `appId` is the `client_id`, and password is the `client_secret`.

2. To retrieve your subscription ID, run the `az account show` command and look for the id property in the output.