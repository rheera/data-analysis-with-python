"""Which request parameters the API accepts or rejects.

A made-up parameter goes first as a control: if the API accepts it, then
"accepted" alone says nothing about whether a parameter is applied.

Usage: python agents/minimax_tests/check_params.py [model]
"""
import sys

from minimax_client import answer, chat, error

model = sys.argv[1] if len(sys.argv) > 1 else None
HI = "Say hi in three words."
TESTS = [
    ("control: made-up foo_bar=1", {"foo_bar": 1}, HI),
    ("temperature 0", {"temperature": 0}, HI),
    ("temperature 2.5", {"temperature": 2.5}, HI),
    ("top_p 0", {"top_p": 0}, HI),
    ("top_p 0.5", {"top_p": 0.5}, HI),
    ("top_p 1.5", {"top_p": 1.5}, HI),
    ("top_k 40", {"top_k": 40}, HI),
    ("presence_penalty 0.5", {"presence_penalty": 0.5}, HI),
    ("frequency_penalty 0.5", {"frequency_penalty": 0.5}, HI),
    ("seed 42", {"seed": 42}, HI),
    ("n 2", {"n": 2}, HI),
    ("stop ['3']", {"stop": ["3"]}, "Count from 1 to 5, separated by spaces."),
]
for name, extra, prompt in TESTS:
    status, data = chat([{"role": "user", "content": prompt}], model=model, **extra)
    result = error(data) or f"accepted -> {answer(data)!r}"
    print(f"{name:28s} HTTP {status}  {result}")
