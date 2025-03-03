def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b


def greet(name: str) -> str:
    """Greets the person with the provided name."""
    return f"Hello, {name}!"


def divide(a: int, b: int) -> float:
    """Divides a by b and returns a float."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

#asd
print(add(3, 5))  # This will raise an error
print(greet("hi"))  # This will raise an error
print(divide(10, 2))  # This will raise an error