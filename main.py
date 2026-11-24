"""Two-Sentence Horror.

Writes one horror story of exactly two sentences to /output/entry.txt:
a child's drawing of the family, and the second sentence that turns
the faceless man in it into the father himself.
"""

from pathlib import Path

TEXT = (
    "My daughter drew our family yesterday: me, her mother, her, and a "
    "tall man standing behind us with no face. When I asked her who he "
    "was, she said, 'That's you, Daddy \u2014 that's how you look when "
    "you think we're asleep.'"
)


# The competition accepts texts of 1 to 400 characters.
MIN_CHARS = 1
MAX_CHARS = 400

# The competition requires exactly two sentences.
SENTENCES = 2
TERMINATORS = ".!?"


def check_sentences(text: str) -> None:
    """Refuse to write a text that is not exactly two sentences."""
    n = sum(1 for ch in text if ch in TERMINATORS)
    if n != SENTENCES:
        raise SystemExit(
            f"entry text has {n} sentence terminators; the gate requires "
            f"exactly {SENTENCES} sentences"
        )


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    check_sentences(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
