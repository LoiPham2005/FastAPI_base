from typing import Any

def to_camel(string: str) -> str:
    return "".join(word.capitalize() for word in string.split("_"))

def to_snake(string: str) -> str:
    return "".join(["_" + i.lower() if i.isupper() else i for i in string]).lstrip("_")
