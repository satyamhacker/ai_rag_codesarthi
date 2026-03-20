"""
Authentication Database Module

This module handles SQLite database operations for user authentication.
It provides functions to initialize the database, register users, and verify credentials.
"""

import sqlite3
import hashlib
import os
from datetime import datetime


# Database file path
DB_PATH = "users.db"


def init_db():
    """
    Initialize the SQLite database and create the users table.
    
    Creates a users table with the following columns:
    - id: Primary key (auto-increment)
    - email: User's email address (unique)
    - password: Hashed password (SHA-256)
    - created_at: Timestamp when user was created
    - updated_at: Timestamp when user was last updated
    
    Returns:
        bool: True if database initialized successfully, False otherwise
        
    Raises:
        sqlite3.Error: If database operation fails
        
    Example:
        >>> success = init_db()
        >>> if success:
        ...     print("Database initialized successfully")
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
        
        print(f"✓ Database initialized successfully at {DB_PATH}")
        return True
        
    except sqlite3.Error as e:
        print(f"✗ Database initialization error: {e}")
        return False


def hash_password(password):
    """
    Hash a password using SHA-256 algorithm.
    
    Args:
        password (str): Plain text password to hash
        
    Returns:
        str: Hexadecimal hash of the password (64 characters)
        
    Note:
        SHA-256 is used for simplicity. For production, use bcrypt or argon2.
        
    Example:
        >>> hashed = hash_password("MyPassword123")
        >>> print(len(hashed))
        64
    """
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(email, password):
    """
    Register a new user in the database.
    
    Args:
        email (str): User's email address (must be unique)
        password (str): User's password (will be hashed before storing)
        
    Returns:
        dict: User object with id, email, created_at if successful
        None: If registration fails (e.g., email already exists)
        
    Raises:
        ValueError: If email or password is empty
        sqlite3.IntegrityError: If email already exists
        
    Example:
        >>> user = register_user("john@example.com", "SecurePass123")
        >>> if user:
        ...     print(f"User registered with ID: {user['id']}")
        ... else:
        ...     print("Registration failed")
    """
    if not email or not password:
        print("✗ Email and password cannot be empty")
        return None
    
    if '@' not in email:
        print("✗ Invalid email address")
        return None
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Hash the password
        password_hash = hash_password(password)
        
        # Insert user into database
        cursor.execute('''
            INSERT INTO users (email, password)
            VALUES (?, ?)
        ''', (email, password_hash))
        
        conn.commit()
        user_id = cursor.lastrowid
        
        # Retrieve the created user
        cursor.execute('''
            SELECT id, email, created_at FROM users WHERE id = ?
        ''', (user_id,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            user = {
                'id': result[0],
                'email': result[1],
                'created_at': result[2]
            }
            print(f"✓ User registered successfully: {email}")
            return user
        
        return None
        
    except sqlite3.IntegrityError:
        print(f"✗ Email {email} already exists in the database")
        return None
        
    except sqlite3.Error as e:
        print(f"✗ Database error during registration: {e}")
        return None


def verify_user(email, password):
    """
    Verify user credentials and return user ID if valid.
    
    Args:
        email (str): User's email address
        password (str): User's password (plain text)
        
    Returns:
        int: User ID if credentials are valid
        None: If email not found or password doesn't match
        
    Raises:
        ValueError: If email or password is empty
        sqlite3.Error: If database operation fails
        
    Example:
        >>> user_id = verify_user("john@example.com", "SecurePass123")
        >>> if user_id:
        ...     print(f"Login successful. User ID: {user_id}")
        ... else:
        ...     print("Invalid credentials")
    """
    if not email or not password:
        print("✗ Email and password cannot be empty")
        return None
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Hash the provided password
        password_hash = hash_password(password)
        
        # Query user by email and password
        cursor.execute('''
            SELECT id, email FROM users WHERE email = ? AND password = ?
        ''', (email, password_hash))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            user_id = result[0]
            print(f"✓ Login successful for {email} (User ID: {user_id})")
            return user_id
        else:
            print(f"✗ Invalid credentials for {email}")
            return None
            
    except sqlite3.Error as e:
        print(f"✗ Database error during verification: {e}")
        return None


def get_user_by_email(email):
    """
    Retrieve user information by email address.
    
    Args:
        email (str): User's email address
        
    Returns:
        dict: User object with id, email, created_at if found
        None: If user not found
        
    Example:
        >>> user = get_user_by_email("john@example.com")
        >>> if user:
        ...     print(f"User found: {user['email']}")
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, email, created_at FROM users WHERE email = ?
        ''', (email,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return {
                'id': result[0],
                'email': result[1],
                'created_at': result[2]
            }
        
        return None
        
    except sqlite3.Error as e:
        print(f"✗ Database error: {e}")
        return None


def get_all_users():
    """
    Retrieve all users from the database.
    
    Returns:
        list: List of user objects with id, email, created_at
        
    Example:
        >>> users = get_all_users()
        >>> print(f"Total users: {len(users)}")
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, email, created_at FROM users
        ''')
        
        results = cursor.fetchall()
        conn.close()
        
        users = [
            {
                'id': row[0],
                'email': row[1],
                'created_at': row[2]
            }
            for row in results
        ]
        
        return users
        
    except sqlite3.Error as e:
        print(f"✗ Database error: {e}")
        return []


def delete_user(email):
    """
    Delete a user from the database.
    
    Args:
        email (str): User's email address
        
    Returns:
        bool: True if user was deleted, False otherwise
        
    Example:
        >>> success = delete_user("john@example.com")
        >>> if success:
        ...     print("User deleted successfully")
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM users WHERE email = ?', (email,))
        conn.commit()
        
        deleted = cursor.rowcount > 0
        conn.close()
        
        if deleted:
            print(f"✓ User {email} deleted successfully")
        else:
            print(f"✗ User {email} not found")
        
        return deleted
        
    except sqlite3.Error as e:
        print(f"✗ Database error: {e}")
        return False


def get_user_count():
    """
    Get the total number of users in the database.
    
    Returns:
        int: Number of users
        
    Example:
        >>> count = get_user_count()
        >>> print(f"Total users: {count}")
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]
        conn.close()
        
        return count
        
    except sqlite3.Error as e:
        print(f"✗ Database error: {e}")
        return 0


# Test script
if __name__ == "__main__":
    print("=" * 60)
    print("CodeSarthi - Authentication Database Test")
    print("=" * 60)
    
    # Initialize database
    print("\n1. Initializing database...")
    init_db()
    
    # Register test users
    print("\n2. Registering test users...")
    user1 = register_user("alice@example.com", "AlicePass123")
    user2 = register_user("bob@example.com", "BobPass456")
    
    # Try to register duplicate email
    print("\n3. Attempting to register duplicate email...")
    user3 = register_user("alice@example.com", "AnotherPass")
    
    # Verify users with correct password
    print("\n4. Verifying users with correct passwords...")
    verify_user("alice@example.com", "AlicePass123")
    verify_user("bob@example.com", "BobPass456")
    
    # Verify users with wrong password
    print("\n5. Verifying users with wrong passwords...")
    verify_user("alice@example.com", "WrongPassword")
    verify_user("bob@example.com", "WrongPassword")
    
    # Get all users
    print("\n6. Retrieving all users...")
    all_users = get_all_users()
    print(f"Total users in database: {len(all_users)}")
    for user in all_users:
        print(f"   - ID: {user['id']}, Email: {user['email']}, Created: {user['created_at']}")
    
    # Get user count
    print("\n7. Getting user count...")
    count = get_user_count()
    print(f"User count: {count}")
    
    # Get specific user
    print("\n8. Retrieving specific user...")
    user = get_user_by_email("alice@example.com")
    if user:
        print(f"User found: {user}")
    
    print("\n" + "=" * 60)
    print(f"✓ Test completed. Database file: {DB_PATH}")
    print("=" * 60)
