# Google Cloud Platform

Banyan uses the [Google Cloud Client Libraries for Python](https://cloud.google.com/compute/docs/tutorials/python-guide) to synchronize GCP resources into Banyan's inventory.

If you installed `pybanyan` using `pip`, get the GCP extra:
```console
$ pip install pybanyan[gcp]
```

## Authentication

Create a [Service Account](https://cloud.google.com/iam/docs/creating-managing-service-accounts).

Assign the following IAM roles to your Service Account:
- Project Viewer

Create a key and download the JSON key file.

Add a section named `gcp` in the `~/.banyan.conf` file with the path to your Service Account's JSON key file:

```ini
[banyan]
api_url = ...
refresh_token = ...

[gcp]
google_application_credentials=/path/to/my/key.json
```

**Note:** if you're on Windows, Python still uses `/` not `\` in the path to key file, so you'd use `C:/Users/foobar/key.json` and not `C:\Users\foobar\key.json`.


## Multiple Projects

The same Service Account can be used to discover resources across multiple projects. As in [this post](https://gtseres.medium.com/using-service-accounts-across-projects-in-gcp-cf9473fef8f0), add the Service Account email address and assign the IAM roles in each project you want to synchronize.


## Test

Run the test command to verify access:

```bash
banyan cloud-resource test-gcp
```


## Synchronize

Run the sync command to synchronize your Iaas resources:

```bash
banyan cloud-resource sync-gcp
```