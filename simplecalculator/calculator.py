def add(a, b):
    """Perform addition."""
    return a + b


def subtract(a, b):
    """Perform subtraction."""
    return a - b


def multiply(a, b):
    """Perform multiplication."""
    return a * b


def divide(a, b):
    """Perform division."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
