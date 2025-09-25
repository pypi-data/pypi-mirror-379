from keyauth_renee import is_valid_key

def test_valid_key():
    assert is_valid_key("abc123", "http://localhost:8000/validate") is True

def test_invalid_key():
    assert is_valid_key("badkey", "http://localhost:8000/validate") is False