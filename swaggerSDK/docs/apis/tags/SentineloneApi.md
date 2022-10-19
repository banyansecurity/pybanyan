<a name="__pageTop"></a>
# openapi_client.apis.tags.sentinelone_api.SentineloneApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_integration_sentinelone_post**](#v2_integration_sentinelone_post) | **post** /v2/integration/sentinelone |  POST to create a new SentinelOne integration

# **v2_integration_sentinelone_post**
<a name="v2_integration_sentinelone_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_integration_sentinelone_post(any_type)

 POST to create a new SentinelOne integration

Submit properties for a new SentinelOne integration

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import sentinelone_api
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
    api_instance = sentinelone_api.SentineloneApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        name="UI-S1-EDR",
        description="UI-S1-EDR",
        partner_url="https://usea1-partners.sentinelone.net",
        api_key="dZClm5o9GfGEe9B29n5VBcn9DLv7hgwdUsMe5YErgiRpsZZgs5AwKH4BjlctKgRGb1mJbdpv57txWJbS",
        signals=[
            dict(
                name="s1.registeredWith",
                signal_min_threshold=0,
                target_platforms=[
                    "linux"
                ],
            )
        ],
    )
    try:
        #  POST to create a new SentinelOne integration
        api_response = api_instance.v2_integration_sentinelone_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SentineloneApi->v2_integration_sentinelone_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        name="UI-S1-EDR",
        description="UI-S1-EDR",
        partner_url="https://usea1-partners.sentinelone.net",
        api_key="dZClm5o9GfGEe9B29n5VBcn9DLv7hgwdUsMe5YErgiRpsZZgs5AwKH4BjlctKgRGb1mJbdpv57txWJbS",
        signals=[
            dict(
                name="s1.registeredWith",
                signal_min_threshold=0,
                target_platforms=[
                    "linux"
                ],
            )
        ],
    )
    try:
        #  POST to create a new SentinelOne integration
        api_response = api_instance.v2_integration_sentinelone_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SentineloneApi->v2_integration_sentinelone_post: %s\n" % e)
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
**partner_url** | str,  | str,  |  | [optional] 
**api_key** | str,  | str,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
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
**[target_platforms](#target_platforms)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# target_platforms

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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
200 | [ApiResponseFor200](#v2_integration_sentinelone_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_integration_sentinelone_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_integration_sentinelone_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_integration_sentinelone_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_integration_sentinelone_post.ApiResponseFor500) | Internal Server Error

#### v2_integration_sentinelone_post.ApiResponseFor200
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
**api_key_expiry** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[signals](#signals)** | list, tuple,  | tuple,  |  | [optional] 
**[device_identity_commands](#device_identity_commands)** | list, tuple,  | tuple,  |  | [optional] 
**last_batch_update** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**sync_status** | str,  | str,  |  | [optional] 
**target_platforms** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
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
**[target_platforms](#target_platforms)** | list, tuple,  | tuple,  |  | [optional] 
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
**integration_id** | str,  | str,  |  | [optional] 
**signal_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
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
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**partner** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_sentinelone_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

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
**data** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_integration_sentinelone_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sentinelone_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_integration_sentinelone_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

