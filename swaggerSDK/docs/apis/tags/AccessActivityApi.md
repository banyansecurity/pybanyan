<a name="__pageTop"></a>
# openapi_client.apis.tags.access_activity_api.AccessActivityApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_access_activity_get**](#v1_access_activity_get) | **get** /v1/access_activity |  Returns data for all access activities

# **v1_access_activity_get**
<a name="v1_access_activity_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] v1_access_activity_get()

 Returns data for all access activities

This is a comprehensive endpoint that returns all access activities filtered by services, users, devices.Note: We only lookup security events which are of eventtype access.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import access_activity_api
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
    api_instance = access_activity_api.AccessActivityApi(api_client)

    # example passing only optional values
    query_params = {
        'DeviceID': "DeviceID_example",
        'Email': "Email_example",
        'ServiceID': "ServiceID_example",
        'StartTime': "StartTime_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Returns data for all access activities
        api_response = api_instance.v1_access_activity_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccessActivityApi->v1_access_activity_get: %s\n" % e)
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
DeviceID | DeviceIDSchema | | optional
Email | EmailSchema | | optional
ServiceID | ServiceIDSchema | | optional
StartTime | StartTimeSchema | | optional


# DeviceIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServiceIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartTimeSchema

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
200 | [ApiResponseFor200](#v1_access_activity_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_access_activity_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v1_access_activity_get.ApiResponseFor500) | Internal Server Error

#### v1_access_activity_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

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
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**Name** | str,  | str,  |  | [optional] 
**Email** | str,  | str,  |  | [optional] 
**DeviceID** | str,  | str,  |  | [optional] 
**SerialNumber** | str,  | str,  |  | [optional] 
**Model** | str,  | str,  |  | [optional] 
**Roles** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastAuthorizedEvent](#LastAuthorizedEvent)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[LastUnauthorizedEvent](#LastUnauthorizedEvent)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastAuthorizedEvent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**EventType** | str,  | str,  |  | [optional] 
**EventAction** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**EventJSON** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUnauthorizedEvent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**EventType** | str,  | str,  |  | [optional] 
**EventAction** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**EventJSON** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_access_activity_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_access_activity_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

