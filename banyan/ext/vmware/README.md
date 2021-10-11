# VMware vSphere

Ensure you have the [VMware vSphere Automation SDK for Python](https://github.com/vmware/vsphere-automation-sdk-python) installed and configured.

```bash
pip install -r requirements.txt
```

## Configuration

Set up environment variables to connect to the vSphere API.
```bash
VSPHERE_SERVER="vSphere service address to connect to"
VSPHERE_USERNAME="User name to use when connecting to host"
VSPHERE_PASSWORD="Password to use when connecting to host"
VSPHERE_NOSSL="Set to Disable ssl host certificate verification"
```

Other credentials configuration methods are available. See the VMware docs for details.


## Test

Confirm you are set up correctly, by running:

```console
python main.py
```

You should see a list of your VMs.

