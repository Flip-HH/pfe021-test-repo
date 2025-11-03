"""Functions with TODO, FIXME, and BUG comments.

This module demonstrates common code annotation patterns used in development
to mark areas that need attention, improvement, or contain known issues.
"""

from typing import List, Optional, Dict
import re


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discounted price.
    
    # TODO: Add validation for negative prices
    # TODO: Consider adding support for multiple discount types
    """
    return price * (1 - discount_percent / 100)


def parse_email(email: str) -> Dict[str, str]:
    """Extract username and domain from email address.
    
    # FIXME: This regex doesn't handle all valid email formats
    # FIXME: Should validate email format before parsing
    """
    match = re.match(r'^([^@]+)@([^@]+)$', email)
    if match:
        return {"username": match.group(1), "domain": match.group(2)}
    return {"username": "", "domain": ""}


def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers.
    
    # BUG: Division by zero is not handled properly
    """
    return a / b


def find_user_by_id(user_id: int, users: List[Dict]) -> Optional[Dict]:
    """Find a user in the list by ID.
    
    # TODO: Optimize this O(n) search with a hash map
    # FIXME: Should handle case-insensitive ID matching
    """
    for user in users:
        if user.get('id') == user_id:
            return user
    return None


def process_payment(amount: float, currency: str = "USD") -> bool:
    """Process a payment transaction.
    
    # TODO: Implement actual payment gateway integration
    # TODO: Add transaction logging
    # FIXME: Currency conversion rates are hardcoded
    # BUG: Negative amounts are not rejected
    """
    conversion_rates = {"USD": 1.0, "EUR": 0.85, "GBP": 0.73}
    
    # FIXME: This will crash if currency is not in dict
    converted = amount * conversion_rates[currency]
    
    # TODO: Replace this placeholder with real payment processing
    print(f"Processing {converted} USD")
    return True


def sort_by_priority(items: List[Dict]) -> List[Dict]:
    """Sort items by priority field.
    
    # BUG: Crashes when items don't have 'priority' key
    # FIXME: Should handle missing or None priority values
    # TODO: Add support for custom sort orders
    """
    return sorted(items, key=lambda x: x['priority'])


def cache_result(key: str, value: any) -> None:
    """Cache a computation result.
    
    # TODO: Implement cache expiration
    # TODO: Add cache size limit to prevent memory leaks
    # FIXME: This global cache is not thread-safe
    # BUG: Cache never gets cleared, grows indefinitely
    """
    global _cache
    if '_cache' not in globals():
        _cache = {}
    _cache[key] = value


def validate_password(password: str) -> bool:
    """Check if password meets security requirements.
    
    # FIXME: Requirements are too weak (no special chars, no length minimum)
    # TODO: Add checks for common passwords
    # TODO: Implement password strength meter
    """
    if len(password) < 6:
        return False
    # BUG: This only checks if ANY digit exists, should require multiple criteria
    return any(c.isdigit() for c in password)


def format_phone_number(phone: str) -> str:
    """Format phone number to standard format.
    
    # FIXME: Only handles US phone numbers
    # TODO: Add international format support
    # BUG: Doesn't validate that input is actually a phone number
    """
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone


def get_config_value(key: str, default=None):
    """Retrieve configuration value.
    
    # TODO: Load config from file instead of hardcoding
    # FIXME: Config should be loaded once at startup, not every call
    # BUG: Changes to config require code changes
    """
    config = {
        "api_url": "https://api.example.com",
        "timeout": 30,
        "retry_count": 3
    }
    return config.get(key, default)


def merge_lists(list1: List, list2: List) -> List:
    """Merge two lists removing duplicates.
    
    # BUG: Order is not preserved
    # FIXME: This is inefficient for large lists (O(n^2))
    # TODO: Use set operations for better performance
    """
    result = list1.copy()
    for item in list2:
        if item not in result:
            result.append(item)
    return result


if __name__ == "__main__":
    # Simple demo showing the functions (some will demonstrate bugs!)
    print("Testing annotated functions:")
    
    print("\n1. calculate_discount(100, 20):", calculate_discount(100, 20))
    
    print("\n2. parse_email('user@example.com'):", parse_email('user@example.com'))
    
    # This will crash - demonstrates BUG comment
    try:
        print("\n3. divide_numbers(10, 0):", divide_numbers(10, 0))
    except ZeroDivisionError as e:
        print(f"   ERROR: {e} (as noted in BUG comment)")
    
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    print("\n4. find_user_by_id(1, users):", find_user_by_id(1, users))
    
    print("\n5. process_payment(100, 'USD'):", process_payment(100, 'USD'))
    
    # This will crash - demonstrates BUG comment
    try:
        items = [{"name": "A"}, {"name": "B", "priority": 2}]
        print("\n6. sort_by_priority(items):", sort_by_priority(items))
    except KeyError as e:
        print(f"   ERROR: {e} (as noted in BUG comment)")
    
    print("\n7. validate_password('pass123'):", validate_password('pass123'))
    
    print("\n8. format_phone_number('1234567890'):", format_phone_number('1234567890'))
    
    print("\n9. get_config_value('timeout'):", get_config_value('timeout'))
    
    print("\n10. merge_lists([1,2,3], [3,4,5]):", merge_lists([1,2,3], [3,4,5]))
    
    print("\n✓ Demo complete (some functions showed expected bugs)")
