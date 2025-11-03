"""Order processing module with duplicated business logic.

This module demonstrates code duplication in calculation and validation.
Contains generic utility functions that are duplicated within this file
and also duplicated in user_management.py (CROSS-FILE DUPLICATION).
"""

from typing import Dict, List, Optional, Any
from decimal import Decimal
from datetime import datetime
import re
import json


# ============================================================================
# GENERIC UTILITY FUNCTIONS - DUPLICATED FROM user_management.py
# ============================================================================

def sanitize_string(text: str) -> str:
    """Remove special characters and trim whitespace.
    
    CROSS-FILE DUPLICATE: This exact function exists in user_management.py
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
    
    CROSS-FILE DUPLICATE: This exists in user_management.py
    """
    if not value or not isinstance(value, str):
        raise ValueError(f"{field_name} cannot be empty")
    if len(value.strip()) == 0:
        raise ValueError(f"{field_name} cannot be only whitespace")
    return True


def format_timestamp(timestamp: str) -> str:
    """Format ISO timestamp to readable string.
    
    CROSS-FILE DUPLICATE: This exists in user_management.py
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
    
    CROSS-FILE DUPLICATE: This exists in user_management.py
    """
    if not isinstance(data, dict):
        return default
    return data.get(key, default)


def build_response(success: bool, message: str, data: Any = None) -> Dict:
    """Build standardized response dictionary.
    
    CROSS-FILE DUPLICATE: This exists in user_management.py
    """
    response = {
        "success": success,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    if data is not None:
        response["data"] = data
    return response


def log_action(action: str, details: Dict) -> None:
    """Log action with timestamp.
    
    CROSS-FILE DUPLICATE: This exists in user_management.py
    """
    log_entry = {
        "action": action,
        "details": details,
        "timestamp": datetime.now().isoformat()
    }
    # In real code, this would write to a file or service
    print(f"[LOG] {json.dumps(log_entry)}")


def clean_text_input(text: str) -> str:
    """Clean text input - INTERNAL DUPLICATION #1.
    
    This is a duplicate of sanitize_string() above.
    """
    if not text:
        return ""
    # Remove special characters except spaces, letters, numbers
    cleaned = re.sub(r'[^\w\s-]', '', text)
    # Remove extra whitespace
    cleaned = ' '.join(cleaned.split())
    return cleaned.strip()


def parse_timestamp(timestamp: str) -> str:
    """Parse timestamp - INTERNAL DUPLICATION #2.
    
    This is a duplicate of format_timestamp() above.
    """
    if not timestamp:
        return "Unknown"
    try:
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return "Invalid Date"


def calculate_order_total(items: List[Dict]) -> Decimal:
    """Calculate total order amount.
    
    Note: Calculation logic is duplicated across multiple functions.
    """
    # Duplicated: Item total calculation
    subtotal = Decimal('0')
    for item in items:
        price = Decimal(str(item.get('price', 0)))
        quantity = int(item.get('quantity', 0))
        subtotal += price * quantity
    
    # Duplicated: Tax calculation
    tax_rate = Decimal('0.10')  # 10% tax
    tax = subtotal * tax_rate
    
    # Duplicated: Shipping calculation
    if subtotal < Decimal('50'):
        shipping = Decimal('5.99')
    elif subtotal < Decimal('100'):
        shipping = Decimal('3.99')
    else:
        shipping = Decimal('0')
    
    total = subtotal + tax + shipping
    
    # Log using duplicated function
    log_action("calculate_order", {"total": str(total)})
    
    return total


def calculate_invoice_total(items: List[Dict]) -> Dict[str, Decimal]:
    """Calculate invoice with breakdown.
    
    Note: Duplicates calculation logic from calculate_order_total.
    """
    # Duplicated: Item total calculation (exact copy)
    subtotal = Decimal('0')
    for item in items:
        price = Decimal(str(item.get('price', 0)))
        quantity = int(item.get('quantity', 0))
        subtotal += price * quantity
    
    # Duplicated: Tax calculation (exact copy)
    tax_rate = Decimal('0.10')  # 10% tax
    tax = subtotal * tax_rate
    
    # Duplicated: Shipping calculation (exact copy)
    if subtotal < Decimal('50'):
        shipping = Decimal('5.99')
    elif subtotal < Decimal('100'):
        shipping = Decimal('3.99')
    else:
        shipping = Decimal('0')
    
    total = subtotal + tax + shipping
    
    return {
        "subtotal": subtotal,
        "tax": tax,
        "shipping": shipping,
        "total": total
    }


def calculate_refund_amount(items: List[Dict], refund_items: List[Dict]) -> Decimal:
    """Calculate refund amount for returned items.
    
    Note: Duplicates calculation logic again.
    """
    # Duplicated: Item total calculation (exact copy)
    subtotal = Decimal('0')
    for item in refund_items:
        price = Decimal(str(item.get('price', 0)))
        quantity = int(item.get('quantity', 0))
        subtotal += price * quantity
    
    # Duplicated: Tax calculation (exact copy)
    tax_rate = Decimal('0.10')  # 10% tax
    tax = subtotal * tax_rate
    
    # Shipping not refunded for partial returns
    refund_total = subtotal + tax
    return refund_total


def validate_order_items(items: List[Dict]) -> bool:
    """Validate order items before processing.
    
    Note: Validation logic is duplicated.
    """
    # Duplicated: Item validation
    for item in items:
        # Check required fields
        if 'product_id' not in item:
            raise ValueError("Missing product_id")
        if 'price' not in item:
            raise ValueError("Missing price")
        if 'quantity' not in item:
            raise ValueError("Missing quantity")
        
        # Validate types and values
        price = item.get('price')
        if not isinstance(price, (int, float, Decimal)) or price <= 0:
            raise ValueError("Invalid price")
        
        quantity = item.get('quantity')
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid quantity")
    
    return True


def validate_refund_items(items: List[Dict]) -> bool:
    """Validate refund items before processing.
    
    Note: Duplicates validation from validate_order_items.
    """
    # Duplicated: Item validation (exact copy)
    for item in items:
        # Check required fields
        if 'product_id' not in item:
            raise ValueError("Missing product_id")
        if 'price' not in item:
            raise ValueError("Missing price")
        if 'quantity' not in item:
            raise ValueError("Missing quantity")
        
        # Validate types and values
        price = item.get('price')
        if not isinstance(price, (int, float, Decimal)) or price <= 0:
            raise ValueError("Invalid price")
        
        quantity = item.get('quantity')
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid quantity")
    
    return True


def apply_discount_code(total: Decimal, code: str) -> Decimal:
    """Apply discount code to order total.
    
    Note: Discount logic is duplicated.
    """
    # Duplicated: Discount code logic
    discounts = {
        "SAVE10": Decimal('0.10'),
        "SAVE20": Decimal('0.20'),
        "SUMMER": Decimal('0.15'),
        "WINTER": Decimal('0.15'),
    }
    
    code_upper = code.upper()
    if code_upper in discounts:
        discount_rate = discounts[code_upper]
        discount_amount = total * discount_rate
        return total - discount_amount
    
    return total


def apply_promotional_discount(subtotal: Decimal, promo_code: str) -> Decimal:
    """Apply promotional discount to subtotal.
    
    Note: Duplicates discount logic from apply_discount_code.
    """
    # Duplicated: Discount code logic (exact copy)
    discounts = {
        "SAVE10": Decimal('0.10'),
        "SAVE20": Decimal('0.20'),
        "SUMMER": Decimal('0.15'),
        "WINTER": Decimal('0.15'),
    }
    
    code_upper = promo_code.upper()
    if code_upper in discounts:
        discount_rate = discounts[code_upper]
        discount_amount = subtotal * discount_rate
        return subtotal - discount_amount
    
    return subtotal


def format_price(amount: Decimal) -> str:
    """Format price for display.
    
    Note: Formatting logic is duplicated.
    """
    # Duplicated: Price formatting
    amount_str = f"{amount:.2f}"
    parts = amount_str.split('.')
    integer_part = parts[0]
    decimal_part = parts[1]
    
    # Add thousand separators
    formatted = ""
    for i, digit in enumerate(reversed(integer_part)):
        if i > 0 and i % 3 == 0:
            formatted = "," + formatted
        formatted = digit + formatted
    
    return f"${formatted}.{decimal_part}"


def format_invoice_amount(amount: Decimal) -> str:
    """Format invoice amount for display.
    
    Note: Duplicates formatting from format_price.
    """
    # Duplicated: Price formatting (exact copy)
    amount_str = f"{amount:.2f}"
    parts = amount_str.split('.')
    integer_part = parts[0]
    decimal_part = parts[1]
    
    # Add thousand separators
    formatted = ""
    for i, digit in enumerate(reversed(integer_part)):
        if i > 0 and i % 3 == 0:
            formatted = "," + formatted
        formatted = digit + formatted
    
    return f"${formatted}.{decimal_part}"


def generate_order_summary(order: Dict) -> str:
    """Generate order summary text.
    
    Note: Contains duplicated string building.
    """
    # Duplicated: Summary building
    lines = []
    lines.append("="*50)
    lines.append("ORDER SUMMARY")
    lines.append("="*50)
    lines.append(f"Order ID: {order.get('id', 'N/A')}")
    lines.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    
    items = order.get('items', [])
    for item in items:
        name = item.get('name', 'Unknown')
        qty = item.get('quantity', 0)
        price = item.get('price', 0)
        lines.append(f"  {name} x{qty} @ {format_price(Decimal(str(price)))}")
    
    lines.append("")
    lines.append(f"Total: {format_price(order.get('total', Decimal('0')))}")
    lines.append("="*50)
    
    return "\n".join(lines)


def generate_invoice_summary(invoice: Dict) -> str:
    """Generate invoice summary text.
    
    Note: Duplicates summary building from generate_order_summary.
    """
    # Duplicated: Summary building (similar pattern)
    lines = []
    lines.append("="*50)
    lines.append("INVOICE")
    lines.append("="*50)
    lines.append(f"Invoice ID: {invoice.get('id', 'N/A')}")
    lines.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    
    items = invoice.get('items', [])
    for item in items:
        name = item.get('name', 'Unknown')
        qty = item.get('quantity', 0)
        price = item.get('price', 0)
        lines.append(f"  {name} x{qty} @ {format_price(Decimal(str(price)))}")
    
    lines.append("")
    lines.append(f"Subtotal: {format_invoice_amount(invoice.get('subtotal', Decimal('0')))}")
    lines.append(f"Tax: {format_invoice_amount(invoice.get('tax', Decimal('0')))}")
    lines.append(f"Shipping: {format_invoice_amount(invoice.get('shipping', Decimal('0')))}")
    lines.append(f"Total: {format_invoice_amount(invoice.get('total', Decimal('0')))}")
    lines.append("="*50)
    
    return "\n".join(lines)


def make_success_response(message: str, data: Any = None) -> Dict:
    """Make success response - INTERNAL DUPLICATION #3.
    
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


def make_error_response(message: str) -> Dict:
    """Make error response - INTERNAL DUPLICATION #4.
    
    This also duplicates build_response() above.
    """
    response = {
        "success": False,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    return response


def get_dict_value(data: Dict, key: str, default: Any = None) -> Any:
    """Get value from dict safely - INTERNAL DUPLICATION #5.
    
    This duplicates safe_get() above.
    """
    if not isinstance(data, dict):
        return default
    return data.get(key, default)


def validate_string_field(value: str, field_name: str) -> bool:
    """Validate string field - INTERNAL DUPLICATION #6.
    
    This duplicates validate_non_empty_string() above.
    """
    if not value or not isinstance(value, str):
        raise ValueError(f"{field_name} cannot be empty")
    if len(value.strip()) == 0:
        raise ValueError(f"{field_name} cannot be only whitespace")
    return True


if __name__ == "__main__":
    print("Order Processing Module - Demonstrating Code Duplication\n")
    print("="*60)
    print("DEMONSTRATING INTERNAL AND CROSS-FILE DUPLICATION")
    print("="*60)
    
    # Test duplicated utility functions
    print("\n1. Testing DUPLICATED sanitize functions:")
    test_text = "  Product@Name#456  "
    print(f"   Input: '{test_text}'")
    print(f"   sanitize_string(): '{sanitize_string(test_text)}'")
    print(f"   clean_text_input(): '{clean_text_input(test_text)}'")
    print("   ^ These are INTERNAL duplicates")
    
    print("\n2. Testing DUPLICATED timestamp functions:")
    now = datetime.now().isoformat()
    print(f"   format_timestamp(): {format_timestamp(now)}")
    print(f"   parse_timestamp(): {parse_timestamp(now)}")
    print("   ^ These are INTERNAL duplicates")
    
    print("\n3. Testing DUPLICATED dict getter functions:")
    test_dict = {"key": "value", "count": 42}
    print(f"   safe_get(): {safe_get(test_dict, 'key', 'default')}")
    print(f"   get_dict_value(): {get_dict_value(test_dict, 'key', 'default')}")
    print("   ^ These are INTERNAL duplicates")
    
    print("\n4. Testing DUPLICATED response builders:")
    print(f"   build_response(): {build_response(True, 'OK', {'id': 100})}")
    print(f"   make_success_response(): {make_success_response('OK', {'id': 100})}")
    print(f"   make_error_response(): {make_error_response('Error')}")
    print("   ^ These are INTERNAL duplicates")
    
    print("\n" + "="*60 + "\n")
    
    # Test order calculation
    test_items = [
        {"product_id": 1, "name": "Widget", "price": 19.99, "quantity": 2},
        {"product_id": 2, "name": "Gadget", "price": 29.99, "quantity": 1},
    ]
    
    print("Validating items...")
    validate_order_items(test_items)
    print("✓ Items valid\n")
    
    total = calculate_order_total(test_items)
    print(f"Order total: {format_price(total)}\n")
    
    invoice = calculate_invoice_total(test_items)
    print("Invoice breakdown:")
    print(f"  Subtotal: {format_price(invoice['subtotal'])}")
    print(f"  Tax: {format_price(invoice['tax'])}")
    print(f"  Shipping: {format_price(invoice['shipping'])}")
    print(f"  Total: {format_price(invoice['total'])}")
    
    print("\n" + "="*60 + "\n")
    
    # Test discount
    discounted = apply_discount_code(total, "SAVE10")
    print(f"After SAVE10 discount: {format_price(discounted)}\n")
    
    # Test order summary
    order = {
        "id": "ORD-12345",
        "items": test_items,
        "total": total
    }
    print(generate_order_summary(order))
    
    print("\n" + "="*60)
    print("NOTE: Many utility functions in this file also exist in")
    print("      user_management.py (CROSS-FILE DUPLICATION)")
    print("="*60)
