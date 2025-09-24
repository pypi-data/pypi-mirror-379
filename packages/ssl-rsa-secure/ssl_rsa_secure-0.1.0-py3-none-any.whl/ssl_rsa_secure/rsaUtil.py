import base64
import json
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

_current_key = None


def set_buffer_key(key_string: str):
    """
    Sets the AES key to be used for encryption/decryption.
    :param key_string: A 32-character string representing the AES key.
    """
    global _current_key

    if not isinstance(key_string, str) or not key_string.strip():
        raise ValueError("Key must be a non-empty string.")

    key_bytes = key_string.encode('utf-8')

    if len(key_bytes) != 32:
        raise ValueError(f"Invalid key length: got {len(key_bytes)} bytes. Expected 32 bytes for AES-256.")

    _current_key = key_bytes


def encrypt_data(data):
    """
    Encrypts data using AES-256-CBC and the previously set key.
    :param data: String or JSON-serializable object to encrypt
    :return: Encrypted data in the format: iv:encryptedBase64
    """
    if _current_key is None:
        raise ValueError("Encryption key not set. Use set_buffer_key() before encrypting.")

    iv = os.urandom(16)
    plaintext = data if isinstance(data, str) else json.dumps(data)
    plaintext_bytes = plaintext.encode('utf-8')

    cipher = AES.new(_current_key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(plaintext_bytes, AES.block_size))

    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    iv_base64 = base64.b64encode(iv).decode('utf-8')

    return f"{iv_base64}:{encrypted_base64}"


def decrypt_data(encrypted_text: str):
    """
    Decrypts data using AES-256-CBC and the previously set key.
    :param encrypted_text: Encrypted text in the format: iv:encryptedBase64
    :return: Decrypted plain text or parsed JSON object
    """
    if _current_key is None:
        raise ValueError("Decryption key not set. Use set_buffer_key() before decrypting.")

    try:
        iv_base64, encrypted_base64 = encrypted_text.split(':')
    except ValueError:
        raise ValueError('Invalid encrypted format. Expected "iv:encryptedData".')

    iv = base64.b64decode(iv_base64)
    encrypted_bytes = base64.b64decode(encrypted_base64)

    cipher = AES.new(_current_key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
    decrypted_text = decrypted_bytes.decode('utf-8')

    try:
        return json.loads(decrypted_text)
    except json.JSONDecodeError:
        return decrypted_text
