# devo-model-manager
Devo API for machine learning

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0
- Package version: 1.8.7
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [http://www.devo.com](http://www.devo.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install devo-model-manager
```

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:

```python
import devo_model_manager_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import devo_model_manager_client
```

### Versioning

Versioning depends on the branch name, not the commit history of that branch. For example, if branch name is:

- BREAKING-CHANGE/MAC-xxx_Whatever: 1.2.3 -> 2.0.0
- feature/MAC-xxx_Whatever: 1.2.3 -> 1.3.0
- fix/MAC-xxx_Whatever: 1.2.3 -> 1.2.4

Note (v{MAJOR}.{MINOR}.{PATCH}):
- For MAJOR: branch name has to start with "Major" or "Break" (case insensitive)
- For MINOR: branch name has to start with "Minor" or "Feat" (case insensitive)
- For PATCH: in any other case

(all defined in: [bump-version.yml](.github/workflows/bump-version.yml))

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import devo_model_manager_client
from devo_model_manager_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: standAloneToken
configuration = devo_model_manager_client.Configuration()
configuration.api_key['standAloneToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standAloneToken'] = 'Bearer'

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
name = 'name_example' # str | 

try:
    api_instance.delete_model_by_id(domain_name, name)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_model_by_id: %s\n" % e)

# Configure API key authorization: standAloneToken
configuration = devo_model_manager_client.Configuration()
configuration.api_key['standAloneToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standAloneToken'] = 'Bearer'

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 

try:
    api_response = api_instance.find_all(domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_all: %s\n" % e)

# Configure API key authorization: standAloneToken
configuration = devo_model_manager_client.Configuration()
configuration.api_key['standAloneToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standAloneToken'] = 'Bearer'

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
name = 'name_example' # str | 

try:
    api_response = api_instance.find_all_children(domain_name, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_all_children: %s\n" % e)

# Configure API key authorization: standAloneToken
configuration = devo_model_manager_client.Configuration()
configuration.api_key['standAloneToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standAloneToken'] = 'Bearer'

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
name = 'name_example' # str | 

try:
    api_response = api_instance.find_by_name(domain_name, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_by_name: %s\n" % e)

# Configure API key authorization: standAloneToken
configuration = devo_model_manager_client.Configuration()
configuration.api_key['standAloneToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standAloneToken'] = 'Bearer'

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
name = 'name_example' # str | 

try:
    api_response = api_instance.find_by_name_fast(domain_name, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_by_name_fast: %s\n" % e)

# Configure API key authorization: standAloneToken
configuration = devo_model_manager_client.Configuration()
configuration.api_key['standAloneToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standAloneToken'] = 'Bearer'

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
name = 'name_example' # str |  (optional)
engine = 'engine_example' # str |  (optional)

try:
    api_response = api_instance.find_filtered(domain_name, name=name, engine=engine)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_filtered: %s\n" % e)

# Configure API key authorization: standAloneToken
configuration = devo_model_manager_client.Configuration()
configuration.api_key['standAloneToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standAloneToken'] = 'Bearer'

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
name = 'name_example' # str | 

try:
    api_response = api_instance.find_image(domain_name, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_image: %s\n" % e)

# Configure API key authorization: standAloneToken
configuration = devo_model_manager_client.Configuration()
configuration.api_key['standAloneToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standAloneToken'] = 'Bearer'

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
newerthan = 789 # int | 

try:
    api_response = api_instance.find_newer_than(newerthan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_newer_than: %s\n" % e)

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
email = 'email_example' # str |  (optional)
domain = 'domain_example' # str |  (optional)
password = 'password_example' # str |  (optional)

try:
    api_response = api_instance.login(email=email, domain=domain, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->login: %s\n" % e)

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))

try:
    api_response = api_instance.logout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->logout: %s\n" % e)

# Configure API key authorization: standAloneToken
configuration = devo_model_manager_client.Configuration()
configuration.api_key['standAloneToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standAloneToken'] = 'Bearer'

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
body = devo_model_manager_client.ModelDetail() # ModelDetail |  (optional)

try:
    api_instance.save_model(domain_name, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->save_model: %s\n" % e)

# Configure API key authorization: standAloneToken
configuration = devo_model_manager_client.Configuration()
configuration.api_key['standAloneToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['standAloneToken'] = 'Bearer'

# create an instance of the API class
api_instance = devo_model_manager_client.DefaultApi(devo_model_manager_client.ApiClient(configuration))
domain_name = 'domain_name_example' # str | 
engine = 'engine_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)

try:
    api_response = api_instance.upload_model_image(domain_name, engine=engine, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_model_image: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://{host}:{port}/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**delete_model_by_id**](docs/DefaultApi.md#delete_model_by_id) | **DELETE** /domains/{domainName}/models/{name} | 
*DefaultApi* | [**find_all**](docs/DefaultApi.md#find_all) | **GET** /domains/{domainName}/models | 
*DefaultApi* | [**find_all_children**](docs/DefaultApi.md#find_all_children) | **GET** /domains/{domainName}/models/{name}/children | 
*DefaultApi* | [**find_by_name**](docs/DefaultApi.md#find_by_name) | **GET** /domains/{domainName}/models/{name} | 
*DefaultApi* | [**find_by_name_fast**](docs/DefaultApi.md#find_by_name_fast) | **GET** /domains/{domainName}/models/{name}/fast | 
*DefaultApi* | [**find_filtered**](docs/DefaultApi.md#find_filtered) | **GET** /domains/{domainName}/models/filtered | 
*DefaultApi* | [**find_image**](docs/DefaultApi.md#find_image) | **GET** /domains/{domainName}/models/{name}/image | 
*DefaultApi* | [**find_newer_than**](docs/DefaultApi.md#find_newer_than) | **GET** /domains/*/models/newerthan/{newerthan} | 
*DefaultApi* | [**login**](docs/DefaultApi.md#login) | **POST** /stateful/login | 
*DefaultApi* | [**logout**](docs/DefaultApi.md#logout) | **GET** /stateful/logout | 
*DefaultApi* | [**save_model**](docs/DefaultApi.md#save_model) | **POST** /domains/{domainName}/models | 
*DefaultApi* | [**upload_model_image**](docs/DefaultApi.md#upload_model_image) | **POST** /domains/{domainName}/models/images/upload | 

## Documentation For Models

 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [Cluster](docs/Cluster.md)
 - [Field](docs/Field.md)
 - [Image](docs/Image.md)
 - [LoginResponse](docs/LoginResponse.md)
 - [Model](docs/Model.md)
 - [ModelDetail](docs/ModelDetail.md)
 - [ModelReview](docs/ModelReview.md)

## Documentation For Authorization


## standAloneToken

- **Type**: API key
- **API key parameter name**: standAloneToken
- **Location**: HTTP header


## Author

machine.learning@devo.com
