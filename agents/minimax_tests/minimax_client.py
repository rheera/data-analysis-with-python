"""Tiny MiniMax client shared by the test scripts. Reads agents/minimax.yaml."""
import os
from pathlib import Path

import requests
import yaml

CONFIG_PATH = Path(__file__).resolve().parent.parent / "minimax.yaml"
CONFIG = yaml.safe_load(CONFIG_PATH.read_text())
# In cloud sessions the network proxy replaces this header with the saved key.
HEADERS = {"Authorization": f"Bearer {os.environ.get('MINIMAX_API_KEY', 'proxy-injected')}"}


def chat(messages, model=None, max_tokens=None, **extra):
    """POST /chat/completions and return (http_status, response_json)."""
    body = {
        "model": model or CONFIG["model"],
        "max_tokens": max_tokens or CONFIG["max_tokens"],
        "messages": messages,
        **extra,
    }
    r = requests.post(CONFIG["api"]["base_url"] + "/chat/completions",
                      headers=HEADERS, json=body, timeout=CONFIG["timeout_seconds"])
    return r.status_code, r.json()


def answer(data):
    """Final answer text from a response, without any <think> block."""
    choices = data.get("choices") or []
    if not choices:
        return None
    content = choices[0]["message"].get("content") or ""
    return content.split("</think>")[-1].strip()


def error(data):
    """Error message from a response, or None."""
    if data.get("error"):
        return data["error"].get("message")
    base = data.get("base_resp") or {}
    return base.get("status_msg") if base.get("status_code") else None
