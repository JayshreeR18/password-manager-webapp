import hashlib, base64, os
from cryptography.fernet import Fernet

def derive_key(password: str, salt: bytes = None):
    salt = salt or b'some_fixed_salt'  # for now
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000, dklen=32)
    return base64.urlsafe_b64encode(key)

def encrypt_data(data: str, key: bytes):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_data(data: str, key: bytes):
    f = Fernet(key)
    return f.decrypt(data.encode()).decode()
