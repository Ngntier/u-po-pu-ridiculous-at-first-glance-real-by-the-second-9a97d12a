"""Write the one-sentence pitch to /output/entry.txt.

Pure stdlib, deterministic: the same bytes on every run.
"""

import os

SENTENCE = (
    "We sell one square foot of a stranger's backyard to apartment dwellers "
    "who pay $9 a month for a deed, a photo, and the right to say they own "
    "land in the country."
)


def main() -> None:
    # Gate guard: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space, and the brief requires one sentence.
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars, must be 1-200"
    assert text and not text.isspace(), "sentence must not be only white space"
    assert text.count(".") == 1 and text.endswith("."), "must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
