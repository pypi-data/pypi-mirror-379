import requests
import os

# -----------------------------
# Custom Exceptions
# -----------------------------
class OrionacAIError(Exception):
    pass

class AuthenticationError(OrionacAIError):
    pass

class APIError(OrionacAIError):
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

# -----------------------------
# API Response Object
# -----------------------------
class APIResponse:
    def __init__(self, response_json):
        self._data = response_json
        # Extract text from vLLM-style response
        choices = self._data.get("choices", [])
        if choices and "message" in choices[0]:
            self.text = choices[0]["message"].get("content", "")
        else:
            self.text = ""
        self.model_used = self._data.get("model", "")
        usage = self._data.get("usage", {})
        self.prompt_tokens = usage.get("prompt_tokens")
        self.completion_tokens = usage.get("completion_tokens")
        self.total_tokens = usage.get("total_tokens")

    def __repr__(self):
        return f"<APIResponse text='{self.text[:50]}...'>"

    @property
    def raw_data(self):
        return self._data

# -----------------------------
# Main Client
# -----------------------------
class Theta:
    def __init__(self, api_key=None, base_url="http://13.202.235.154:8000/v1"):
        if api_key is None:
            api_key = os.environ.get("ORIONAC_API_KEY")
        if not api_key:
            raise AuthenticationError(
                "No API key provided or set in environment variable ORIONAC_API_KEY."
            )

        self.api_key = api_key
        self.api_base_url = base_url
        self.default_model = "merged_model"
        self.timeout = 60
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "orionac-ai-python/0.1.0"
        })
        self.last_response = None

    # -------------------------
    # Generate Method
    # -------------------------
    def generate(self, prompt, stream=False, **kwargs):
        payload = {
            "model": kwargs.get("model", self.default_model),
            "messages": [{"role": "user", "content": prompt}],
            "stream": stream
        }

        try:
            url = f"{self.api_base_url}/chat/completions"
            if stream:
                url += "/stream"

            response = self._session.post(url, json=payload, timeout=self.timeout, stream=stream)
            self.last_response = response

            if stream:
                # Streaming: return a generator of text chunks
                def generator():
                    for chunk in response.iter_content(chunk_size=16, decode_unicode=True):
                        if chunk:
                            yield chunk
                return generator()
            else:
                # Non-streaming: return APIResponse object
                response.raise_for_status()
                return APIResponse(response.json())

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise AuthenticationError("Authentication failed. Check your API key.")
            else:
                raise APIError(f"API returned error: {e.response.text}", status_code=e.response.status_code)
        except requests.exceptions.RequestException as e:
            raise APIError(f"Network error: {e}")
