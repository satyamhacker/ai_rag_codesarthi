"""
user_service.py – In‑memory user store.

Provides simple user registration and retrieval.
"""

# In‑memory store: email -> user info
_users = {}

def create_user(email: str, password_hash: str) -> bool:
    """Create a new user.

    Args:
        email: User email.
        password_hash: Pre‑hashed password (should use auth.hash_password).

    Returns:
        True if user created, False if user already exists.
    """
    if email in _users:
        return False
    _users[email] = {"email": email, "password": password_hash}
    return True


def get_user(email: str) -> dict | None:
    """Retrieve a user by email.

    Args:
        email: User email.

    Returns:
        User dict if found, None otherwise.
    """
    return _users.get(email)


def list_users() -> list:
    """List all registered users."""
    return list(_users.values())