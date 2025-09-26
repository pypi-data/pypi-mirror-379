[![PyPI - Version](https://img.shields.io/pypi/v/gsmservice_gateway)](https://pypi.org/project/gsmservice-gateway/)
[![GitHub License](https://img.shields.io/github/license/gsmservice-pl/messaging-sdk-python)](https://github.com/gsmservice-pl/messaging-sdk-python/blob/main/LICENSE)
[![Static Badge](https://img.shields.io/badge/built_by-Speakeasy-yellow)](https://www.speakeasy.com/?utm_source=gsmservice-gateway&utm_campaign=python)
# SzybkiSMS.pl Messaging REST API SDK for Python (powered by GSMService.pl)

This package includes Messaging SDK for Python to send SMS & MMS messages directly from your app via https://szybkisms.pl messaging platform.

## Additional documentation:

A documentation of all methods and types is available below in section [Available Resources and Operations
](#available-resources-and-operations).

Also you can refer to the [REST API documentation](https://api.szybkisms.pl/rest/) for additional details about the basics of this SDK.
<!-- No Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [SzybkiSMS.pl Messaging REST API SDK for Python (powered by GSMService.pl)](#szybkismspl-messaging-rest-api-sdk-for-python-powered-by-gsmservicepl)
  * [Additional documentation:](#additional-documentation)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add gsmservice-gateway
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install gsmservice-gateway
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add gsmservice-gateway
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from gsmservice-gateway python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "gsmservice-gateway",
# ]
# ///

from gsmservice_gateway import Client

sdk = Client(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Sending single SMS Message

This example demonstrates simple sending SMS message to a single recipient:

```python
# Synchronous Example
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.sms.send(request={
        "recipients": "+48999999999",
        "message": "This is SMS message content.",
        "sender": "Bramka SMS",
        "type": 1,
        "unicode": True,
        "flash": False,
        "date_": None,
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from gsmservice_gateway import Client

async def main():

    async with Client(
        bearer="<YOUR API ACCESS TOKEN>",
    ) as client:

        res = await client.outgoing.sms.send_async(request={
            "recipients": "+48999999999",
            "message": "This is SMS message content.",
            "sender": "Bramka SMS",
            "type": 1,
            "unicode": True,
            "flash": False,
            "date_": None,
        })

        # Handle response
        print(res)

asyncio.run(main())
```

### Sending single MMS Message

This example demonstrates simple sending MMS message to a single recipient:

```python
# Synchronous Example
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.send(request={
        "recipients": "+48999999999",
        "subject": "This is a subject of the message",
        "message": "This is MMS message content.",
        "attachments": "<file body in base64 format>",
        "date_": None,
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from gsmservice_gateway import Client

async def main():

    async with Client(
        bearer="<YOUR API ACCESS TOKEN>",
    ) as client:

        res = await client.outgoing.mms.send_async(request={
            "recipients": "+48999999999",
            "subject": "This is a subject of the message",
            "message": "This is MMS message content.",
            "attachments": "<file body in base64 format>",
            "date_": None,
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [accounts](docs/sdks/accounts/README.md)

* [get](docs/sdks/accounts/README.md#get) - Get account details
* [get_subaccount](docs/sdks/accounts/README.md#get_subaccount) - Get subaccount details


### [common](docs/sdks/common/README.md)

* [ping](docs/sdks/common/README.md#ping) - Checks API availability and version

### [incoming](docs/sdks/incoming/README.md)

* [list](docs/sdks/incoming/README.md#list) - List the received SMS messages
* [get_by_ids](docs/sdks/incoming/README.md#get_by_ids) - Get the incoming messages by IDs

### [outgoing](docs/sdks/outgoing/README.md)

* [get_by_ids](docs/sdks/outgoing/README.md#get_by_ids) - Get the messages details and status by IDs
* [cancel_scheduled](docs/sdks/outgoing/README.md#cancel_scheduled) - Cancel a scheduled messages
* [list](docs/sdks/outgoing/README.md#list) - Lists the history of sent messages

#### [outgoing.mms](docs/sdks/mms/README.md)

* [get_price](docs/sdks/mms/README.md#get_price) - Check the price of MMS Messages
* [send](docs/sdks/mms/README.md#send) - Send MMS Messages

#### [outgoing.sms](docs/sdks/sms/README.md)

* [get_price](docs/sdks/sms/README.md#get_price) - Check the price of SMS Messages
* [send](docs/sdks/sms/README.md#send) - Send SMS Messages

### [senders](docs/sdks/senders/README.md)

* [list](docs/sdks/senders/README.md#list) - List allowed senders names
* [add](docs/sdks/senders/README.md#add) - Add a new sender name
* [delete](docs/sdks/senders/README.md#delete) - Delete a sender name
* [set_default](docs/sdks/senders/README.md#set_default) - Set default sender name

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from gsmservice_gateway import Client
from gsmservice_gateway.utils import BackoffStrategy, RetryConfig


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.accounts.get(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from gsmservice_gateway import Client
from gsmservice_gateway.utils import BackoffStrategy, RetryConfig


with Client(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.accounts.get()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`ClientError`](./src/gsmservice_gateway/models/clienterror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from gsmservice_gateway import Client, models


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:
    res = None
    try:

        res = client.accounts.get()

        # Handle response
        print(res)


    except models.ClientError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.ErrorResponseError):
            print(e.data.type)  # Optional[str]
            print(e.data.status)  # Optional[int]
            print(e.data.title)  # Optional[str]
            print(e.data.detail)  # Optional[str]
            print(e.data.code)  # Optional[str]
```

### Error Classes
**Primary errors:**
* [`ClientError`](./src/gsmservice_gateway/models/clienterror.py): The base class for HTTP error responses.
  * [`ErrorResponseError`](./src/gsmservice_gateway/models/errorresponseerror.py): An object that complies with RFC 9457 containing information about a request error.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`ClientError`](./src/gsmservice_gateway/models/clienterror.py)**:
* [`ResponseValidationError`](./src/gsmservice_gateway/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name      | Server                                  | Description           |
| --------- | --------------------------------------- | --------------------- |
| `prod`    | `https://api.szybkisms.pl/rest`         | Production system     |
| `sandbox` | `https://api.szybkisms.pl/rest-sandbox` | Test system (SANDBOX) |

#### Example

```python
from gsmservice_gateway import Client


with Client(
    server="sandbox",
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.accounts.get()

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from gsmservice_gateway import Client


with Client(
    server_url="https://api.szybkisms.pl/rest",
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.accounts.get()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from gsmservice_gateway import Client
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Client(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from gsmservice_gateway import Client
from gsmservice_gateway.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Client(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name     | Type | Scheme      | Environment Variable |
| -------- | ---- | ----------- | -------------------- |
| `bearer` | http | HTTP Bearer | `GATEWAY_API_BEARER` |

To authenticate with the API the `bearer` parameter must be set when initializing the SDK client instance. For example:
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.accounts.get()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Client` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from gsmservice_gateway import Client
def main():

    with Client(
        bearer="<YOUR API ACCESS TOKEN>",
    ) as client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Client(
        bearer="<YOUR API ACCESS TOKEN>",
    ) as client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from gsmservice_gateway import Client
import logging

logging.basicConfig(level=logging.DEBUG)
s = Client(debug_logger=logging.getLogger("gsmservice_gateway"))
```

You can also enable a default debug logger by setting an environment variable `GATEWAY_API_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in continuous development and there may be breaking changes between a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation.
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release.