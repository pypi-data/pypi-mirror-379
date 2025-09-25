from caesar_rawan.cli import encrypt, decrypt

def test_encrypt_lower():
    assert encrypt("abc", 1) == "bcd"

def test_encrypt_upper():
    assert encrypt("ABC", 2) == "CDE"

def test_wrap():
    assert encrypt("xyz", 3) == "abc"

def test_decrypt():
    assert decrypt("def", 3) == "abc"

def test_nonalpha_preserved():
    assert encrypt("a b!2", 5) == "f g!2"
