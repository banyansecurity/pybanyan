
# Azure

Ensure you have the [Microsoft Graph SDK for Python](https://github.com/microsoftgraph/msgraph-sdk-python-core) installed and configured.

```bash
pip install -r requirements.txt
```

## Permissions

Create a [service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) and ensure it has permissions granted for your organization. Specifically, you need `Application.ReadWrite.All`, `Group.Read.All`, `GroupMember.ReadWrite.All` permission to interact with the Graph API.


## Configuration

Set up environment variables for your service principal
```bash
AZURE_SUBSCRIPTION_ID="id of your Azure subscription"
AZURE_TENANT_ID="id of the application's Azure Active Directory tenant"
AZURE_CLIENT_ID="id of an Azure Active Directory application"
AZURE_CLIENT_SECRET="one of the application's client secrets"
```

Other credentials configuration methods are available. See the Azure docs for details.

## Test

Confirm you are set up correctly, by running:

```bash
python -u application.py
```

You should see a list of your AzureAD applications.

