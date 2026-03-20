# Sample Project – User Management API

This is a sample Python project that demonstrates a simple user management system.

## Features
- User registration with email and password
- Password hashing using SHA256
- Simple user lookup

## Files
- `auth.py` – Contains authentication logic.
- `user_service.py` – Handles user operations.

## Usage
```python
from auth import hash_password, verify_password
from user_service import create_user, get_user

create_user("alice@example.com", "secret")
user = get_user("alice@example.com")
print(user)