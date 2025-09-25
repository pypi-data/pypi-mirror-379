"""Tests for DG213ExamplesSectionValidation rule."""

import pytest

from dococtopy.adapters.python.adapter import PythonSymbol
from dococtopy.rules.python.google_style import DG213ExamplesSectionValidation


class TestDG213ExamplesSectionValidation:
    """Test cases for DG213ExamplesSectionValidation rule."""

    def _parse_code(self, code: str) -> list[PythonSymbol]:
        """Parse code and return symbols."""
        import ast

        tree = ast.parse(code)
        symbols = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                docstring = ast.get_docstring(node)
                symbols.append(
                    PythonSymbol(
                        name=node.name,
                        kind="function",
                        lineno=node.lineno,
                        col=node.col_offset,
                        docstring=docstring,
                        ast_node=node,
                    )
                )

        return symbols

    def test_complex_function_with_examples_section_passes(self):
        """Test that complex functions with Examples section pass."""
        code = '''
def complex_calculation(data, threshold, options=None):
    """Perform complex calculation with multiple parameters.

    Args:
        data: Input data for calculation.
        threshold: Threshold value for filtering.
        options: Optional configuration dictionary.

    Returns:
        Dict[str, Any]: Calculation results.

    Examples:
        >>> result = complex_calculation([1, 2, 3], 2.0)
        >>> print(result['sum'])
        6
    """
    if options is None:
        options = {}
    
    filtered_data = [x for x in data if x > threshold]
    result = {
        'sum': sum(filtered_data),
        'count': len(filtered_data),
        'average': sum(filtered_data) / len(filtered_data) if filtered_data else 0
    }
    return result
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_complex_function_without_examples_section_fails(self):
        """Test that complex functions without Examples section fail."""
        code = '''
def complex_calculation(data, threshold, options=None):
    """Perform complex calculation with multiple parameters.

    Args:
        data: Input data for calculation.
        threshold: Threshold value for filtering.
        options: Optional configuration dictionary.

    Returns:
        Dict[str, Any]: Calculation results.
    """
    if options is None:
        options = {}
    
    filtered_data = [x for x in data if x > threshold]
    result = {
        'sum': sum(filtered_data),
        'count': len(filtered_data),
        'average': sum(filtered_data) / len(filtered_data) if filtered_data else 0
    }
    return result
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG213"
        assert "Complex function should have Examples section" in findings[0].message
        assert findings[0].level.value == "info"

    def test_simple_function_passes(self):
        """Test that simple functions pass."""
        code = '''
def add_numbers(a, b):
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        int: Sum of the two numbers.
    """
    return a + b
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_no_docstring_passes(self):
        """Test that functions without docstrings pass."""
        code = """
def complex_calculation(data, threshold, options=None):
    if options is None:
        options = {}
    
    filtered_data = [x for x in data if x > threshold]
    result = {
        'sum': sum(filtered_data),
        'count': len(filtered_data),
        'average': sum(filtered_data) / len(filtered_data) if filtered_data else 0
    }
    return result
"""
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_complex_function_with_examples_section_passes(self):
        """Test that async complex functions with Examples section pass."""
        code = '''
async def async_data_processor(urls, timeout=30, retries=3):
    """Process multiple URLs asynchronously.

    Args:
        urls: List of URLs to process.
        timeout: Request timeout in seconds.
        retries: Number of retry attempts.

    Returns:
        List[Dict[str, Any]]: Processing results.

    Examples:
        >>> urls = ['http://example.com', 'http://test.com']
        >>> results = await async_data_processor(urls)
        >>> len(results)
        2
    """
    import asyncio
    import aiohttp
    
    async def fetch_url(session, url):
        for attempt in range(retries):
            try:
                async with session.get(url, timeout=timeout) as response:
                    return {'url': url, 'status': response.status, 'data': await response.text()}
            except Exception as e:
                if attempt == retries - 1:
                    return {'url': url, 'error': str(e)}
                await asyncio.sleep(1)
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_async_complex_function_without_examples_section_fails(self):
        """Test that async complex functions without Examples section fail."""
        code = '''
async def async_data_processor(urls, timeout=30, retries=3):
    """Process multiple URLs asynchronously.

    Args:
        urls: List of URLs to process.
        timeout: Request timeout in seconds.
        retries: Number of retry attempts.

    Returns:
        List[Dict[str, Any]]: Processing results.
    """
    import asyncio
    import aiohttp
    
    async def fetch_url(session, url):
        for attempt in range(retries):
            try:
                async with session.get(url, timeout=timeout) as response:
                    return {'url': url, 'status': response.status, 'data': await response.text()}
            except Exception as e:
                if attempt == retries - 1:
                    return {'url': url, 'error': str(e)}
                await asyncio.sleep(1)
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG213"
        assert "Complex function should have Examples section" in findings[0].message
        assert findings[0].level.value == "info"

    def test_function_with_multiple_examples_passes(self):
        """Test that functions with multiple examples pass."""
        code = '''
def parse_config_file(filepath, validate=True, encoding='utf-8'):
    """Parse configuration file with validation.

    Args:
        filepath: Path to configuration file.
        validate: Whether to validate the configuration.
        encoding: File encoding to use.

    Returns:
        Dict[str, Any]: Parsed configuration.

    Examples:
        >>> config = parse_config_file('config.json')
        >>> 'database' in config
        True
        
        >>> config = parse_config_file('config.yaml', validate=False)
        >>> isinstance(config, dict)
        True
    """
    import json
    import yaml
    
    with open(filepath, 'r', encoding=encoding) as f:
        if filepath.endswith('.json'):
            config = json.load(f)
        elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
            config = yaml.safe_load(f)
        else:
            raise ValueError(f"Unsupported file format: {filepath}")
    
    if validate:
        validate_config(config)
    
    return config
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_complex_logic_and_examples_passes(self):
        """Test that functions with complex logic and examples pass."""
        code = '''
def advanced_search(query, filters=None, sort_by='relevance', limit=10):
    """Perform advanced search with multiple filters and sorting.

    Args:
        query: Search query string.
        filters: Dictionary of filter criteria.
        sort_by: Field to sort results by.
        limit: Maximum number of results to return.

    Returns:
        List[Dict[str, Any]]: Search results.

    Examples:
        >>> results = advanced_search('python tutorial')
        >>> len(results) <= 10
        True
        
        >>> results = advanced_search('python', {'category': 'programming'}, 'date')
        >>> all('python' in r['title'].lower() for r in results)
        True
    """
    if filters is None:
        filters = {}
    
    # Complex search logic
    base_query = build_base_query(query)
    filtered_query = apply_filters(base_query, filters)
    sorted_results = sort_results(filtered_query, sort_by)
    
    return sorted_results[:limit]
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_nested_functions_and_examples_passes(self):
        """Test that functions with nested functions and examples pass."""
        code = '''
def data_transformer(input_data, transformations):
    """Transform data using multiple transformation functions.

    Args:
        input_data: Input data to transform.
        transformations: List of transformation functions.

    Returns:
        Any: Transformed data.

    Examples:
        >>> data = [1, 2, 3, 4, 5]
        >>> transforms = [lambda x: x * 2, lambda x: x + 1]
        >>> result = data_transformer(data, transforms)
        >>> result[0]
        3
    """
    def apply_transformation(data, transform_func):
        if isinstance(data, list):
            return [transform_func(item) for item in data]
        else:
            return transform_func(data)
    
    result = input_data
    for transform in transformations:
        result = apply_transformation(result, transform)
    
    return result
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_exception_handling_and_examples_passes(self):
        """Test that functions with exception handling and examples pass."""
        code = '''
def safe_file_operation(filepath, operation='read', data=None):
    """Safely perform file operations with error handling.

    Args:
        filepath: Path to the file.
        operation: Operation to perform ('read', 'write', 'append').
        data: Data to write (for write/append operations).

    Returns:
        Any: Operation result.

    Raises:
        FileNotFoundError: When file doesn't exist for read operations.
        PermissionError: When file permissions are insufficient.

    Examples:
        >>> result = safe_file_operation('test.txt', 'read')
        >>> isinstance(result, str)
        True
        
        >>> safe_file_operation('test.txt', 'write', 'Hello World')
        'File written successfully'
    """
    try:
        if operation == 'read':
            with open(filepath, 'r') as f:
                return f.read()
        elif operation == 'write':
            with open(filepath, 'w') as f:
                f.write(data)
                return 'File written successfully'
        elif operation == 'append':
            with open(filepath, 'a') as f:
                f.write(data)
                return 'Data appended successfully'
        else:
            raise ValueError(f"Unknown operation: {operation}")
    except FileNotFoundError:
        if operation == 'read':
            raise
        else:
            # Create file for write operations
            with open(filepath, 'w') as f:
                f.write(data)
                return 'File created and written successfully'
    except PermissionError:
        raise
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_function_with_class_instantiation_and_examples_passes(self):
        """Test that functions with class instantiation and examples pass."""
        code = '''
def create_database_connection(config):
    """Create database connection with configuration.

    Args:
        config: Database configuration dictionary.

    Returns:
        DatabaseConnection: Configured database connection.

    Examples:
        >>> config = {'host': 'localhost', 'port': 5432, 'database': 'test'}
        >>> conn = create_database_connection(config)
        >>> conn.is_connected()
        True
    """
    class DatabaseConnection:
        def __init__(self, host, port, database, username=None, password=None):
            self.host = host
            self.port = port
            self.database = database
            self.username = username
            self.password = password
            self._connected = False
        
        def connect(self):
            # Simulate connection logic
            self._connected = True
        
        def is_connected(self):
            return self._connected
    
    conn = DatabaseConnection(
        host=config['host'],
        port=config['port'],
        database=config['database'],
        username=config.get('username'),
        password=config.get('password')
    )
    conn.connect()
    return conn
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0

    def test_multiple_complex_functions_without_examples(self):
        """Test that multiple complex functions without examples are all detected."""
        code = '''
def function1(data, threshold, options=None):
    """First complex function without examples."""
    if options is None:
        options = {}
    
    filtered_data = [x for x in data if x > threshold]
    result = {
        'sum': sum(filtered_data),
        'count': len(filtered_data),
        'average': sum(filtered_data) / len(filtered_data) if filtered_data else 0
    }
    return result

def function2(urls, timeout=30, retries=3):
    """Second complex function without examples."""
    import asyncio
    import aiohttp
    
    async def fetch_url(session, url):
        for attempt in range(retries):
            try:
                async with session.get(url, timeout=timeout) as response:
                    return {'url': url, 'status': response.status, 'data': await response.text()}
            except Exception as e:
                if attempt == retries - 1:
                    return {'url': url, 'error': str(e)}
                await asyncio.sleep(1)
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 2
        assert all(f.rule_id == "DG213" for f in findings)
        assert all(
            "Complex function should have Examples section" in f.message
            for f in findings
        )

    def test_mixed_functions_complex_without_examples(self):
        """Test mixed functions where only complex without examples is detected."""
        code = '''
def simple_add(a, b):
    """Simple function that doesn't need examples."""
    return a + b

def complex_calculation(data, threshold, options=None):
    """Complex function without examples."""
    if options is None:
        options = {}
    
    filtered_data = [x for x in data if x > threshold]
    result = {
        'sum': sum(filtered_data),
        'count': len(filtered_data),
        'average': sum(filtered_data) / len(filtered_data) if filtered_data else 0
    }
    return result
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 1
        assert findings[0].rule_id == "DG213"
        assert "Complex function should have Examples section" in findings[0].message
        assert findings[0].symbol == "complex_calculation"

    def test_function_with_examples_and_other_sections_passes(self):
        """Test that functions with Examples section and other sections pass."""
        code = '''
def comprehensive_function(data, config):
    """Comprehensive function with all sections.

    Args:
        data: Input data.
        config: Configuration dictionary.

    Returns:
        Dict[str, Any]: Processed results.

    Raises:
        ValueError: When data is invalid.
        TypeError: When config is not a dictionary.

    Examples:
        >>> result = comprehensive_function([1, 2, 3], {'multiply': 2})
        >>> result['processed']
        [2, 4, 6]

    Note:
        This function performs comprehensive data processing.
    """
    if not isinstance(data, list):
        raise ValueError("Data must be a list")
    
    if not isinstance(config, dict):
        raise TypeError("Config must be a dictionary")
    
    processed_data = [x * config.get('multiply', 1) for x in data]
    
    return {
        'processed': processed_data,
        'count': len(processed_data),
        'sum': sum(processed_data)
    }
'''
        symbols = self._parse_code(code)
        rule = DG213ExamplesSectionValidation()
        findings = rule.check(symbols=symbols)

        assert len(findings) == 0
