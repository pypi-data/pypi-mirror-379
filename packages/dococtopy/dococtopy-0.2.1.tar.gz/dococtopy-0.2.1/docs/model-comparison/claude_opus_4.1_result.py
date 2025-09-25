"""Result from Claude Opus 4.1 (Premium) model."""

"""Enhanced test fixture with nested functions and classes for model comparison."""

def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


def process_user_data(user_id, include_metadata=False):
    """Process user data for a given user ID.
    
    Args:
        user_id: The unique identifier of the user to process.
        include_metadata: Whether to include additional metadata in the processed data.
    """

    # Process user data
    pass


class UserManager:
    """Manages user records and operations."""
    
    def __init__(self, database_url):
    """Initialize the database connection handler.
    
    Args:
        database_url: The URL string for connecting to the database.
            Should be in the format appropriate for the database type
            (e.g., 'postgresql://user:password@host:port/dbname').
    """

        # Initialize user manager
        self.db_url = database_url

    def create_user(self, username, email):
    """Create a new user.
    
    Args:
        username: The username for the new user.
        email: The email address for the new user.
    """

        # Create new user
        pass

    def get_user(self, user_id):
    """Retrieve a user by their ID.
    
    Args:
        user_id: The unique identifier of the user to retrieve.
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
    """Execute the outer function logic.
    
    This function serves as an outer wrapper or container function
    that performs its designated operations.
    """

    # Outer function
    def inner_function():
    """Execute the inner function logic.
    
    This function performs the core implementation logic as an inner function.
    It encapsulates specific functionality within its parent scope.
    """

        # Inner function
        pass
    
    return inner_function


class OuterClass:
    """Outer class for testing nested structures."""
    
    def __init__(self):
    """Initialize a new instance of the class.
    
    This constructor initializes the object with default settings.
    No parameters are required for initialization.
    """

        # Initialize outer class
        pass
    
    class InnerClass:
    """Inner class for encapsulating related functionality.
    
    This class provides internal implementation details and helper methods
    that support the parent class's operations.
    
    Attributes:
        None: No attributes are currently defined in this implementation.
    
    Methods:
        None: No methods are currently defined in this implementation.
    
    Note:
        This is an inner class and should typically not be instantiated
        directly outside of its parent class context.
    """

        # Inner class
        def __init__(self):
    """Initialize a new instance of the class.
    
    This constructor initializes the object with default settings.
    No parameters are required for initialization.
    """

            # Initialize inner class
            pass
        
        def inner_method(self):
    """Execute the inner method logic.
    
    This method performs the core implementation logic for the class instance.
    """

            # Inner method
            def nested_function():
    """Execute a nested function operation.
    
    This function performs nested operations or demonstrates nested function behavior.
    """

                # Nested function
                pass
            return nested_function
