import os
import json
import time
import base64
import typing as t
from dataclasses import dataclass
from enum import Enum

import requests


DEFAULT_CONTROL_BASE_URL = "https://metal-api.prava.co"


class ActionKind(str, Enum):
    LEFT_CLICK = "left_click"
    RIGHT_CLICK = "right_click"
    DOUBLE_CLICK = "double_click"
    TYPE = "type"
    KEY = "key"
    MOUSE_MOVE = "mouse_move"
    SCROLL = "scroll"
    WAIT = "wait"
    STOP = "stop"


@dataclass
class Coordinate:
    x: int
    y: int

    def to_dict(self) -> dict[str, int]:
        return {"x": self.x, "y": self.y}


@dataclass
class ControlAction:
    kind: ActionKind
    coordinate: t.Optional[Coordinate] = None
    text: t.Optional[str] = None
    keys: t.Optional[list[str]] = None
    delta_x: t.Optional[int] = None
    delta_y: t.Optional[int] = None
    duration_ms: t.Optional[int] = None
    message: t.Optional[str] = None

    def to_dict(self) -> dict[str, t.Any]:
        data = {"kind": self.kind.value}
        if self.coordinate:
            data["coordinate"] = self.coordinate.to_dict()
        if self.text:
            data["text"] = self.text
        if self.keys:
            data["keys"] = self.keys
        if self.delta_x is not None:
            data["delta_x"] = self.delta_x
        if self.delta_y is not None:
            data["delta_y"] = self.delta_y
        if self.duration_ms:
            data["duration_ms"] = self.duration_ms
        if self.message:
            data["message"] = self.message
        return data

    @classmethod
    def from_dict(cls, data: dict[str, t.Any]) -> "ControlAction":
        coordinate = None
        if "coordinate" in data:
            coord_data = data["coordinate"]
            coordinate = Coordinate(x=coord_data["x"], y=coord_data["y"])

        return cls(
            kind=ActionKind(data["kind"]),
            coordinate=coordinate,
            text=data.get("text"),
            keys=data.get("keys"),
            delta_x=data.get("delta_x"),
            delta_y=data.get("delta_y"),
            duration_ms=data.get("duration_ms"),
            message=data.get("message"),
        )


class ControlAPIError(RuntimeError):
    def __init__(self, status: int, message: str, data: t.Any | None = None):
        super().__init__(f"HTTP {status}: {message}")
        self.status = status
        self.data = data


def _control_request_json(
    method: str,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    json_body: t.Any | None = None,
    timeout: int = 90,
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
        raise ControlAPIError(resp.status_code, message, data)
    return data


@dataclass
class _ControlModels:
    base_url: str
    timeout: int

    def list(self) -> dict:
        """List available control models.

        Returns:
            Dict with 'models' key containing list of available models.
        """
        return _control_request_json(
            "GET",
            f"{self.base_url}/v1/control/models",
            timeout=self.timeout,
        )


class ControlClient:
    """Prava Control API client for computer automation.

    Example:
        >>> from prava.control import ControlClient
        >>> client = ControlClient()
        >>> models = client.models.list()
        >>> response = client.predict({
        ...     "model": "prava-af-medium",
        ...     "instruction": "Click the submit button",
        ...     "image_url": "data:image/png;base64,..."
        ... })
    """

    def __init__(self, *, base_url: str | None = None, timeout: int = 90):
        base = (base_url or DEFAULT_CONTROL_BASE_URL).rstrip("/")

        self.base_url = base
        self.timeout = int(timeout)
        self.models = _ControlModels(base_url=self.base_url, timeout=self.timeout)

    def predict(self, request: dict[str, t.Any]) -> dict[str, t.Any]:
        """Predict next control action from screenshot and instruction.

        Args:
            request: Dict containing model, instruction, image_url, and optional
                    previous_actions and context.

        Returns:
            Dict containing predicted action and metadata.
        """
        # Clean the request - ensure previous_actions are plain dicts
        clean_request = {
            "model": request["model"],
            "instruction": request["instruction"],
            "image_url": request["image_url"]
        }

        if "previous_actions" in request:
            clean_request["previous_actions"] = request["previous_actions"]

        if "context" in request:
            clean_request["context"] = request["context"]

        return _control_request_json(
            "POST",
            f"{self.base_url}/v1/control/predict",
            headers={"content-type": "application/json"},
            json_body=clean_request,
            timeout=self.timeout,
        )

    def screenshot_to_data_uri(self, image_bytes: bytes) -> str:
        """Convert image bytes to data URI format.

        Args:
            image_bytes: Raw image bytes (PNG format recommended).

        Returns:
            Data URI string suitable for image_url parameter.
        """
        b64_data = base64.b64encode(image_bytes).decode("ascii")
        return f"data:image/png;base64,{b64_data}"

    def run_task(
        self,
        instruction: str,
        take_screenshot: t.Callable[[], bytes],
        execute_action: t.Callable[[ControlAction], None],
        model: str = "prava-af-medium",
        max_iterations: int = 15,
    ) -> None:
        """Run a complete automation task with screenshots and action execution.

        Args:
            instruction: Natural language description of the task.
            take_screenshot: Function that returns screenshot bytes.
            execute_action: Function that executes a ControlAction.
            model: Model ID to use for predictions.
            max_iterations: Maximum number of action iterations.
        """
        previous_actions: list[ControlAction] = []

        for i in range(max_iterations):
            print(f"Iteration {i + 1}/{max_iterations}")

            # Take screenshot
            screenshot_bytes = take_screenshot()
            image_url = self.screenshot_to_data_uri(screenshot_bytes)

            # Get prediction
            result = self.predict({
                "model": model,
                "instruction": instruction,
                "image_url": image_url,
                "previous_actions": [action.to_dict() for action in previous_actions],
            })

            # Handle response
            if result.get("action"):
                action_data = result["action"]
                action = ControlAction.from_dict(action_data)
                print(f"Action: {action.kind}")

                # Execute action
                execute_action(action)
                previous_actions.append(action)

                # Check for completion
                if action.kind == ActionKind.STOP:
                    print("Task completed:", action.message)
                    break
            elif result.get("message"):
                print("Message:", result["message"])
                break
            else:
                print("No action returned")
                break

            # Small delay between actions
            time.sleep(0.5)