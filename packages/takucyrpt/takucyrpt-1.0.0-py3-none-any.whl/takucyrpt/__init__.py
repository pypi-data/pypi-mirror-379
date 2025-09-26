
from .data import data

def Tencrypt(message):
    """
    Encrypt a message using the takucyrpt cipher.
    
    Args:
        message (str): The message to encrypt
        
    Returns:
        str: The encrypted message
    """
    encrypted_message = ""
    for letter in message:
        if letter in data:
            encrypted_message += data[letter] + "^"
        else:
            encrypted_message += letter + "^"
    return encrypted_message.rstrip("^")

def Tdecrypt(encrypted_message):
    """
    Decrypt a message using the takucyrpt cipher.
    
    Args:
        encrypted_message (str): The encrypted message to decrypt
        
    Returns:
        str: The decrypted message
    """
    decrypted_message = ""
    symbols = encrypted_message.split("^")
    
    for symbol in symbols:
        if symbol == "":
            continue
        found = False
        for key, value in data.items():
            if value == symbol:
                decrypted_message += key
                found = True
                break
        if not found:
            decrypted_message += symbol
    return decrypted_message

# Make functions available at package level
__all__ = ['Tencrypt', 'Tdecrypt']
__version__ = "1.0.0"
