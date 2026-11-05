"""Whether sampling settings change the answers.

Asks the same open-ended question several times per setting and counts the
distinct answers. If a setting works, temperature 0.01 or top_p 0.01 should
give fewer distinct answers than temperature 1.0, and a fixed seed should
repeat answers.

Usage: python agents/minimax_tests/check_effect.py [model] [runs]
"""
import sys
from collections import Counter

from minimax_client import answer, chat, error

model = sys.argv[1] if len(sys.argv) > 1 else None
runs = int(sys.argv[2]) if len(sys.argv) > 2 else 5
PROMPT = "Invent a name for a new coffee shop. Reply with only the name."
SETTINGS = [
    ("temperature 0.01", {"temperature": 0.01}),
    ("temperature 1.0", {"temperature": 1.0}),
    ("temperature 2.0", {"temperature": 2.0}),
    ("top_p 0.01, temperature 1.0", {"temperature": 1.0, "top_p": 0.01}),
    ("seed 42, temperature 1.0", {"temperature": 1.0, "seed": 42}),
]
for name, extra in SETTINGS:
    answers = []
    for _ in range(runs):
        _, data = chat([{"role": "user", "content": PROMPT}], model=model, **extra)
        answers.append(answer(data) or f"ERROR {error(data)}")
    counts = Counter(answers)
    print(f"{name:28s} distinct={len(counts)}/{runs}  {dict(counts)}")
