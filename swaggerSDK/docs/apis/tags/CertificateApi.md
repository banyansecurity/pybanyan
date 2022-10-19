<a name="__pageTop"></a>
# openapi_client.apis.tags.certificate_api.CertificateApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_cert_update_post**](#v2_cert_update_post) | **post** /v2/cert_update |  POST to submit a cert update code to get the UPN to bake into a device certificate
[**v2_cert_update_prepare_post**](#v2_cert_update_prepare_post) | **post** /v2/cert_update/prepare |  POST to submit the UPN details to restapiserver so they can be retrieved later by the BanyanApp

# **v2_cert_update_post**
<a name="v2_cert_update_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_cert_update_post(any_type)

 POST to submit a cert update code to get the UPN to bake into a device certificate

Submit a cert update code to obtain the user principal name (UPN) sent by Trustprovider after a successful IdP login. Expected to be used by the BanyanApp.

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import certificate_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = certificate_api.CertificateApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        cert_update_code="update-me",
        serial_number="my-serial",
        csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICbjCCAVYCAQAwKTEnMCUGA1UEAwweTWFuYWdlZERldmljZS1CTk4tQzFNS1I0\nTEFEVFkzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzKijMkeHQ/ul\noEoJ9AuvPNslqk2xwiT9kW2TbAGze8iaBmCWL+I/soeiw3okS7LE9FFZ4Pn8H225\nH3qpZSOEorAdO1olKJmVqnUo2YIhMWk3ARtH+TI87PoJtGhT87LgLVHGpVr1L2qk\nakNoNH2/MZVlsUNX5Uvt9XZWXOcA5o1rMRhjVdUI5obj\noAJuRm1cmGOlqgPnWaUbN4Vvw\nZnylxMnjFXo6yLumfTlILMFvEouNTuP223HLjqhU1dAzk1lO9cdeN9QAvSbnksIy\nd4p9LuZ+0Hy3ExcJtbJueqfhp2pySf9oFa7sluSJgPQjM2U8f41zd7tcYFf6x/Er\n/rOjpkQjaO1RRIeJSYvQBlzliaEIKbOSA+uQqjTRj3Bv/w3IciXTjVZ7sMpylNVH\nlHk=\n-----END CERTIFICATE REQUEST-----",
    )
    try:
        #  POST to submit a cert update code to get the UPN to bake into a device certificate
        api_response = api_instance.v2_cert_update_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateApi->v2_cert_update_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        cert_update_code="update-me",
        serial_number="my-serial",
        csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICbjCCAVYCAQAwKTEnMCUGA1UEAwweTWFuYWdlZERldmljZS1CTk4tQzFNS1I0\nTEFEVFkzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzKijMkeHQ/ul\noEoJ9AuvPNslqk2xwiT9kW2TbAGze8iaBmCWL+I/soeiw3okS7LE9FFZ4Pn8H225\nH3qpZSOEorAdO1olKJmVqnUo2YIhMWk3ARtH+TI87PoJtGhT87LgLVHGpVr1L2qk\nakNoNH2/MZVlsUNX5Uvt9XZWXOcA5o1rMRhjVdUI5obj\noAJuRm1cmGOlqgPnWaUbN4Vvw\nZnylxMnjFXo6yLumfTlILMFvEouNTuP223HLjqhU1dAzk1lO9cdeN9QAvSbnksIy\nd4p9LuZ+0Hy3ExcJtbJueqfhp2pySf9oFa7sluSJgPQjM2U8f41zd7tcYFf6x/Er\n/rOjpkQjaO1RRIeJSYvQBlzliaEIKbOSA+uQqjTRj3Bv/w3IciXTjVZ7sMpylNVH\nlHk=\n-----END CERTIFICATE REQUEST-----",
    )
    try:
        #  POST to submit a cert update code to get the UPN to bake into a device certificate
        api_response = api_instance.v2_cert_update_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateApi->v2_cert_update_post: %s\n" % e)
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
**cert_update_code** | str,  | str,  |  | [optional] 
**serial_number** | str,  | str,  |  | [optional] 
**csr** | str,  | str,  |  | [optional] 
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
200 | [ApiResponseFor200](#v2_cert_update_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_cert_update_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_cert_update_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_cert_update_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_cert_update_post.ApiResponseFor500) | Internal Server Error

#### v2_cert_update_post.ApiResponseFor200
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
**principal_name** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_cert_update_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_cert_update_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_cert_update_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_cert_update_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_cert_update_prepare_post**
<a name="v2_cert_update_prepare_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_cert_update_prepare_post(any_type)

 POST to submit the UPN details to restapiserver so they can be retrieved later by the BanyanApp

Submit the UPN details to restapiserver after the user successfully authenticates at the IdP. Expected to be used by TrustProvider

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import certificate_api
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
    api_instance = certificate_api.CertificateApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        org_id="1",
        cert_update_code="update-me",
        serial_number="my-serial",
        principal_name="ariel@example.com",
    )
    try:
        #  POST to submit the UPN details to restapiserver so they can be retrieved later by the BanyanApp
        api_response = api_instance.v2_cert_update_prepare_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateApi->v2_cert_update_prepare_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        org_id="1",
        cert_update_code="update-me",
        serial_number="my-serial",
        principal_name="ariel@example.com",
    )
    try:
        #  POST to submit the UPN details to restapiserver so they can be retrieved later by the BanyanApp
        api_response = api_instance.v2_cert_update_prepare_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CertificateApi->v2_cert_update_prepare_post: %s\n" % e)
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
**org_id** | str,  | str,  |  | [optional] 
**cert_update_code** | str,  | str,  |  | [optional] 
**serial_number** | str,  | str,  |  | [optional] 
**principal_name** | str,  | str,  |  | [optional] 
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
200 | [ApiResponseFor200](#v2_cert_update_prepare_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_cert_update_prepare_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_cert_update_prepare_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_cert_update_prepare_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_cert_update_prepare_post.ApiResponseFor500) | Internal Server Error

#### v2_cert_update_prepare_post.ApiResponseFor200
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
**data** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_cert_update_prepare_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_cert_update_prepare_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_cert_update_prepare_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_cert_update_prepare_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

