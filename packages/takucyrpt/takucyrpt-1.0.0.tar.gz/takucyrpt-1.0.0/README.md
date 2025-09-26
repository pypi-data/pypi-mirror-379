# Takucyrpt

A simple encryption and decryption module for text.

## Installation

```bash
pip install takucyrpt
```

## Usage

```python
from takucyrpt import encrypt, decrypt

text = "Hello, World!"
key = "mykey"

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print(f"Original: {text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

## Functions

### encrypt(text, key)
Encrypts the given text using a simple XOR cipher with the provided key.

### decrypt(ciphertext, key)
Decrypts the given ciphertext using a simple XOR cipher with the provided key.

## Example

```python
from takucyrpt import encrypt, decrypt

# Encrypt a message
message = "This is a secret message"
key = "secretkey"
encrypted_message = encrypt(message, key)
print(f"Encrypted: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt(encrypted_message, key)
print(f"Decrypted: {decrypted_message}")
```

## License

MIT

## Author

Takuya

## Changelog

### 1.0.0
- Initial release
- Basic encryption and decryption functions
