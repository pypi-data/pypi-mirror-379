<p align="center">
    <a href="https://katonic.ai/">
      <img src="https://katonic.ai/assets/brand/Logo.png" width="550">
    </a>
</p>
<br />

[![Docs Latest](https://img.shields.io/badge/docs-latest-blue.svg)](https://docs.katonic.ai/)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/katonic-dev/katonic-sdk/blob/master/LICENSE)
[![PYPI](https://img.shields.io/pypi/v/katonic.svg)](https://pypi.python.org/pypi/katonic)

# Katonic SDK

A Python SDK for interacting with Katonic's AI/ML platform, providing easy access to language models, vision models, and comprehensive request logging capabilities.

## Features

- 🤖 **Language Model Integration**: Generate completions from various LLM models
- 👁️ **Vision Model Support**: Process text and image inputs with vision models
- 📊 **Request Logging**: Comprehensive logging with token usage and cost tracking
- ⚡ **Simple API**: Easy-to-use Python functions instead of raw API calls
- 🔍 **Monitoring**: Track and analyze LLM requests across your applications

## Installation

```bash
pip install katonic
```

## Model Completion

### Import

```python
from katonic.llm import generate_completion
```

### generate_completion

Generates a completion from a specified model.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `model_id` | str | ✅ | Unique identifier of the model (found in My Model Library under LLM Management) |
| `data` | dict | ✅ | Input payload containing query and optional image_url |
| `data.query` | str | ✅ | The prompt or question |
| `data.image_url` | str | ❌ | Image URL for vision models |

#### Returns
- **Type**: `str`
- **Description**: Model-generated response as plain text

#### Finding Your Model ID

To find your model ID:
1. Navigate to **My Model Library** under **LLM Management** in the Katonic UI

    ![alt text](image.png)
2. Copy the model ID from the interface
3. Use this ID in the `model_id` parameter

### Examples

#### Text Model

```python
from katonic.llm import generate_completion

result = generate_completion(
    model_id="688b552061aa55897ae98fdc",
    data={"query": "Tell me a fun fact about space."}
)

print(result)
# Output: "Space is completely silent because there is no atmosphere to carry sound waves."
```

#### Vision Model (Text + Image)

```python
from katonic.llm import generate_completion

result = generate_completion(
    model_id="688b552061aa55897ae98fdc",
    data={
        "query": "Describe what is in this image.",
        "image_url": "https://example.com/photo.jpg"
    }
)

print(result)
```

#### Response Format

The response will contain the model's generated text.

Example:
```
"Space is completely silent because there is no atmosphere to carry sound waves."
```

## Request Logging

### Import

```python
from katonic.llm.log_requests import log_request_to_platform
```

### log_request_to_platform

Logs user queries, responses, token usage, and cost details for monitoring and analysis.

`model_name` can be fetched from the following section of the platform.

![alt text](image-1.png)

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `input_query` | str | ✅ | The original user query |
| `response` | str | ✅ | The LLM's response to the query |
| `user_name` | str | ✅ | The user's email or unique identifier |
| `model_name` | str | ✅ | The LLM model name (e.g., "Openai/gpt-5-nano", "Anthropic/claude") |
| `product_type` | str | ✅ | Type of product (e.g., "Ace") |
| `product_name` | str | ✅ | Name of the product where the query was made |
| `project_name` | str | ✅ | The project associated with the query |
| `latency` | float | ✅ | API latency in seconds |
| `status` | str | ✅ | Request status (e.g., "success", "failed") |
| `answer_validity` | bool | ❌ | Whether the response is valid/usable (default: False) |
| `embedding_model_name` | str | ❌ | Name of embedding model if applicable |

#### Returns
- **Success**: Returns a `message_id` (string) for tracking the logged request
- **Failure**: Returns `None`

### Example

```python
from katonic.llm.log_requests import log_request_to_platform

# Log a request with comprehensive details
message_id = log_request_to_platform(
    input_query="tell me about katonic",
    response="Katonic is a modern MLOps platform that helps enterprises manage AI/ML workflows efficiently.",
    user_name="developer@company.com",
    model_name="Openai/gpt-5-nano",
    product_type="Ace",
    product_name="Ace",
    project_name="Ace",
    latency=0.42,  # API response time in seconds
    status="success",  # status of the request
    embedding_model_name=None
)

print(f"Message logged with ID: {message_id}")
```

### Response Format

On successful logging:
```
✅ Cost has been added successfully.
Message logged with ID: 650e95d2a8c7b123f5c123ab
```

## Complete Workflow Example

Here's how to use both methods together:

```python
from katonic.llm import generate_completion
from katonic.llm.log_requests import log_request_to_platform
import time

# Step 1: Generate completion
start_time = time.time()
query = "Explain quantum computing in simple terms"
model_id = "688b552061aa55897ae98fdc"

result = generate_completion(
    model_id=model_id,
    data={"query": query}
)

# Step 2: Calculate latency
latency = time.time() - start_time

# Step 3: Log the request
message_id = log_request_to_platform(
    input_query=query,
    response=result,
    user_name="developer@company.com",
    model_name="Openai/gpt-4",
    product_type="Research",
    product_name="QA Assistant",
    project_name="Science Education",
    latency=latency,
    status="success"
)

print(f"Response: {result}")
print(f"Logged with ID: {message_id}")
```

## Notes

### Model Completion
- Use the correct `model_id` provided in the Katonic UI
- For image-based models, ensure `image_url` is accessible over the internet
- The SDK handles API calls internally, so you only need to focus on inputs and outputs

### Request Logging
- The SDK automatically calculates token usage and cost (if pricing data is available)
- If the request fails, you will see a warning message in the console
- Use the returned `message_id` to track logged requests

## Requirements

- Python 3.7+
- Internet connection for API calls
- Valid Katonic platform credentials

## Support

For issues, questions, or feature requests, please contact the Katonic support team or refer to the official Katonic platform documentation.

## License

Please refer to your Katonic platform agreement for licensing terms.