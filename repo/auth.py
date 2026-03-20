"""
Authentication Module

This module handles user authentication operations including login and logout.
It provides functions to verify user credentials and manage user sessions.
"""

import hashlib
from datetime import datetime


def login(email, password, user_db):
    """
    Authenticate a user with email and password.
    
    Args:
        email (str): User's email address
        password (str): User's password (plain text)
        user_db (dict): Dictionary containing user credentials
        
    Returns:
        dict: User object if authentication successful, None otherwise
        
    Raises:
        ValueError: If email or password is empty
        
    Example:
        >>> user = login("user@example.com", "password123", user_db)
        >>> if user:
        ...     print(f"Login successful for {user['email']}")
    """
    if not email or not password:
        raise ValueError("Email and password cannot be empty")
    
    # Hash the provided password
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if user exists and password matches
    if email in user_db and user_db[email]['password'] == password_hash:
        user = user_db[email].copy()
        user['last_login'] = datetime.now().isoformat()
        return user
    
    return None


def logout(user_id, session_manager):
    """
    Logout a user and clear their session.
    
    Args:
        user_id (str): Unique identifier for the user
        session_manager (dict): Dictionary managing active sessions
        
    Returns:
        bool: True if logout successful, False otherwise
        
    Example:
        >>> success = logout("user123", session_manager)
        >>> if success:
        ...     print("User logged out successfully")
    """
    if user_id in session_manager:
        session_manager[user_id]['logged_out_at'] = datetime.now().isoformat()
        del session_manager[user_id]
        return True
    
    return False


def verify_token(token, session_manager):
    """
    Verify if a session token is valid.
    
    Args:
        token (str): Session token to verify
        session_manager (dict): Dictionary managing active sessions
        
    Returns:
        dict: Session data if token is valid, None otherwise
        
    Example:
        >>> session = verify_token("token_abc123", session_manager)
        >>> if session:
        ...     print(f"Token valid for user {session['user_id']}")
    """
    for user_id, session_data in session_manager.items():
        if session_data.get('token') == token:
            return session_data
    
    return None


def validate_password_strength(password):
    """
    Validate password strength based on security criteria.
    
    Args:
        password (str): Password to validate
        
    Returns:
        tuple: (is_valid, message) where is_valid is bool and message is str
        
    Criteria:
        - Minimum 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        
    Example:
        >>> is_valid, msg = validate_password_strength("Pass123")
        >>> print(msg)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter"
    
    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter"
    
    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one digit"
    
    return True, "Password is strong"
