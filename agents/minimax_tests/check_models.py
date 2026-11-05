"""Which models listed by /v1/models actually answer a request.

Usage: python agents/minimax_tests/check_models.py
"""
import requests

from minimax_client import CONFIG, HEADERS, chat, error

models = requests.get(CONFIG["api"]["base_url"] + "/models", headers=HEADERS, timeout=30).json()["data"]
for m in models:
    status, data = chat([{"role": "user", "content": "hi"}], model=m["id"], max_tokens=64)
    print(f"{m['id']:24s} HTTP {status}  {error(data) or 'available'}")
