"""Scenario 5: Comprehensive Google style docstring patterns."""


def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number.

    Args:
        n: The position in the Fibonacci sequence to calculate
    """
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


def process_user_data(user_id, include_metadata=False):
    # Process user data
    pass


class UserManager:
    """User management class.

    Args:
        database_url: URL to the database
    """

    def __init__(self, database_url):
        self.db_url = database_url

    def create_user(self, username, email):
        """Create a new user.

        Args:
            username: The username
            email: The email address
        """
        # Create new user
        pass

    def get_user(self, user_id):
        # Get user by ID
        pass


def validate_email(email):
    """Validates whether an email address is valid.

    Args:
        email: The email address to validate
    """
    import re

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None
