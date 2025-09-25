"""Scenario 1: Missing docstrings for functions and classes."""


def calculate_fibonacci(n):
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


def process_user_data(user_id, include_metadata=False):
    # Process user data
    pass


class UserManager:
    def __init__(self, database_url):
        self.db_url = database_url

    def create_user(self, username, email):
        # Create new user
        pass

    def get_user(self, user_id):
        # Get user by ID
        pass


def validate_email(email):
    import re

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None
