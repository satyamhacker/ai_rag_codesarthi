"""
User Service Module

This module provides user management operations including user creation,
retrieval, password hashing, and user data manipulation.
"""

import hashlib
import uuid
from datetime import datetime


class UserService:
    """
    Service class for managing user operations.
    
    Provides methods for creating users, retrieving user data,
    hashing passwords, and updating user information.
    """
    
    def __init__(self, database=None):
        """
        Initialize the UserService.
        
        Args:
            database (dict, optional): In-memory database for users. Defaults to empty dict.
        """
        self.database = database if database is not None else {}
    
    
    def create_user(self, email, password, full_name=None):
        """
        Create a new user in the system.
        
        Args:
            email (str): User's email address (must be unique)
            password (str): User's password (will be hashed)
            full_name (str, optional): User's full name
            
        Returns:
            dict: Created user object with user_id, email, full_name, created_at
            
        Raises:
            ValueError: If email already exists or email is invalid
            
        Example:
            >>> user = user_service.create_user("john@example.com", "SecurePass123", "John Doe")
            >>> print(user['user_id'])
        """
        if not email or '@' not in email:
            raise ValueError("Invalid email address")
        
        if email in self.database:
            raise ValueError(f"User with email {email} already exists")
        
        user_id = str(uuid.uuid4())
        password_hash = self.hash_password(password)
        
        user = {
            'user_id': user_id,
            'email': email,
            'password': password_hash,
            'full_name': full_name or '',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'is_active': True
        }
        
        self.database[email] = user
        return user
    
    
    def get_user(self, email):
        """
        Retrieve a user by email address.
        
        Args:
            email (str): User's email address
            
        Returns:
            dict: User object if found, None otherwise
            
        Example:
            >>> user = user_service.get_user("john@example.com")
            >>> if user:
            ...     print(f"User found: {user['full_name']}")
        """
        return self.database.get(email)
    
    
    def get_user_by_id(self, user_id):
        """
        Retrieve a user by user ID.
        
        Args:
            user_id (str): Unique user identifier
            
        Returns:
            dict: User object if found, None otherwise
            
        Example:
            >>> user = user_service.get_user_by_id("550e8400-e29b-41d4-a716-446655440000")
            >>> if user:
            ...     print(user['email'])
        """
        for user in self.database.values():
            if user['user_id'] == user_id:
                return user
        return None
    
    
    def hash_password(self, password):
        """
        Hash a password using SHA-256 algorithm.
        
        Args:
            password (str): Plain text password to hash
            
        Returns:
            str: Hexadecimal hash of the password
            
        Note:
            This is a basic implementation. For production, use bcrypt or argon2.
            
        Example:
            >>> hashed = user_service.hash_password("MyPassword123")
            >>> print(len(hashed))  # SHA-256 produces 64 character hex string
            64
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    
    def verify_password(self, email, password):
        """
        Verify if a password matches the stored hash for a user.
        
        Args:
            email (str): User's email address
            password (str): Plain text password to verify
            
        Returns:
            bool: True if password matches, False otherwise
            
        Example:
            >>> is_valid = user_service.verify_password("john@example.com", "SecurePass123")
            >>> if is_valid:
            ...     print("Password is correct")
        """
        user = self.get_user(email)
        if not user:
            return False
        
        password_hash = self.hash_password(password)
        return user['password'] == password_hash
    
    
    def update_user(self, email, **kwargs):
        """
        Update user information.
        
        Args:
            email (str): User's email address
            **kwargs: Fields to update (e.g., full_name, is_active)
            
        Returns:
            dict: Updated user object, None if user not found
            
        Example:
            >>> updated_user = user_service.update_user("john@example.com", full_name="John Smith")
            >>> print(updated_user['full_name'])
        """
        user = self.get_user(email)
        if not user:
            return None
        
        # Update allowed fields
        allowed_fields = ['full_name', 'is_active']
        for field, value in kwargs.items():
            if field in allowed_fields:
                user[field] = value
        
        user['updated_at'] = datetime.now().isoformat()
        return user
    
    
    def delete_user(self, email):
        """
        Delete a user from the system.
        
        Args:
            email (str): User's email address
            
        Returns:
            bool: True if user was deleted, False if user not found
            
        Example:
            >>> success = user_service.delete_user("john@example.com")
            >>> if success:
            ...     print("User deleted successfully")
        """
        if email in self.database:
            del self.database[email]
            return True
        return False
    
    
    def list_all_users(self):
        """
        Retrieve all users in the system.
        
        Returns:
            list: List of all user objects
            
        Example:
            >>> all_users = user_service.list_all_users()
            >>> print(f"Total users: {len(all_users)}")
        """
        return list(self.database.values())
    
    
    def get_user_count(self):
        """
        Get the total number of users in the system.
        
        Returns:
            int: Number of users
            
        Example:
            >>> count = user_service.get_user_count()
            >>> print(f"System has {count} users")
        """
        return len(self.database)
