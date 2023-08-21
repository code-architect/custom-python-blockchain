import hashlib


def hash256(s):
    """Two rounds of SHA256"""
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()
