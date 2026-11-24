#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — a 5-7-5 haiku about debugging.

Writes the haiku to /output/entry.txt (the file the sealed scorer reads).
Before writing, the program verifies its own entry against the gate:
three lines, 5-7-5 syllables, 1 to 200 characters.
"""

import os

HAIKU = """The rubber duck stares
I explain the bug aloud
and the answer lands"""

# Syllable count of every word in the haiku, counted by hand.
SYLLABLES = {
    "the": 1, "rubber": 2, "duck": 1, "stares": 1,
    "i": 1, "explain": 2, "bug": 1, "aloud": 2,
    "and": 1, "answer": 2, "lands": 1,
}

EXPECTED_SHAPE = (5, 7, 5)


def check(haiku: str) -> None:
    """Raise if the haiku breaks the 5-7-5 shape or the 200-char limit."""
    text = haiku.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"haiku is {len(text)} chars, must be 1-200")
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku has {len(lines)} lines, must be 3")
    for line, expected in zip(lines, EXPECTED_SHAPE):
        count = sum(SYLLABLES[word] for word in line.lower().split())
        if count != expected:
            raise ValueError(f"{line!r} is {count} syllables, expected {expected}")


def main() -> None:
    check(HAIKU)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")
    print(HAIKU)


if __name__ == "__main__":
    main()
