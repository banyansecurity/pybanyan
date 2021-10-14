# VMware vSphere

**NOTE: WIP!**

Banyan uses the [VMware vSphere Automation SDK for Python](https://github.com/vmware/vsphere-automation-sdk-python) to synchronize vSphere resources into Banyan's inventory.

Install the SDK following instructions in the repo:
```console
$ pip install git+https://github.com/vmware/vsphere-automation-sdk-python.git
```

## Configuration

Set up environment variables to connect to the vSphere API.
```bash
VSPHERE_SERVER="vSphere service address to connect to"
VSPHERE_USERNAME="User name to use when connecting to host"
VSPHERE_PASSWORD="Password to use when connecting to host"
VSPHERE_NOSSL="Set to Disable ssl host certificate verification"
```

## Test

Try the Controller:

```console
python -m banyan.ext.iaas.vmware
```

You should see a list of your VMs.

