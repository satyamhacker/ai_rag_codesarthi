"""
Sample Project Package

This package contains sample implementations of authentication and user management modules.
It demonstrates best practices for user authentication, password hashing, and database operations.
"""

from .auth import (
    login,
    logout,
    verify_token,
    validate_password_strength
)

from .user_service import UserService

__version__ = "1.0.0"
__author__ = "CodeSarthi"

__all__ = [
    'login',
    'logout',
    'verify_token',
    'validate_password_strength',
    'UserService'
]
