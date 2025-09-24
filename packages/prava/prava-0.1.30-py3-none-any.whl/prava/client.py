import os
import json
import base64
import typing as t
from dataclasses import dataclass

import requests


DEFAULT_BASE_URL = os.getenv("PRAVA_BASE_URL", "https://sdk-api.prava.co/v1").rstrip("/")
DEFAULT_CONTROL_BASE_URL = "https://metal-api.prava.co"


class APIError(RuntimeError):
    def __init__(self, status: int, message: str, data: t.Any | None = None):
        super().__init__(f"HTTP {status}: {message}")
        self.status = status
        self.data = data


def _request_json(
    method: str,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    json_body: t.Any | None = None,
    timeout: int = 60,
) -> t.Any:
    resp = requests.request(method, url, headers=headers, json=json_body, timeout=timeout)
    text = resp.text or ""
    data: t.Any | None = None
    try:
        data = json.loads(text) if text else None
    except Exception:
        data = None
    if not resp.ok:
        message = (data or {}).get("error", {}).get("message") or (data or {}).get("message") or resp.reason
        raise APIError(resp.status_code, message, data)
    return data


@dataclass
class _Tasks:
    api_key: str
    base_url: str
    timeout: int

    def create(self, body: dict) -> dict:
        """Create a task.

        Args:
            body: Request body with workflow, data, etc.
        Returns:
            Parsed JSON response as dict.
        """
        return _request_json(
            "POST",
            f"{self.base_url}/tasks",
            headers={
                "content-type": "application/json",
                "authorization": f"Bearer {self.api_key}",
            },
            json_body=body,
            timeout=self.timeout,
        )

    def get(self, task_id: str) -> dict:
        """Get a task by ID.

        Args:
            task_id: The task ID.
        Returns:
            Parsed JSON response as dict.
        """
        return _request_json(
            "GET",
            f"{self.base_url}/tasks/{task_id}",
            headers={
                "authorization": f"Bearer {self.api_key}",
            },
            timeout=self.timeout,
        )

    def list(self) -> dict:
        """List tasks.

        Returns:
            Parsed JSON response as dict.
        """
        return _request_json(
            "GET",
            f"{self.base_url}/tasks",
            headers={
                "authorization": f"Bearer {self.api_key}",
            },
            timeout=self.timeout,
        )


@dataclass
class _ControlModels:
    base_url: str
    timeout: int

    def list(self) -> dict:
        return _request_json("GET", f"{self.base_url}/v1/control/models", timeout=self.timeout)


class ControlClient:
    def __init__(self, *, api_key: str | None = None, base_url: str | None = None, timeout: int = 90):
        # Control API doesn't need API key for now, but keep interface consistent
        self.api_key = api_key or os.getenv("PRAVA_API_KEY")
        base = (base_url or DEFAULT_CONTROL_BASE_URL).rstrip("/")
        self.base_url = base
        self.timeout = int(timeout)
        self.models = _ControlModels(base_url=self.base_url, timeout=self.timeout)

    def predict(self, request: dict[str, t.Any]) -> dict[str, t.Any]:
        clean_request = {
            "model": request["model"],
            "instruction": request["instruction"],
            "image_url": request["image_url"]
        }
        if "previous_actions" in request:
            clean_request["previous_actions"] = request["previous_actions"]
        if "context" in request:
            clean_request["context"] = request["context"]

        return _request_json(
            "POST",
            f"{self.base_url}/v1/control/predict",
            headers={"content-type": "application/json"},
            json_body=clean_request,
            timeout=self.timeout,
        )

    def screenshot_to_data_uri(self, image_bytes: bytes) -> str:
        b64_data = base64.b64encode(image_bytes).decode("ascii")
        return f"data:image/png;base64,{b64_data}"


class Prava:
    """Prava API client.

    Example:
        >>> from prava import Prava
        >>> client = Prava()
        >>> client.tasks.create({"workflow": "example", "data": {}})
    """

    def __init__(self, *, api_key: str | None = None, base_url: str | None = None, timeout: int = 60):
        api_key = api_key or os.getenv("PRAVA_API_KEY")
        if not api_key:
            raise ValueError("Missing API key: pass api_key or set PRAVA_API_KEY")
        base = (base_url or DEFAULT_BASE_URL).rstrip("/")

        self.api_key = api_key
        self.base_url = base
        self.timeout = int(timeout)

        self.tasks = _Tasks(api_key=self.api_key, base_url=self.base_url, timeout=self.timeout)

