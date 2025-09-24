# Orionac GenAI Python SDK Documentation

---

## Installation

Install via PyPI:

```bash
pip install orionac_ai
```

Or install locally:

```bash
pip install ./dist/orionac_ai-0.2.1-py3-none-any.whl
```

---

## Quick Start

```python
from orionac_genai.client import Theta

client = Theta(api_key="YOUR_API_KEY_HERE", base_url="http:///v1")

# Non-streaming generation
response = client.generate("Hello EC2!", stream=False)
print(response.text)

# Streaming generation
stream_gen = client.generate("Hello EC2!", stream=True)
for chunk in stream_gen:
    print(chunk, end="")
```

---

## Features

1. Non-streaming generation: Returns a full `APIResponse` object.
2. Streaming generation: Returns a generator yielding chunks of text.
3. Custom parameters: Supports `model`, `temperature`, `max_tokens`, etc.
4. Automatic error handling with `AuthenticationError` and `APIError`.
5. Stateless: Each request is independent.

---

## API Reference

### Class: `Theta`

```python
Theta(api_key: str, base_url: str = "")
```

* `api_key`: Your API key for authentication.
* `base_url`: URL of the Orionac GenAI server.

### Method: `generate`

```python
generate(prompt: str, stream: bool = False, **kwargs) -> APIResponse | generator
```

* `prompt`: Text to generate from.
* `stream`: If True, returns a generator.
* `kwargs`: Additional parameters like `model`, `max_tokens`, `temperature`, etc.

Returns `APIResponse` for non-streaming, or generator for streaming.

### Class: `APIResponse`

```python
APIResponse._data
APIResponse.text
APIResponse.model_used
APIResponse.prompt_tokens
APIResponse.completion_tokens
APIResponse.total_tokens
```

---

## Error Handling

```python
from orionac_genai.client import Theta, AuthenticationError, APIError

try:
    client = Theta(api_key="YOUR_API_KEY")
    response = client.generate("Hello!")
except AuthenticationError as e:
    print("Invalid API key:", e)
except APIError as e:
    print("API request failed:", e, e.status_code)
```

---

## Example Use Cases

1. Chatbots
2. Email drafting

```python
resp = client.generate(
    "Draft a follow-up email to a prospect we spoke with.",
    context={"prospect_name": "Jane Doe"}
)
print(resp.text)
```

3. Streaming terminal applications

```python
for chunk in client.generate("Explain AWS EC2 to a beginner.", stream=True):
    print(chunk, end="")
```

---

## Notes

* Ensure EC2 security group allows inbound traffic on port `8000`.
* Supports HTTP and HTTPS.
* Fully stateless.
