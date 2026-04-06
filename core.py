"""Core functionality for project6.

This project demonstrates advanced multi-project dependencies.
It depends on project5, project3, and uses features from project1 and project2.
"""

from project5 import ultra_greet
from project3 import super_greet
from project2 import format_message, add_prefix, count_words
from project1 import greet


def supreme_greet(name: str, style: str = "default") -> str:
    """Return the supreme greeting combining all project features.
    
    Args:
        name: The name to greet
        style: Message style (default, uppercase, title, reverse)
    
    Returns:
        Supreme greeting message combining all projects
    """
    ultra_msg = ultra_greet(name)
    formatted = format_message(ultra_msg, style)
    prefixed = add_prefix(formatted, "[SUPREME]")
    return f"{prefixed} - The ultimate greeting from project6!"


def aggregate_messages(names: list[str]) -> dict:
    """Aggregate greetings for multiple names.
    
    Args:
        names: List of names to greet
    
    Returns:
        Dictionary with name as key and greeting info as value
    """
    results = {}
    for name in names:
        basic = greet(name)
        super_msg = super_greet(name)
        ultra_msg = ultra_greet(name)
        
        results[name] = {
            "basic": basic,
            "super": super_msg,
            "ultra": ultra_msg,
            "word_count": count_words(ultra_msg),
            "formatted_upper": format_message(ultra_msg, "uppercase"),
            "formatted_title": format_message(ultra_msg, "title")
        }
    
    return results


def create_report(data: dict, title: str = "Report") -> str:
    """Create a formatted report from data.
    
    Args:
        data: Dictionary of data to report
        title: Report title
    
    Returns:
        Formatted report string
    """
    lines = [
        "=" * 60,
        format_message(title, "uppercase"),
        "=" * 60,
        ""
    ]
    
    for key, value in data.items():
        lines.append(add_prefix(f"{key}: {value}", "[DATA]"))
    
    lines.append("")
    lines.append("=" * 60)
    lines.append(f"Total entries: {len(data)}")
    lines.append("=" * 60)
    
    return "\n".join(lines)


def validate_input(value: str, min_length: int = 1, max_length: int = 100) -> tuple[bool, str]:
    """Validate input string.
    
    Args:
        value: String to validate
        min_length: Minimum required length
        max_length: Maximum allowed length
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not value:
        return False, "Value cannot be empty"
    
    if len(value) < min_length:
        return False, f"Value must be at least {min_length} characters"
    
    if len(value) > max_length:
        return False, f"Value must be at most {max_length} characters"
    
    return True, "Valid"


def transform_data(items: list, transform_type: str = "greet") -> list:
    """Transform a list of items using various greeting functions.
    
    Args:
        items: List of items (names) to transform
        transform_type: Type of transformation (greet, super, ultra, supreme)
    
    Returns:
        List of transformed items
    """
    transform_funcs = {
        "greet": greet,
        "super": super_greet,
        "ultra": ultra_greet,
        "supreme": lambda x: supreme_greet(x, "default")
    }
    
    func = transform_funcs.get(transform_type, greet)
    return [func(item) for item in items]
