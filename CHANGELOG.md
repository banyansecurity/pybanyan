# PyBanyan Change History

## 0.27.0

 * support for autodiscovering cloud resources

## 0.26.0

 * add `source_cidrs` list to `exempted_paths` struct in service model
 * add `is_deleted` flag to users and devices

## 0.25.0

 * Handle invalid values for netagent LastActivityAt timestamp

## 0.24.0

* Export policy attachments when exporting services

## 0.23.0

* add support for Kubernetes audit events

## 0.22.0

* make AWS library dependencies optional

## 0.21.0

* use `banyan.conf` if environment variables `BANYAN_REFRESH_TOKEN` and `BANYAN_API_URL` are not set

## 0.20.0

* send partial API results in progress callbacks

## 0.19.0

* add `-k` CLI flag to skip TLS verification (needed for `gcstage.banyanops.com`)

## 0.18.3

* pass params through API list() method

## 0.18.2

* trapped errors in progress callbacks

## 0.18.1

* add progress callbacks to new list methods in event_v2

## 0.18.0

* added count method to event_v2 object

## 0.17.2

* Remove testing code that imported ujson module

## 0.17.1

* Fix TypeError if no params are specified in API call

## 0.17.0

* Replace event paging model with time index based queries

## 0.16.0

* Add progress callback for long paging requests

## 0.15.0

* allow for inconsistent timestamps in event data
* implement paging for events v2 API
* fix broken callable support in API base class
* more parser tests for events

## 0.14.0

* more updates to events model
* added filter to remove null fields in JSON output
* Pythonified field names in EventV2TypeCount

## 0.13.0

* updated events model to latest v2 API

## 0.12.1

* added new dependencies to setup.py

## 0.12.0

* changed versioning scheme
* added CUSTOM service type

## 0.0.11

* added support for exporting roles, policies, and services via `banyan export` command
* added support for testing services from an Access Tier via `banyan service test` command

## 0.0.10

* added support for retrieving audit logs via `banyan audit` command

## 0.0.9

* added support for new Kubernetes service type
* replaced string constants with enums in roles/templates
* clean up PEP8/pyflakes/pylint issues

## 0.0.8

* fix for reporting users or devices with no last_login value

## 0.0.7

* removed Python 3.6 from compatibility list

## 0.0.6

* added support for listing security events
* fixed resource leak warnings in unit tests
* make pybanyan more resilient to unexpected fields in API responses
* use paging only on endpoints

## 0.0.5

* support both USER_WEB and WEB_USER style templates in services
* turn off strict schema validation in Marshmallow (by excluding unknown fields)
* only request paging on endpoints that support it

## 0.0.3

* Version bump to fix TravisCI weirdness.

## 0.0.2

* Added support for paging on devices and endusers API endpoints.

## 0.0.1

* Initial release.
