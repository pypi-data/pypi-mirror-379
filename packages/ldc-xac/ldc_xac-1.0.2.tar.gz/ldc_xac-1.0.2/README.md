# LDC-XAC - External API Caller

A Python package for making external API calls with comprehensive logging capabilities.

## Features

- **Comprehensive Logging**: Log all external API requests, responses, and errors in a structured format
- **Request Tracking**: Track request duration and performance metrics
- **Error Handling**: Detailed error logging with exception information
- **Data Truncation**: Automatic truncation of large request/response data for logging
- **Flexible Configuration**: Customizable API codes, system identifiers, and logging parameters

## Installation

```bash
pip install ldc-xac
```

## Quick Start

```python
from xac import make_external_api_request

# Make a simple GET request
response = make_external_api_request(
    url="https://api.example.com/data",
    method="GET",
    api_code="EXAMPLE_API",
    system="MY_SYSTEM"
)

print(response.status_code)
print(response.json())

# For testing with self-signed certificates or SSL issues
response = make_external_api_request(
    url="https://api.example.com/data",
    method="GET",
    api_code="EXAMPLE_API",
    system="MY_SYSTEM",
    verify=False  # Disable SSL verification
)
```

## Advanced Usage

```python
from xac import ExternalAPICaller

# Log a request manually
start_time = ExternalAPICaller.log_external_api_request(
    url="https://api.example.com/users",
    method="POST",
    api_code="CREATE_USER",
    system="USER_MANAGEMENT"
)

# Make your request
import requests
response = requests.post(
    "https://api.example.com/users",
    json={"name": "John Doe", "email": "john@example.com"}
)

# Log the response
ExternalAPICaller.log_external_api_response(
    url="https://api.example.com/users",
    response=response,
    start_time=start_time,
    api_code="CREATE_USER",
    system="USER_MANAGEMENT"
)
```

## Configuration

The package uses the following default configuration:

- **MAX_REQUEST_BODY_SIZE**: 10,000 characters (configurable in `xac.config`)

## Logging Format

The package logs in JSON format with the following structure:

### Request Log
```json
{
    "descr": "External API Request",
    "system": "EXTERNAL",
    "api_code": "API_CALL",
    "request_method": "GET",
    "request_url": "https://api.example.com/data"
}
```

### Response Log
```json
{
    "descr": "External API Response",
    "system": "EXTERNAL",
    "api_code": "API_CALL",
    "response_code": 200,
    "response_for_request": "https://api.example.com/data",
    "time_taken_ms": 150.25
}
```

### Error Log
```json
{
    "descr": "External API Error",
    "system": "EXTERNAL",
    "api_code": "API_CALL",
    "response_code": null,
    "response_for_request": "https://api.example.com/data",
    "time_taken_ms": 5000.0,
    "error_message": "Connection timeout",
    "error_type": "ConnectTimeout"
}
```

## API Reference

### `make_external_api_request()`

Make an external API request with automatic logging.

**Parameters:**
- `url` (str): The API endpoint URL
- `method` (str): HTTP method (default: "GET")
- `headers` (dict, optional): Request headers
- `params` (dict, optional): Query parameters
- `timeout` (int, optional): Request timeout in seconds (default: 300)
- `api_code` (str, optional): Custom API code identifier
- `system` (str, optional): System identifier
- `verify` (bool, optional): SSL certificate verification (default: True)
- `**kwargs`: Additional arguments passed to `requests.request()`

**Returns:**
- `requests.Response`: The response object

### `ExternalAPICaller`

Main class for logging external API calls.

#### Methods:

- `log_external_api_request()`: Log request details
- `log_external_api_response()`: Log response details
- `log_external_api_error()`: Log error details
- `_truncate_large_data()`: Truncate large data for logging

## Development

### Setup Development Environment

```bash
git clone https://github.com/ayushsonar-lendenclub/ldc-xac
cd xac
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black xac/
```

### Type Checking

```bash
mypy xac/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for your changes
5. Run the test suite
6. Submit a pull request

## Support

For support and questions, please open an issue on GitHub.
