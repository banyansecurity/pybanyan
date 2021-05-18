# Okta

Ensure you have the [Okta SDK for Python](https://github.com/okta/okta-sdk-python) installed and configured.

```bash
pip install -r requirements.txt
```

## Configuration

Set up configuration (in ~/.okta/okta.yaml):
```yaml
okta:
  client:
    orgUrl: "https://{yourOktaDomain}"
    token: "YOUR_API_TOKEN"
```

Other credentials configuration methods are available. See the Okta docs for details.


## Test

Confirm you are set up correctly, by running:

```console
python application.py
```

You should see a list of your Okta applications.