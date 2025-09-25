"""Result from Claude Haiku 3 (Budget) model."""

"""Enhanced test fixture with nested functions and classes for model comparison."""

def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


def process_user_data(user_id, include_metadata=False):
    """Processes user data.
    
    Args:
        user_id (int): Unique identifier for the user.
        include_metadata (bool): Whether to include additional metadata about the user.
    
    Returns:
        dict: User data, including any requested metadata.
    """

    # Process user data
    pass


class UserManager:
    """Manages user records and operations."""
    
    def __init__(self, database_url):
    """Initialize the database connection.
    
    Args:
        database_url (str): The URL of the database to connect to.
    """

        # Initialize user manager
        self.db_url = database_url

    def create_user(self, username, email):
    """Create a new user.
    
    Args:
        username (str): The username for the new user.
        email (str): The email address for the new user.
    """

        # Create new user
        pass

    def get_user(self, user_id):
    """Get a user by their ID.
    
    Args:
        user_id (int): The unique identifier for the user.
    
    Returns:
        dict: A dictionary containing the user's information.
    """

        # Get user by ID
        pass

    def _private_method(self):
        # Private method
        pass

    def __str__(self):
        # String representation
        return f"UserManager(db_url={self.db_url})"


def outer_function():
    """Implements the outer function.
    """

    # Outer function
    def inner_function():
    """Implements the core functionality of the outer function.
    """

        # Inner function
        pass
    
    return inner_function


class OuterClass:
    """Outer class for testing nested structures."""
    
    def __init__(self):
    """Initializes the object.
    """

        # Initialize outer class
        pass
    
    class InnerClass:
    """Implements the functionality of the outer class.
    """

        # Inner class
        def __init__(self):
    """Initializes the object.
    """

            # Initialize inner class
            pass
        
        def inner_method(self):
    """Implements the core functionality of the class.
    """

            # Inner method
            def nested_function():
    """Implements a nested function.
    """

                # Nested function
                pass
            return nested_function
