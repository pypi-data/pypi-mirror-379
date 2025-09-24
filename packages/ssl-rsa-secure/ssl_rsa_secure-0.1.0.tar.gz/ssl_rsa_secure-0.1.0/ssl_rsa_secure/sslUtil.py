from authlib.jose import JsonWebEncryption
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from pathlib import Path
import json
from typing import Union

_jwe = JsonWebEncryption()

_private_key = None
_public_key = None

def load_private_key(pem_or_path: str):
    global _private_key
    pem_content = pem_or_path
    if not pem_content.strip().startswith("-----BEGIN"):
        pem_content = Path(pem_or_path).read_text(encoding="utf-8")
    _private_key = serialization.load_pem_private_key(
        pem_content.encode(), password=None, backend=default_backend()
    )

def load_public_key(pem_or_path: str):
    global _public_key
    pem_content = pem_or_path
    if not pem_content.strip().startswith("-----BEGIN"):
        pem_content = Path(pem_or_path).read_text(encoding="utf-8")
    _public_key = serialization.load_pem_public_key(
        pem_content.encode(), backend=default_backend()
    )

def encrypt_data(data: Union[dict, str]) -> str:
    if _public_key is None:
        raise ValueError("Public key not loaded.")
    plaintext = data if isinstance(data, str) else json.dumps(data)
    protected_header = {
        "alg": "RSA-OAEP-256",
        "enc": "A256GCM",
        "zip": "DEF"  # optional compression
    }
    encrypted = _jwe.serialize_compact(protected_header, plaintext.encode(), _public_key)
    return encrypted.decode() if isinstance(encrypted, bytes) else encrypted

def decrypt_data(encrypted_data: str) -> Union[dict, str]:
    if _private_key is None:
        raise ValueError("Private key not loaded.")
    decrypted = _jwe.deserialize_compact(encrypted_data, _private_key)
    payload_bytes = decrypted["payload"]
    payload_str = payload_bytes.decode()
    try:
        return json.loads(payload_str)
    except json.JSONDecodeError:
        return payload_str
