
"""
auth.py – User authentication module.

Provides password hashing and verification.
"""

import hashlib

def hash_password(password: str) -> str:
    """Hash a password using SHA256.

    Args:
        password: Plain text password.

    Returns:
        Hexadecimal string of the hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against its hash.

    Args:
        password: Plain text password.
        hashed: Previously hashed password.

    Returns:
        True if the password matches, False otherwise.
    """
    return hash_password(password) == hashed