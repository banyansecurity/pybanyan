# Azure

Ensure you have the [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python) installed and configured.

```bash
pip install -r requirements.txt
```

## Configuration

Set up environment variables for your service principal
```bash
export AZURE_SUBSCRIPTION_ID="id of your Azure subscription"
export AZURE_TENANT_ID="id of the application's Azure Active Directory tenant"
export AZURE_CLIENT_ID="id of an Azure Active Directory application"
export AZURE_CLIENT_SECRET="one of the application's client secrets"
```

Other credentials configuration methods are available. See the Azure docs for details.

## Test

Confirm you are set up correctly, by running:

```bash
python main.py
```

You should see a list of your Azure VM and LB resources.




