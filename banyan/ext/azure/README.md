# Azure

Ensure you have the [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python) installed and configured.

```bash
pip install -r requirements.txt
```

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
python vm.py
```

You should see a list of your Azure VMs.




