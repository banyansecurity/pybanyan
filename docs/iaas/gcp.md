# Google Cloud Platform

## 1. Python SDK

Install the [Google Cloud Client Libraries for Python](https://cloud.google.com/compute/docs/tutorials/python-guide):

```bash
pip install -r requirements.txt
```

## 2. Credentials

Create a [Service Account](https://cloud.google.com/iam/docs/creating-managing-service-accounts).

Assign the following IAM roles to your Service Account:
- Project Viewer

Create a key and download the JSON key file.

Add a section named `iaas-gcp` in the `~/.banyan.conf` file with the path to the JSON key file:

```ini
[banyan]
api_url = ...
refresh_token = ...

[iaas-gcp]
google_application_credentials=/path/to/my/key.json
```

Note that if you're on Windows, use `/` not `\` in the path here, so you'd use `C:/Users/foobar/key.json` and not `C:\Users\foobar\key.json`.


## 3. Additional Projects

The same Service Account can be used to discover resources across multiple projects. As in [this post](https://gtseres.medium.com/using-service-accounts-across-projects-in-gcp-cf9473fef8f0) add the Service Account email address and assign the IAM roles in each project you need.


## 4. Test

Confirm you are set up correctly, by running:

```bash
python main.py
```

You should see a list of your GCP VM resources.


---

## Development Notes

1. Python models

https://github.com/alfonsof/google-cloud-python-examples/blob/master/gcloudcomputeengine/computeenginehelper.py
https://googleapis.github.io/google-api-python-client/docs/epy/index.html
https://googleapis.github.io/google-api-python-client/docs/dyn/compute_v1.instances.html#aggregatedList