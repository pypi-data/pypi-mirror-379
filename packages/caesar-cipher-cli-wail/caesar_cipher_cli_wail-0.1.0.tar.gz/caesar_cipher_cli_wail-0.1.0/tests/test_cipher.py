from caesar_cipher_cli_wail.cli import encrypt, encrypt

def test_encrypt_lower():
    assert encrypt("abc", 1) == "bcd"

def test_encrypt_upper():
    assert encrypt("ABC", 2) == "CDE"

def test_wrap():
    assert encrypt("xyz", 3) == "abc"

def test_decrypt():
    assert encrypt("def", 3) == "abc"

def test_nonalpha_preserved():
    assert encrypt("a b!2", 5) == "f g!2"
