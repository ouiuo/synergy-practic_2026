import re

_non_letters = re.compile(r"[^0-9a-zа-яё\s]+", re.IGNORECASE)
_spaces = re.compile(r"\s+")


def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = _non_letters.sub(" ", text)
    text = _spaces.sub(" ", text)
    return text
