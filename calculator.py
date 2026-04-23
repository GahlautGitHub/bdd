def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return a multiplied by b."""
    return a * b


def suare(a):
    """Return a square by a."""
    return a**2


def area(radius):
    """Return the area of a circle given its radius."""
    pi = 3.14
    return pi * radius * radius


def divide(a, b):
    """Return a divided by b. Raises ValueError for zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
