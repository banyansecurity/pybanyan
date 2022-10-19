<a name="__pageTop"></a>
# openapi_client.apis.tags.trustscore_integration_api.TrustscoreIntegrationApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_integration_crowdstrike_post**](#v2_integration_crowdstrike_post) | **post** /v2/integration/crowdstrike |  POST to create a new Crowdstrike integration
[**v2_integration_crowdstrike_put**](#v2_integration_crowdstrike_put) | **put** /v2/integration/crowdstrike |  PUT to update an existing Crowdstrike integration
[**v2_integration_delete**](#v2_integration_delete) | **delete** /v2/integration |  DELETE to remove an integration
[**v2_integration_device_identity_command_delete**](#v2_integration_device_identity_command_delete) | **delete** /v2/integration/device_identity_command |  DELETE to remove an integration device-identity command
[**v2_integration_device_identity_command_get**](#v2_integration_device_identity_command_get) | **get** /v2/integration/device_identity_command |  GET integration device-identity commands
[**v2_integration_device_identity_command_post**](#v2_integration_device_identity_command_post) | **post** /v2/integration/device_identity_command |  POST to create/register a new integration device-identity command
[**v2_integration_device_identity_command_put**](#v2_integration_device_identity_command_put) | **put** /v2/integration/device_identity_command |  PUT to update an integration device-identity command
[**v2_integration_get**](#v2_integration_get) | **get** /v2/integration |  GET to retrieve the details of integrations
[**v2_integration_partner_get**](#v2_integration_partner_get) | **get** /v2/integration/partner |  GET the list of supported Integration partners
[**v2_integration_post**](#v2_integration_post) | **post** /v2/integration |  POST to create/register a new integration
[**v2_integration_put**](#v2_integration_put) | **put** /v2/integration |  PUT to create/register a new integration
[**v2_integration_signal_delete**](#v2_integration_signal_delete) | **delete** /v2/integration/signal |  DELETE to remove an integration signal from an existing integration
[**v2_integration_signal_get**](#v2_integration_signal_get) | **get** /v2/integration/signal |  GET integration signal
[**v2_integration_signal_post**](#v2_integration_signal_post) | **post** /v2/integration/signal |  POST to associate a new integration signal with an existing integration
[**v2_integration_signal_put**](#v2_integration_signal_put) | **put** /v2/integration/signal |  PUT to update an integration signal with an existing integration
[**v2_integration_sync_config_get**](#v2_integration_sync_config_get) | **get** /v2/integration/sync_config |  GET the background/bulk sync config for an integration
[**v2_integration_sync_config_post**](#v2_integration_sync_config_post) | **post** /v2/integration/sync_config |  POST to configure the background/bulk sync for an integration
[**v2_integration_sync_config_put**](#v2_integration_sync_config_put) | **put** /v2/integration/sync_config |  PUT to update the sync config of an integration
[**v2_integration_sync_stats_device_csv_get**](#v2_integration_sync_stats_device_csv_get) | **get** /v2/integration/sync_stats/device_csv |  Get the integration sync stats in CSV format
[**v2_integration_sync_stats_get**](#v2_integration_sync_stats_get) | **get** /v2/integration/sync_stats |  GET to retrieve the sync stats details of an integration
[**v2_integration_test_credentials_crowdstrike_post**](#v2_integration_test_credentials_crowdstrike_post) | **post** /v2/integration/test_credentials/crowdstrike |  POST to test Crowdstrike credentials
[**v2_integration_test_credentials_get**](#v2_integration_test_credentials_get) | **get** /v2/integration/test_credentials |  GET to test an integration&#x27;s credentials

# **v2_integration_crowdstrike_post**
<a name="v2_integration_crowdstrike_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_crowdstrike_post(any_type)

 POST to create a new Crowdstrike integration

Submit properties for a new Crowdstrike integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        name="Crowdstrike1",
        description="Test EDR",
        id="<tenant ID>",
        secret="<tenant secret>",
        signals=[
            dict(
                name="zta.score",
                signal_min_threshold=75,
            )
        ],
        target_platforms="[\"macos\", \"windows\", \"linux\"]",
        base_url="https://api.crowdstrike.com",
    )
    try:
        #  POST to create a new Crowdstrike integration
        api_response = api_instance.v2_integration_crowdstrike_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_crowdstrike_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        name="Crowdstrike1",
        description="Test EDR",
        id="<tenant ID>",
        secret="<tenant secret>",
        signals=[
            dict(
                name="zta.score",
                signal_min_threshold=75,
            )
        ],
        target_platforms="[\"macos\", \"windows\", \"linux\"]",
        base_url="https://api.crowdstrike.com",
    )
    try:
        #  POST to create a new Crowdstrike integration
        api_response = api_instance.v2_integration_crowdstrike_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_crowdstrike_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**secret** | str,  | str,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
**target_platforms** | str,  | str,  |  | [optional] 
**base_url** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# signals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_crowdstrike_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_crowdstrike_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_crowdstrike_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_crowdstrike_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_crowdstrike_post.ApiResponseFor500) | Internal Server Error

#### v2_integration_crowdstrike_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_endpoint** | str,  | str,  |  | [optional] 
**authentication_type** | str,  | str,  |  | [optional] 
**authentication_endpoint** | str,  | str,  |  | [optional] 
**username** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**api_key** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**last_updated_by** | str,  | str,  |  | [optional] 
**integration_partner** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
**[device_identity_commands](#device_identity_commands)** | list, tuple,  | tuple,  |  | [optional] 
**[target_platforms](#target_platforms)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# signals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_identity_commands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# target_platforms

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_crowdstrike_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_crowdstrike_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_crowdstrike_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_crowdstrike_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_crowdstrike_put**
<a name="v2_integration_crowdstrike_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_crowdstrike_put(any_type)

 PUT to update an existing Crowdstrike integration

Update the details of an existing Crowdstrike integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        name="Crowdstrike2",
        description="Test EDR",
        id="<tenant ID>",
        secret="<tenant secret>",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        target_platforms="[\"macos\", \"windows\", \"linux\"]",
    )
    try:
        #  PUT to update an existing Crowdstrike integration
        api_response = api_instance.v2_integration_crowdstrike_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_crowdstrike_put: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        name="Crowdstrike2",
        description="Test EDR",
        id="<tenant ID>",
        secret="<tenant secret>",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        target_platforms="[\"macos\", \"windows\", \"linux\"]",
    )
    try:
        #  PUT to update an existing Crowdstrike integration
        api_response = api_instance.v2_integration_crowdstrike_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_crowdstrike_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**secret** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**target_platforms** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_crowdstrike_put.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_crowdstrike_put.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_crowdstrike_put.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_crowdstrike_put.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_crowdstrike_put.ApiResponseFor500) | Internal Server Error

#### v2_integration_crowdstrike_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_endpoint** | str,  | str,  |  | [optional] 
**authentication_type** | str,  | str,  |  | [optional] 
**authentication_endpoint** | str,  | str,  |  | [optional] 
**username** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**api_key** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**last_updated_by** | str,  | str,  |  | [optional] 
**integration_partner** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# signals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[device_identity_commands](#device_identity_commands)** | list, tuple,  | tuple,  |  | [optional] 
**[target_platforms](#target_platforms)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_identity_commands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# target_platforms

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_crowdstrike_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_crowdstrike_put.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_crowdstrike_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_crowdstrike_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_delete**
<a name="v2_integration_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_delete(any_type)

 DELETE to remove an integration

DELETE an integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
        name="FakeEDR2",
        type="EDR",
        active=1,
        api_endpoint="https",
        authentication_type="OAuth2",
        authentication_endpoint="https",
        username="<tenant id>",
        password="<tenant secret>",
        api_key="",
        description="EDR integration",
        created_by="jayanth@banyanops.com",
        last_updated_by="jayanth@banyanops.com",
        integration_partner="crowdstrike",
        created_at=1648152665096160800,
        updated_at=1648513348392427000,
        signals=[
            dict(
                id="a0ecb9c7-968e-483f-ab4b-fa3762de35ba",
                org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
                integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
                name="zta.score",
                type="integer",
                signal_min_threshold=75,
                signal_value_match="",
                signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
                signal_not_satisfied_trustlevel="AlwaysDeny",
                active=1,
                windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                created_at=1648152665098241800,
                updated_at=1648513348393724700,
            )
        ],
        device_identity_commands=[
            dict(
                id="659ce4b7-25da-487e-9186-a2bfbf1a0e2f",
                org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
                integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
                platform="macos",
                version="6.0",
                command="sudo /Applications/Falcon.app/Contents/Resources/falconctl stats | grep agentID",
                utility_signature_data="Authority=Developer ID Application",
                utility_signature_command="codesign -dv --verbose=4 /Applications/Falcon.app 2>&1 | grep -e 'Developer ID Application'",
                created_at=1648152665106748400,
                updated_at=1648513348394443000,
            )
        ],
    )
    try:
        #  DELETE to remove an integration
        api_response = api_instance.v2_integration_delete(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_delete: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
        name="FakeEDR2",
        type="EDR",
        active=1,
        api_endpoint="https",
        authentication_type="OAuth2",
        authentication_endpoint="https",
        username="<tenant id>",
        password="<tenant secret>",
        api_key="",
        description="EDR integration",
        created_by="jayanth@banyanops.com",
        last_updated_by="jayanth@banyanops.com",
        integration_partner="crowdstrike",
        created_at=1648152665096160800,
        updated_at=1648513348392427000,
        signals=[
            dict(
                id="a0ecb9c7-968e-483f-ab4b-fa3762de35ba",
                org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
                integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
                name="zta.score",
                type="integer",
                signal_min_threshold=75,
                signal_value_match="",
                signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
                signal_not_satisfied_trustlevel="AlwaysDeny",
                active=1,
                windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                created_at=1648152665098241800,
                updated_at=1648513348393724700,
            )
        ],
        device_identity_commands=[
            dict(
                id="659ce4b7-25da-487e-9186-a2bfbf1a0e2f",
                org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
                integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
                platform="macos",
                version="6.0",
                command="sudo /Applications/Falcon.app/Contents/Resources/falconctl stats | grep agentID",
                utility_signature_data="Authority=Developer ID Application",
                utility_signature_command="codesign -dv --verbose=4 /Applications/Falcon.app 2>&1 | grep -e 'Developer ID Application'",
                created_at=1648152665106748400,
                updated_at=1648513348394443000,
            )
        ],
    )
    try:
        #  DELETE to remove an integration
        api_response = api_instance.v2_integration_delete(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_endpoint** | str,  | str,  |  | [optional] 
**authentication_type** | str,  | str,  |  | [optional] 
**authentication_endpoint** | str,  | str,  |  | [optional] 
**username** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**api_key** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**last_updated_by** | str,  | str,  |  | [optional] 
**integration_partner** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
**[device_identity_commands](#device_identity_commands)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# signals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_identity_commands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**utility_signature_data** | str,  | str,  |  | [optional] 
**utility_signature_command** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_delete.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_delete.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_delete.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_delete.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_delete.ApiResponseFor500) | Internal Server Error

#### v2_integration_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**data** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_device_identity_command_delete**
<a name="v2_integration_device_identity_command_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_device_identity_command_delete(any_type)

 DELETE to remove an integration device-identity command

Remove the details of an integration device identity command

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        id="e4023744-6621-45ae-92be-d07d9ff192c4",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        platform="macos",
        version="5.36",
        command="sudo /Library/CS/falconctl stats | grep agentID",
        utility_signature_data="",
        utility_signature_command="",
    )
    try:
        #  DELETE to remove an integration device-identity command
        api_response = api_instance.v2_integration_device_identity_command_delete(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_device_identity_command_delete: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        id="e4023744-6621-45ae-92be-d07d9ff192c4",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        platform="macos",
        version="5.36",
        command="sudo /Library/CS/falconctl stats | grep agentID",
        utility_signature_data="",
        utility_signature_command="",
    )
    try:
        #  DELETE to remove an integration device-identity command
        api_response = api_instance.v2_integration_device_identity_command_delete(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_device_identity_command_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**utility_signature_data** | str,  | str,  |  | [optional] 
**utility_signature_command** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_device_identity_command_delete.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_device_identity_command_delete.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_device_identity_command_delete.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_device_identity_command_delete.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_device_identity_command_delete.ApiResponseFor500) | Internal Server Error

#### v2_integration_device_identity_command_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**data** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_device_identity_command_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_device_identity_command_get**
<a name="v2_integration_device_identity_command_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_device_identity_command_get()

 GET integration device-identity commands

Update the details of an integration device identity commands for all active integrations or a specific integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only optional values
    query_params = {
        'integration_id': "integration_id_example",
        'platform': "platform_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET integration device-identity commands
        api_response = api_instance.v2_integration_device_identity_command_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_device_identity_command_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
integration_id | IntegrationIdSchema | | optional
platform | PlatformSchema | | optional


# IntegrationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PlatformSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_device_identity_command_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_device_identity_command_get.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_device_identity_command_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_device_identity_command_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_device_identity_command_get.ApiResponseFor500) | Internal Server Error

#### v2_integration_device_identity_command_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**partner** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_device_identity_command_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_device_identity_command_post**
<a name="v2_integration_device_identity_command_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_device_identity_command_post(any_type)

 POST to create/register a new integration device-identity command

Submit the details of an integration device identity command to restapiserver

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        platform="macos",
        version="5.36",
        command="sudo /Library/CS/falconctl stats | grep agentID",
        utility_signature_data="",
        utility_signature_command="",
    )
    try:
        #  POST to create/register a new integration device-identity command
        api_response = api_instance.v2_integration_device_identity_command_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_device_identity_command_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        platform="macos",
        version="5.36",
        command="sudo /Library/CS/falconctl stats | grep agentID",
        utility_signature_data="",
        utility_signature_command="",
    )
    try:
        #  POST to create/register a new integration device-identity command
        api_response = api_instance.v2_integration_device_identity_command_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_device_identity_command_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**utility_signature_data** | str,  | str,  |  | [optional] 
**utility_signature_command** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_device_identity_command_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_device_identity_command_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_device_identity_command_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_device_identity_command_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_device_identity_command_post.ApiResponseFor500) | Internal Server Error

#### v2_integration_device_identity_command_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**utility_signature_data** | str,  | str,  |  | [optional] 
**utility_signature_command** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_device_identity_command_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_device_identity_command_put**
<a name="v2_integration_device_identity_command_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_device_identity_command_put(any_type)

 PUT to update an integration device-identity command

Update the details of an integration device identity command

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        id="e4023744-6621-45ae-92be-d07d9ff192c4",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        platform="macos",
        version="5.36",
        command="sudo /Library/CS/falconctl stats | grep agentID",
        utility_signature_data="",
        utility_signature_command="",
    )
    try:
        #  PUT to update an integration device-identity command
        api_response = api_instance.v2_integration_device_identity_command_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_device_identity_command_put: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        id="e4023744-6621-45ae-92be-d07d9ff192c4",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        platform="macos",
        version="5.36",
        command="sudo /Library/CS/falconctl stats | grep agentID",
        utility_signature_data="",
        utility_signature_command="",
    )
    try:
        #  PUT to update an integration device-identity command
        api_response = api_instance.v2_integration_device_identity_command_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_device_identity_command_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**utility_signature_data** | str,  | str,  |  | [optional] 
**utility_signature_command** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_device_identity_command_put.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_device_identity_command_put.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_device_identity_command_put.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_device_identity_command_put.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_device_identity_command_put.ApiResponseFor500) | Internal Server Error

#### v2_integration_device_identity_command_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**utility_signature_data** | str,  | str,  |  | [optional] 
**utility_signature_command** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_device_identity_command_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_put.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_device_identity_command_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_get**
<a name="v2_integration_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_get()

 GET to retrieve the details of integrations

Get the credential and config details of an integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only optional values
    query_params = {
        'integration_id': "integration_id_example",
        'active': True,
        'name': "name_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET to retrieve the details of integrations
        api_response = api_instance.v2_integration_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
integration_id | IntegrationIdSchema | | optional
active | ActiveSchema | | optional
name | NameSchema | | optional


# IntegrationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ActiveSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_get.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_get.ApiResponseFor500) | Internal Server Error

#### v2_integration_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_endpoint** | str,  | str,  |  | [optional] 
**authentication_type** | str,  | str,  |  | [optional] 
**authentication_endpoint** | str,  | str,  |  | [optional] 
**username** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**api_key** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**last_updated_by** | str,  | str,  |  | [optional] 
**integration_partner** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
**[device_identity_commands](#device_identity_commands)** | list, tuple,  | tuple,  |  | [optional] 
**[target_platforms](#target_platforms)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# signals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_identity_commands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**command** | str,  | str,  |  | [optional] 
**utility_signature_data** | str,  | str,  |  | [optional] 
**utility_signature_command** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# target_platforms

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_partner_get**
<a name="v2_integration_partner_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_partner_get()

 GET the list of supported Integration partners

Get the partner names plus metadata for the UI wizard creation flow

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET the list of supported Integration partners
        api_response = api_instance.v2_integration_partner_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_partner_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_partner_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_partner_get.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_partner_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_partner_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_partner_get.ApiResponseFor500) | Internal Server Error

#### v2_integration_partner_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**inputs** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_partner_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_partner_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_partner_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_partner_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_post**
<a name="v2_integration_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_post(any_type)

 POST to create/register a new integration

Submit the credential and config details of an integration to restapiserver

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        name="FakeEDR",
        type="EDR",
        active=1,
        api_endpoint="https",
        authentication_type="OAuth2",
        authentication_endpoint="https",
        username="<tenant id>",
        password="<tenant secret>",
        api_key="",
        description="EDR integration",
        integration_partner="crowdstrike",
        signals=[
            dict(
                name="zta.score",
                type="integer",
                signal_min_threshold=75,
                signal_value_match="",
                signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
                signal_not_satisfied_trustlevel="AlwaysDeny",
                active=1,
                windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
            )
        ],
        device_identity_commands=[
            dict(
                platform="macos",
                version="6.0",
            )
        ],
        target_platforms=[
            dict(
                platform="windows",
            )
        ],
    )
    try:
        #  POST to create/register a new integration
        api_response = api_instance.v2_integration_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        name="FakeEDR",
        type="EDR",
        active=1,
        api_endpoint="https",
        authentication_type="OAuth2",
        authentication_endpoint="https",
        username="<tenant id>",
        password="<tenant secret>",
        api_key="",
        description="EDR integration",
        integration_partner="crowdstrike",
        signals=[
            dict(
                name="zta.score",
                type="integer",
                signal_min_threshold=75,
                signal_value_match="",
                signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
                signal_not_satisfied_trustlevel="AlwaysDeny",
                active=1,
                windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
            )
        ],
        device_identity_commands=[
            dict(
                platform="macos",
                version="6.0",
            )
        ],
        target_platforms=[
            dict(
                platform="windows",
            )
        ],
    )
    try:
        #  POST to create/register a new integration
        api_response = api_instance.v2_integration_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_endpoint** | str,  | str,  |  | [optional] 
**authentication_type** | str,  | str,  |  | [optional] 
**authentication_endpoint** | str,  | str,  |  | [optional] 
**username** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**api_key** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**integration_partner** | str,  | str,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
**[device_identity_commands](#device_identity_commands)** | list, tuple,  | tuple,  |  | [optional] 
**[target_platforms](#target_platforms)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# signals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_identity_commands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# target_platforms

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**platform** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_post.ApiResponseFor500) | Internal Server Error

#### v2_integration_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_endpoint** | str,  | str,  |  | [optional] 
**authentication_type** | str,  | str,  |  | [optional] 
**authentication_endpoint** | str,  | str,  |  | [optional] 
**username** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**api_key** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**integration_partner** | str,  | str,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
**[device_identity_commands](#device_identity_commands)** | list, tuple,  | tuple,  |  | [optional] 
**[target_platforms](#target_platforms)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# signals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_identity_commands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# target_platforms

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**platform** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_put**
<a name="v2_integration_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_put(any_type)

 PUT to create/register a new integration

Update the credential and config details of an integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
        name="FakeEDR2",
        type="EDR",
        active=1,
        api_endpoint="https",
        authentication_type="OAuth2",
        authentication_endpoint="https",
        username="<tenant id>",
        password="<tenant secret>",
        api_key="",
        description="EDR integration",
        created_by="jayanth@banyanops.com",
        last_updated_by="jayanth@banyanops.com",
        integration_partner="crowdstrike",
        created_at=1648152665096160800,
        updated_at=1648513348392427000,
        signals=[
            dict(
                id="a0ecb9c7-968e-483f-ab4b-fa3762de35ba",
                org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
                integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
                name="zta.score",
                type="integer",
                signal_min_threshold=75,
                signal_value_match="",
                signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
                signal_not_satisfied_trustlevel="AlwaysDeny",
                active=1,
                windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                created_at=1648152665098241800,
                updated_at=1648513348393724700,
            )
        ],
        device_identity_commands=[
            dict(
                id="659ce4b7-25da-487e-9186-a2bfbf1a0e2f",
                org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
                integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
                platform="macos",
                version="6.0",
                partner="crowdstrike",
                created_at=1648152665106748400,
                updated_at=1648513348394443000,
            )
        ],
        target_platforms=[
            dict(
                id="702028f0-b14a-40ae-a3fd-b2e07afe493c",
                org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
                integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
                platform="windows",
                created_at=1654719498834454300,
                updated_at=1654719498834454300,
            )
        ],
    )
    try:
        #  PUT to create/register a new integration
        api_response = api_instance.v2_integration_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_put: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
        name="FakeEDR2",
        type="EDR",
        active=1,
        api_endpoint="https",
        authentication_type="OAuth2",
        authentication_endpoint="https",
        username="<tenant id>",
        password="<tenant secret>",
        api_key="",
        description="EDR integration",
        created_by="jayanth@banyanops.com",
        last_updated_by="jayanth@banyanops.com",
        integration_partner="crowdstrike",
        created_at=1648152665096160800,
        updated_at=1648513348392427000,
        signals=[
            dict(
                id="a0ecb9c7-968e-483f-ab4b-fa3762de35ba",
                org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
                integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
                name="zta.score",
                type="integer",
                signal_min_threshold=75,
                signal_value_match="",
                signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
                signal_not_satisfied_trustlevel="AlwaysDeny",
                active=1,
                windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
                created_at=1648152665098241800,
                updated_at=1648513348393724700,
            )
        ],
        device_identity_commands=[
            dict(
                id="659ce4b7-25da-487e-9186-a2bfbf1a0e2f",
                org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
                integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
                platform="macos",
                version="6.0",
                partner="crowdstrike",
                created_at=1648152665106748400,
                updated_at=1648513348394443000,
            )
        ],
        target_platforms=[
            dict(
                id="702028f0-b14a-40ae-a3fd-b2e07afe493c",
                org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
                integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
                platform="windows",
                created_at=1654719498834454300,
                updated_at=1654719498834454300,
            )
        ],
    )
    try:
        #  PUT to create/register a new integration
        api_response = api_instance.v2_integration_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_endpoint** | str,  | str,  |  | [optional] 
**authentication_type** | str,  | str,  |  | [optional] 
**authentication_endpoint** | str,  | str,  |  | [optional] 
**username** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**api_key** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**last_updated_by** | str,  | str,  |  | [optional] 
**integration_partner** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
**[device_identity_commands](#device_identity_commands)** | list, tuple,  | tuple,  |  | [optional] 
**[target_platforms](#target_platforms)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# signals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_identity_commands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**partner** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# target_platforms

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_put.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_put.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_put.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_put.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_put.ApiResponseFor500) | Internal Server Error

#### v2_integration_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_endpoint** | str,  | str,  |  | [optional] 
**authentication_type** | str,  | str,  |  | [optional] 
**authentication_endpoint** | str,  | str,  |  | [optional] 
**username** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**api_key** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**last_updated_by** | str,  | str,  |  | [optional] 
**integration_partner** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
**[device_identity_commands](#device_identity_commands)** | list, tuple,  | tuple,  |  | [optional] 
**[target_platforms](#target_platforms)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# signals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_identity_commands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**partner** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# target_platforms

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_put.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_signal_delete**
<a name="v2_integration_signal_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_signal_delete(any_type)

 DELETE to remove an integration signal from an existing integration

Delete an existing integration signal

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        id="a0ecb9c7-968e-483f-ab4b-fa3762de35ba",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        name="zta.score",
        type="integer",
        signal_min_threshold=65,
        signal_value_match="",
        signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
        signal_not_satisfied_trustlevel="AlwaysDeny",
        active=1,
        windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
    )
    try:
        #  DELETE to remove an integration signal from an existing integration
        api_response = api_instance.v2_integration_signal_delete(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_signal_delete: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        id="a0ecb9c7-968e-483f-ab4b-fa3762de35ba",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        name="zta.score",
        type="integer",
        signal_min_threshold=65,
        signal_value_match="",
        signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
        signal_not_satisfied_trustlevel="AlwaysDeny",
        active=1,
        windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
    )
    try:
        #  DELETE to remove an integration signal from an existing integration
        api_response = api_instance.v2_integration_signal_delete(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_signal_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_signal_delete.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_signal_delete.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_signal_delete.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_signal_delete.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_signal_delete.ApiResponseFor500) | Internal Server Error

#### v2_integration_signal_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**data** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_signal_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_signal_get**
<a name="v2_integration_signal_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_signal_get()

 GET integration signal

Get the signals for a specific integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only optional values
    query_params = {
        'integration_id': "integration_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET integration signal
        api_response = api_instance.v2_integration_signal_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_signal_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
integration_id | IntegrationIdSchema | | optional


# IntegrationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_signal_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_signal_get.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_signal_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_signal_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_signal_get.ApiResponseFor500) | Internal Server Error

#### v2_integration_signal_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_signal_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_signal_post**
<a name="v2_integration_signal_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_signal_post(any_type)

 POST to associate a new integration signal with an existing integration

Submit the new signal

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        name="zta.score",
        type="integer",
        signal_min_threshold=75,
        signal_value_match="",
        signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
        signal_not_satisfied_trustlevel="AlwaysDeny",
        active=1,
        windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
    )
    try:
        #  POST to associate a new integration signal with an existing integration
        api_response = api_instance.v2_integration_signal_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_signal_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        name="zta.score",
        type="integer",
        signal_min_threshold=75,
        signal_value_match="",
        signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
        signal_not_satisfied_trustlevel="AlwaysDeny",
        active=1,
        windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
    )
    try:
        #  POST to associate a new integration signal with an existing integration
        api_response = api_instance.v2_integration_signal_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_signal_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_signal_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_signal_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_signal_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_signal_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_signal_post.ApiResponseFor500) | Internal Server Error

#### v2_integration_signal_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_signal_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_signal_put**
<a name="v2_integration_signal_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_signal_put(any_type)

 PUT to update an integration signal with an existing integration

Modify an existing integration signal

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        id="a0ecb9c7-968e-483f-ab4b-fa3762de35ba",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        name="zta.score",
        type="integer",
        signal_min_threshold=65,
        signal_value_match="",
        signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
        signal_not_satisfied_trustlevel="AlwaysDeny",
        active=1,
        windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
    )
    try:
        #  PUT to update an integration signal with an existing integration
        api_response = api_instance.v2_integration_signal_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_signal_put: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        id="a0ecb9c7-968e-483f-ab4b-fa3762de35ba",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        name="zta.score",
        type="integer",
        signal_min_threshold=65,
        signal_value_match="",
        signal_not_satisfied_message="Your device does not satisfy your organization's Crowdstrike policy",
        signal_not_satisfied_trustlevel="AlwaysDeny",
        active=1,
        windows_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        macos_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        linux_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        ios_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
        android_remediation_description="Crowdstrike has evaluated this device's ZTA score below the threshold required. Please reach out to support.",
    )
    try:
        #  PUT to update an integration signal with an existing integration
        api_response = api_instance.v2_integration_signal_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_signal_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_signal_put.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_signal_put.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_signal_put.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_signal_put.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_signal_put.ApiResponseFor500) | Internal Server Error

#### v2_integration_signal_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**signal_min_threshold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**signal_value_match** | str,  | str,  |  | [optional] 
**signal_not_satisfied_message** | str,  | str,  |  | [optional] 
**signal_not_satisfied_trustlevel** | str,  | str,  |  | [optional] 
**active** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**windows_remediation_description** | str,  | str,  |  | [optional] 
**macos_remediation_description** | str,  | str,  |  | [optional] 
**linux_remediation_description** | str,  | str,  |  | [optional] 
**ios_remediation_description** | str,  | str,  |  | [optional] 
**android_remediation_description** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_signal_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_put.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_signal_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_sync_config_get**
<a name="v2_integration_sync_config_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_sync_config_get()

 GET the background/bulk sync config for an integration

Get the bulk sync config for an integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET the background/bulk sync config for an integration
        api_response = api_instance.v2_integration_sync_config_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_sync_config_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_sync_config_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_sync_config_get.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_sync_config_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_sync_config_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_sync_config_get.ApiResponseFor500) | Internal Server Error

#### v2_integration_sync_config_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**sync_interval_secs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_timeout_secs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last_sync_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_sync_config_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_config_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_config_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_config_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_sync_config_post**
<a name="v2_integration_sync_config_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_sync_config_post(any_type)

 POST to configure the background/bulk sync for an integration

Submit the new configuration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        sync_interval_secs=1200,
        api_timeout_secs=30,
    )
    try:
        #  POST to configure the background/bulk sync for an integration
        api_response = api_instance.v2_integration_sync_config_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_sync_config_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        sync_interval_secs=1200,
        api_timeout_secs=30,
    )
    try:
        #  POST to configure the background/bulk sync for an integration
        api_response = api_instance.v2_integration_sync_config_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_sync_config_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**integration_id** | str,  | str,  |  | [optional] 
**sync_interval_secs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_timeout_secs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_sync_config_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_sync_config_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_sync_config_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_sync_config_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_sync_config_post.ApiResponseFor500) | Internal Server Error

#### v2_integration_sync_config_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[items](#items)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**sync_interval_secs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_timeout_secs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last_sync_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_sync_config_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_config_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_config_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_config_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_sync_config_put**
<a name="v2_integration_sync_config_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_sync_config_put(any_type)

 PUT to update the sync config of an integration

Modify the sync config of an integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        id="a0ecb9c7-968e-483f-ab4b-fa3762de35ba",
        org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        sync_interval_secs=2400,
        api_timeout_secs=30,
        last_sync_at=1648152665098241800,
        created_at=1648152665098241800,
        updated_at=1648513348393724700,
    )
    try:
        #  PUT to update the sync config of an integration
        api_response = api_instance.v2_integration_sync_config_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_sync_config_put: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        id="a0ecb9c7-968e-483f-ab4b-fa3762de35ba",
        org_id="1b556bde-5612-4208-9dde-2568f3f48c9b",
        integration_id="99e1ed20-81f3-4994-8491-4cede0ba2bad",
        sync_interval_secs=2400,
        api_timeout_secs=30,
        last_sync_at=1648152665098241800,
        created_at=1648152665098241800,
        updated_at=1648513348393724700,
    )
    try:
        #  PUT to update the sync config of an integration
        api_response = api_instance.v2_integration_sync_config_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_sync_config_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**sync_interval_secs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_timeout_secs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last_sync_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_sync_config_put.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_sync_config_put.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_sync_config_put.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_sync_config_put.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_sync_config_put.ApiResponseFor500) | Internal Server Error

#### v2_integration_sync_config_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**sync_interval_secs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_timeout_secs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last_sync_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_sync_config_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_config_put.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_config_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_config_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_sync_stats_device_csv_get**
<a name="v2_integration_sync_stats_device_csv_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_sync_stats_device_csv_get()

 Get the integration sync stats in CSV format

Fetches integration sync stats information (such as device attributes, integration signals, sync status) for the devices in the organization as CSV File.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Get the integration sync stats in CSV format
        api_response = api_instance.v2_integration_sync_stats_device_csv_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_sync_stats_device_csv_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('text/csv', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_sync_stats_device_csv_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_sync_stats_device_csv_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v2_integration_sync_stats_device_csv_get.ApiResponseFor500) | Internal Server Error

#### v2_integration_sync_stats_device_csv_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextCsv, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextCsv

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Integration Sync Status** | str,  | str,  |  | [optional] 
**Device Name** | str,  | str,  |  | [optional] 
**Users** | str,  | str,  |  | [optional] 
**Trustscore** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last login** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Device Status** | str,  | str,  |  | [optional] 
**Serial Number** | str,  | str,  |  | [optional] 
**Platform** | str,  | str,  |  | [optional] 
**Architecture** | str,  | str,  |  | [optional] 
**OS** | str,  | str,  |  | [optional] 
**&lt;signal1 name&gt;** | str,  | str,  |  | [optional] 
**&lt;signal2 name&gt;** | str,  | str,  |  | [optional] 
**&lt;signalN name&gt;** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_sync_stats_device_csv_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_stats_device_csv_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_sync_stats_get**
<a name="v2_integration_sync_stats_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_sync_stats_get()

 GET to retrieve the sync stats details of an integration

Get the sync stats of an integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only optional values
    query_params = {
        'integration_id': "integration_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  GET to retrieve the sync stats details of an integration
        api_response = api_instance.v2_integration_sync_stats_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_sync_stats_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
integration_id | IntegrationIdSchema | | optional


# IntegrationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
ContentType | ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_sync_stats_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_sync_stats_get.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_sync_stats_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_sync_stats_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_sync_stats_get.ApiResponseFor500) | Internal Server Error

#### v2_integration_sync_stats_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**num_devices_synced** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**num_devices_passing_all_signals** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**num_devices_passing_some_signals** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**num_devices_failing_all_signals** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**last_sync_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_sync_stats_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_stats_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_stats_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sync_stats_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_test_credentials_crowdstrike_post**
<a name="v2_integration_test_credentials_crowdstrike_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_test_credentials_crowdstrike_post(any_type)

 POST to test Crowdstrike credentials

Submit tenant credentials

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        id="<tenant ID>",
        secret="<tenant secret>",
        base_url="https://api.crowdstrike.com",
    )
    try:
        #  POST to test Crowdstrike credentials
        api_response = api_instance.v2_integration_test_credentials_crowdstrike_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_test_credentials_crowdstrike_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        id="<tenant ID>",
        secret="<tenant secret>",
        base_url="https://api.crowdstrike.com",
    )
    try:
        #  POST to test Crowdstrike credentials
        api_response = api_instance.v2_integration_test_credentials_crowdstrike_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_test_credentials_crowdstrike_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**secret** | str,  | str,  |  | [optional] 
**base_url** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_test_credentials_crowdstrike_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_test_credentials_crowdstrike_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_test_credentials_crowdstrike_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_test_credentials_crowdstrike_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_test_credentials_crowdstrike_post.ApiResponseFor500) | Internal Server Error

#### v2_integration_test_credentials_crowdstrike_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**api_response_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_response_message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_test_credentials_crowdstrike_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_test_credentials_crowdstrike_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_test_credentials_crowdstrike_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_test_credentials_crowdstrike_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_integration_test_credentials_get**
<a name="v2_integration_test_credentials_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_test_credentials_get()

 GET to test an integration's credentials

Test the credentials of an integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import trustscore_integration_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trustscore_integration_api.TrustscoreIntegrationApi(api_client)

    # example passing only optional values
    query_params = {
        'integration_id': "integration_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  GET to test an integration's credentials
        api_response = api_instance.v2_integration_test_credentials_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TrustscoreIntegrationApi->v2_integration_test_credentials_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
integration_id | IntegrationIdSchema | | optional


# IntegrationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
ContentType | ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_integration_test_credentials_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_test_credentials_get.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_test_credentials_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_test_credentials_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_test_credentials_get.ApiResponseFor500) | Internal Server Error

#### v2_integration_test_credentials_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**api_response_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_response_message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_test_credentials_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_test_credentials_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_test_credentials_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_test_credentials_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

