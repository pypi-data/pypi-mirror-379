"""Enhanced test fixture with nested functions and classes for model comparison."""


def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


def process_user_data(user_id, include_metadata=False):
    # Process user data
    pass


class UserManager:
    """Manages user records and operations."""

    def __init__(self, database_url):
        # Initialize user manager
        self.db_url = database_url

    def create_user(self, username, email):
        # Create new user
        pass

    def get_user(self, user_id):
        # Get user by ID
        pass

    def _private_method(self):
        # Private method
        pass


def outer_function():
    """Outer function with nested function."""

    def inner_function():
        # Nested function
        pass

    return inner_function


class OuterClass:
    """Outer class with nested class."""

    class InnerClass:
        # Nested class
        pass

    def method_with_nested_function(self):
        """Method with nested function."""

        def nested_function():
            # Nested function inside method
            pass

        return nested_function


def validate_email(email):
    """Validate an email address."""
    import re

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def simple_pass_function():
    # Simple function with pass
    pass


def another_simple_function():
    # Another simple function
    return None
