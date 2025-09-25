"""Result from GPT-5 Mini (Premium) model."""

"""Enhanced test fixture with nested functions and classes for model comparison."""

def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


def process_user_data(user_id, include_metadata=False):
    """Process and return data for a given user.
    
    Processes and returns data for the specified user. The returned dictionary typically includes 'profile' and 'preferences'. If include_metadata is True, the dictionary will also include a 'metadata' key containing timestamps and source information.
    
    Args:
        user_id (int or str): Unique identifier of the user.
        include_metadata (bool): Whether to include additional metadata. If True, the returned data will include metadata such as timestamps and source information.
    
    Returns:
        dict: Dictionary containing the user's data. Common keys are 'profile' and 'preferences'; includes 'metadata' when include_metadata is True.
    """

    # Process user data
    pass


class UserManager:
    """Manages user records and operations."""
    
    def __init__(self, database_url):
    """Initialize the instance with the provided database URL.
    
    Args:
        database_url (str): Database connection URL/DSN (e.g., "postgresql://user:pass@host:port/dbname").
    
    Attributes:
        database_url (str): The raw database URL provided.
    """

        # Initialize user manager
        self.db_url = database_url

    def create_user(self, username, email):
    """Create a new user account and return the created user object.
    
    Args:
        username (str): Desired username for the new user.
        email (str): Email address for the new user.
    
    Returns:
        object: The newly created user object.
    """

        # Create new user
        pass

    def get_user(self, user_id):
    """Retrieve a user by their unique identifier.
    
    Retrieve the user object corresponding to the provided user_id.
    
    Args:
        user_id (int or str): The unique identifier of the user to retrieve. The type depends on the application's user ID scheme.
    
    Returns:
        object or None: The user object corresponding to the provided user_id, or None if no user is found.
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
    """Outer function placeholder.
    
    This function serves as the outer entry point for the surrounding implementation. Replace or extend this function with the desired behavior for the encompassing module or workflow.
    """

    # Outer function
    def inner_function():
    """Internal helper for the enclosing operation.
    
    Implements the core computation used by the enclosing operation. This function is intended for internal use only and is not part of the public API. It may have side effects such as modifying shared state or performing I/O. Implementation-specific exceptions (for example, ValueError or RuntimeError) may be raised depending on runtime conditions; document concrete exceptions in a Raises section when they are known.
    """

        # Inner function
        pass
    
    return inner_function


class OuterClass:
    """Outer class for testing nested structures."""
    
    def __init__(self):
    """Initialize a new instance of the class.
    
    Performs any necessary setup for the object. This constructor initializes instance attributes and documents any side effects.
    
    Notes:
        If the constructor performs side effects (for example, opening files,
        acquiring resources, or starting background threads), describe them here.
    """

        # Initialize outer class
        pass
    
    class InnerClass:
    """Inner helper class used by the surrounding implementation.
    
    This class encapsulates functionality and state intended for internal use by the enclosing module or outer class. It groups related behavior to keep the outer implementation modular and testable.
    
    Attributes:
        Instance attributes are defined in the constructor. Document each attribute here using the format:
            name (type): Description of the attribute.
    
    Methods:
        Document public methods here using the format:
            method_name(arg1, arg2) -> return_type: Brief description of what the method does.
    
    Notes:
        Update this docstring with constructor parameters, attribute descriptions, and method details to provide a complete API reference for consumers and maintainers.
    """

        # Inner class
        def __init__(self):
    """Initialize a new instance of the class.
    
    Performs any necessary setup for the object. This constructor initializes instance attributes and documents any side effects.
    
    Notes:
        If the constructor performs side effects (for example, opening files,
        acquiring resources, or starting background threads), describe them here.
    """

            # Initialize inner class
            pass
        
        def inner_method(self):
    """Perform the inner operation for this instance.
    
    This method contains the internal implementation logic used by the public API. Subclasses may override it to customize behavior. It operates on the instance and does not return a value.
    """

            # Inner method
            def nested_function():
    """Nested helper function.
    
    Placeholder implementation used by an enclosing context. Replace or extend this function to perform the specific computation required by the caller.
    
    Returns:
        The result produced by the nested function, or None if no value is produced.
    """

                # Nested function
                pass
            return nested_function
