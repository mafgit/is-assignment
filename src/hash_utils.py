import hashlib, os


def hash_password(password: str, salt=None):
    if not salt:
        salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return salt.hex() + ":" + hashed.hex()


def verify_password(password: str, stored: str) -> bool:
    salt_hex, hash_hex = stored.split(":")
    salt = bytes.fromhex(salt_hex)
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return hashed.hex() == hash_hex

def anonymize_name(id: int, multiplier: int):
    return "ANON_" + str(id * multiplier)

def anonymize_contact(contact: str):
    return "XXX-XXX-" + contact[-4:]

