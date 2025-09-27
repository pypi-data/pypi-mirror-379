def greet(name: str | None = None) -> str:
    """Return a friendly greeting."""
    if not name:
        name = "World"
    return f"Hello, {name}!"


def farewell(name: str | None = None) -> str:
    """Return a friendly farewell."""
    if not name:
        name = "Friend"
    return f"Goodbye, {name}!"


def shout(message: str) -> str:
    """Return the message in uppercase with exclamation."""
    return message.upper() + "!"