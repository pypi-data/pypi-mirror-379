"""
Core functionality for TF AI Agents.
"""


def hello_world(input_data, debug=False):
    """
    A simple function that returns the same output as input.
    
    Args:
        input_data: Any input data to be returned as output
        debug (bool, optional): If True, prints "Hello World" to console. Defaults to False.
    
    Returns:
        The same data that was passed as input_data
    
    Example:
        >>> hello_world("test")
        "test"
        >>> hello_world("test", debug=True)
        Hello World
        "test"
    """
    if debug:
        print("Hello World")
    
    return input_data
