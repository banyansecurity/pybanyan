# Okta

Banyan uses the [Okta SDK for Python](https://github.com/okta/okta-sdk-python) to bookmark Services into your Okta SSO catalog.

If you installed `pybanyan` using `pip`, get the Okta extra:
```console
$ pip install pybanyan[okta]
```

## Authentication

Create an [API token](https://developer.okta.com/docs/guides/create-an-api-token/create-the-token/) via the Okta Portal.

API tokens inherit the privilege level of the admin account used to create them, so it is a good practice to create a service account with specific privilege level.

Get the token value and note your Org's URL.


Add a section named `okta` in the `~/.banyan.conf` file with your API token:
```ini
[banyan]
api_url = ...
refresh_token = ...

[okta]
org_url = https://YOUR_OKTA_DOMAIN
token = YOUR_API_TOKEN
```

## Test

Confirm you are set up correctly by running:

```bash
python -m banyan.ext.idp.okta
```

You should see a list of your Okta applications.


## Bookmark

You can now create an Okta bookmark application from a web service:

```bash
banyan cloud-resource bookmark-okta
```
