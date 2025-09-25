from .core import KeyAuth

def is_valid_key(key: str, url: str) -> bool:
    return KeyAuth(url).check(key)