# PyBanyan Change History

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
