
import pytest
from takucyrpt import Tencrypt, Tdecrypt

def test_basic_encryption():
    """Test basic encryption and decryption"""
    message = "hello world"
    encrypted = Tencrypt(message)
    decrypted = Tdecrypt(encrypted)
    assert decrypted == message

def test_numbers():
    """Test number encryption"""
    message = "123456789"
    encrypted = Tencrypt(message)
    decrypted = Tdecrypt(encrypted)
    assert decrypted == message

def test_uppercase():
    """Test uppercase encryption"""
    message = "HELLO WORLD"
    encrypted = Tencrypt(message)
    decrypted = Tdecrypt(encrypted)
    assert decrypted == message

def test_special_characters():
    """Test special character encryption"""
    message = "Hello! @#$%"
    encrypted = Tencrypt(message)
    decrypted = Tdecrypt(encrypted)
    assert decrypted == message

def test_mixed_content():
    """Test mixed content encryption"""
    message = "Password123!@# Hello World"
    encrypted = Tencrypt(message)
    decrypted = Tdecrypt(encrypted)
    assert decrypted == message

def test_empty_string():
    """Test empty string"""
    message = ""
    encrypted = Tencrypt(message)
    decrypted = Tdecrypt(encrypted)
    assert decrypted == message

def test_whitespace():
    """Test whitespace characters"""
    message = "hello\tworld\ntest"
    encrypted = Tencrypt(message)
    decrypted = Tdecrypt(encrypted)
    assert decrypted == message

if __name__ == "__main__":
    pytest.main([__file__])
