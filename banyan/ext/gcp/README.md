# Azure

Ensure you have the [Google Cloud Client Libraries for Python](https://cloud.google.com/compute/docs/tutorials/python-guide) installed and configured.

```bash
pip install -r requirements.txt
```

## Configuration

Set up your service account credentials to access Google Cloud
```bash
GOOGLE_APPLICATION_CREDENTIALS=/path/to/my/key.json
```

Other credentials configuration methods are available. See the GCP docs for details.

## Test

Confirm you are set up correctly, by running:

```bash
python main.py
```

You should see a list of your GCP VM resources.



export GOOGLE_APPLICATION_CREDENTIALS="~/workspace/banyan/_clouds/gcp/tdnovpn-bfc18a4833d2.json"