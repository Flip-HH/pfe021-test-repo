"""User management module with duplicated validation logic.

This module demonstrates code duplication in validation and formatting.
Contains generic utility functions that are duplicated within this file
and also duplicated in order_processing.py.
"""

from typing import Optional, Dict, List, Any
import re
from datetime import datetime
import json


# ============================================================================
# GENERIC UTILITY FUNCTIONS - DUPLICATED WITHIN THIS FILE AND ACROSS FILES
# ============================================================================

def sanitize_string(text: str) -> str:
    """Remove special characters and trim whitespace.
    
    DUPLICATED: This exact function appears multiple times in this file
    and also exists in order_processing.py
    """
    if not text:
        return ""
    # Remove special characters except spaces, letters, numbers
    cleaned = re.sub(r'[^\w\s-]', '', text)
    # Remove extra whitespace
    cleaned = ' '.join(cleaned.split())
    return cleaned.strip()


def validate_non_empty_string(value: str, field_name: str) -> bool:
    """Validate that a string is not empty.
    
    DUPLICATED: This validation pattern is duplicated across the codebase.
    """
    if not value or not isinstance(value, str):
        raise ValueError(f"{field_name} cannot be empty")
    if len(value.strip()) == 0:
        raise ValueError(f"{field_name} cannot be only whitespace")
    return True


def format_timestamp(timestamp: str) -> str:
    """Format ISO timestamp to readable string.
    
    DUPLICATED: This exact function appears in multiple places.
    """
    if not timestamp:
        return "Unknown"
    try:
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return "Invalid Date"


def safe_get(data: Dict, key: str, default: Any = None) -> Any:
    """Safely get value from dictionary.
    
    DUPLICATED: This helper is duplicated throughout the codebase.
    """
    if not isinstance(data, dict):
        return default
    return data.get(key, default)


def build_response(success: bool, message: str, data: Any = None) -> Dict:
    """Build standardized response dictionary.
    
    DUPLICATED: This pattern appears in multiple modules.
    """
    response = {
        "success": success,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    if data is not None:
        response["data"] = data
    return response


def sanitize_input(text: str) -> str:
    """Sanitize user input - INTERNAL DUPLICATION #1.
    
    This is a duplicate of sanitize_string() above.
    """
    if not text:
        return ""
    # Remove special characters except spaces, letters, numbers
    cleaned = re.sub(r'[^\w\s-]', '', text)
    # Remove extra whitespace
    cleaned = ' '.join(cleaned.split())
    return cleaned.strip()


def check_timestamp_format(timestamp: str) -> str:
    """Format timestamp - INTERNAL DUPLICATION #2.
    
    This is a duplicate of format_timestamp() above.
    """
    if not timestamp:
        return "Unknown"
    try:
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return "Invalid Date"


def create_user(username: str, email: str, age: int) -> Dict:
    """Create a new user with validation.
    
    Note: Validation logic is duplicated across multiple functions.
    Uses generic utilities that are also duplicated.
    """
    # Use duplicated sanitize function
    username = sanitize_string(username)
    email = sanitize_input(email)  # Using the duplicate version
    
    # Duplicated: Email validation
    if not email or '@' not in email:
        raise ValueError("Invalid email address")
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValueError("Email format is invalid")
    
    # Duplicated: Username validation
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters")
    if not username.isalnum():
        raise ValueError("Username must be alphanumeric")
    
    # Duplicated: Age validation
    if age < 13:
        raise ValueError("User must be at least 13 years old")
    if age > 120:
        raise ValueError("Invalid age")
    
    return {
        "username": username,
        "email": email.lower(),
        "age": age,
        "created_at": datetime.now().isoformat()
    }


def update_user(user_id: int, username: str = None, email: str = None, age: int = None) -> Dict:
    """Update user information with validation.
    
    Note: Contains duplicated validation from create_user.
    """
    updates = {}
    
    if email is not None:
        # Duplicated: Email validation (same as create_user)
        if not email or '@' not in email:
            raise ValueError("Invalid email address")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValueError("Email format is invalid")
        updates["email"] = email.lower()
    
    if username is not None:
        # Duplicated: Username validation (same as create_user)
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters")
        if not username.isalnum():
            raise ValueError("Username must be alphanumeric")
        updates["username"] = username
    
    if age is not None:
        # Duplicated: Age validation (same as create_user)
        if age < 13:
            raise ValueError("User must be at least 13 years old")
        if age > 120:
            raise ValueError("Invalid age")
        updates["age"] = age
    
    updates["updated_at"] = datetime.now().isoformat()
    return updates


def register_admin(username: str, email: str, age: int, admin_code: str) -> Dict:
    """Register a new admin user.
    
    Note: Duplicates validation logic from create_user.
    """
    # Duplicated: Email validation (exact copy)
    if not email or '@' not in email:
        raise ValueError("Invalid email address")
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValueError("Email format is invalid")
    
    # Duplicated: Username validation (exact copy)
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters")
    if not username.isalnum():
        raise ValueError("Username must be alphanumeric")
    
    # Duplicated: Age validation (exact copy)
    if age < 13:
        raise ValueError("User must be at least 13 years old")
    if age > 120:
        raise ValueError("Invalid age")
    
    # Admin-specific validation
    if admin_code != "ADMIN123":
        raise ValueError("Invalid admin code")
    
    return {
        "username": username,
        "email": email.lower(),
        "age": age,
        "role": "admin",
        "created_at": datetime.now().isoformat()
    }


def format_user_display(user: Dict) -> str:
    """Format user info for display.
    
    Note: Contains duplicated formatting logic.
    """
    # Duplicated: Date formatting
    created = user.get("created_at", "")
    if created:
        try:
            dt = datetime.fromisoformat(created)
            created = dt.strftime("%Y-%m-%d %H:%M:%S")
        except:
            created = "Unknown"
    
    # Duplicated: String building pattern
    lines = []
    lines.append(f"Username: {user.get('username', 'N/A')}")
    lines.append(f"Email: {user.get('email', 'N/A')}")
    lines.append(f"Age: {user.get('age', 'N/A')}")
    lines.append(f"Created: {created}")
    
    return "\n".join(lines)


def format_admin_display(admin: Dict) -> str:
    """Format admin info for display.
    
    Note: Duplicates formatting logic from format_user_display.
    """
    # Duplicated: Date formatting (exact copy)
    created = admin.get("created_at", "")
    if created:
        try:
            dt = datetime.fromisoformat(created)
            created = dt.strftime("%Y-%m-%d %H:%M:%S")
        except:
            created = "Unknown"
    
    # Duplicated: String building pattern (exact copy)
    lines = []
    lines.append(f"Username: {admin.get('username', 'N/A')}")
    lines.append(f"Email: {admin.get('email', 'N/A')}")
    lines.append(f"Age: {admin.get('age', 'N/A')}")
    lines.append(f"Created: {created}")
    lines.append(f"Role: {admin.get('role', 'N/A')}")  # Only difference
    
    return "\n".join(lines)


def get_users_by_age_range(users: List[Dict], min_age: int, max_age: int) -> List[Dict]:
    """Filter users by age range.
    
    Note: Contains duplicated filtering logic.
    """
    # Duplicated: Age validation
    if min_age < 13:
        raise ValueError("Minimum age must be at least 13")
    if max_age > 120:
        raise ValueError("Maximum age cannot exceed 120")
    
    # Duplicated: List filtering pattern
    result = []
    for user in users:
        age = user.get("age")
        if age is not None and min_age <= age <= max_age:
            result.append(user)
    return result


def get_active_users_by_age(users: List[Dict], min_age: int, max_age: int) -> List[Dict]:
    """Filter active users by age range.
    
    Note: Duplicates filtering logic from get_users_by_age_range.
    """
    # Duplicated: Age validation (exact copy)
    if min_age < 13:
        raise ValueError("Minimum age must be at least 13")
    if max_age > 120:
        raise ValueError("Maximum age cannot exceed 120")
    
    # Duplicated: List filtering pattern (similar)
    result = []
    for user in users:
        age = user.get("age")
        is_active = user.get("active", False)
        if age is not None and min_age <= age <= max_age and is_active:
            result.append(user)
    return result


def create_success_response(message: str, data: Any = None) -> Dict:
    """Create success response - INTERNAL DUPLICATION #3.
    
    This duplicates build_response() above.
    """
    response = {
        "success": True,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    if data is not None:
        response["data"] = data
    return response


def create_error_response(message: str) -> Dict:
    """Create error response - INTERNAL DUPLICATION #4.
    
    This also duplicates build_response() above.
    """
    response = {
        "success": False,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    return response


def log_action(action: str, details: Dict) -> None:
    """Log user action with timestamp.
    
    DUPLICATED: This logging pattern appears in both files.
    """
    log_entry = {
        "action": action,
        "details": details,
        "timestamp": datetime.now().isoformat()
    }
    # In real code, this would write to a file or service
    print(f"[LOG] {json.dumps(log_entry)}")


if __name__ == "__main__":
    print("User Management Module - Demonstrating Code Duplication\n")
    print("="*60)
    print("DEMONSTRATING INTERNAL AND CROSS-FILE DUPLICATION")
    print("="*60)
    
    # Test duplicated utility functions
    print("\n1. Testing DUPLICATED sanitize functions:")
    test_input = "  Hello@World#123  "
    print(f"   Input: '{test_input}'")
    print(f"   sanitize_string(): '{sanitize_string(test_input)}'")
    print(f"   sanitize_input(): '{sanitize_input(test_input)}'")
    print("   ^ These are INTERNAL duplicates")
    
    print("\n2. Testing DUPLICATED timestamp functions:")
    now = datetime.now().isoformat()
    print(f"   format_timestamp(): {format_timestamp(now)}")
    print(f"   check_timestamp_format(): {check_timestamp_format(now)}")
    print("   ^ These are INTERNAL duplicates")
    
    print("\n3. Testing DUPLICATED response builders:")
    print(f"   build_response(): {build_response(True, 'Success', {'id': 1})}")
    print(f"   create_success_response(): {create_success_response('Success', {'id': 1})}")
    print(f"   create_error_response(): {create_error_response('Error')}")
    print("   ^ These are INTERNAL duplicates")
    
    print("\n" + "="*60 + "\n")
    
    # Test create_user
    user1 = create_user("alice123", "alice@example.com", 25)
    print("Created user:")
    print(format_user_display(user1))
    
    print("\n" + "="*60 + "\n")
    
    # Test admin creation
    admin1 = register_admin("admin01", "admin@example.com", 30, "ADMIN123")
    print("Created admin:")
    print(format_admin_display(admin1))
    
    print("\n" + "="*60 + "\n")
    
    # Test filtering
    test_users = [
        {"username": "user1", "age": 15, "active": True},
        {"username": "user2", "age": 25, "active": True},
        {"username": "user3", "age": 35, "active": False},
    ]
    
    filtered = get_users_by_age_range(test_users, 20, 40)
    print(f"Users aged 20-40: {len(filtered)} found")
    
    active_filtered = get_active_users_by_age(test_users, 20, 40)
    print(f"Active users aged 20-40: {len(active_filtered)} found")
    
    print("\n" + "="*60)
    print("NOTE: Many utility functions in this file also exist in")
    print("      order_processing.py (CROSS-FILE DUPLICATION)")
    print("="*60)
