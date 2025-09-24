"""
Tests for the core module.
"""

import pytest
from tf_ai_agents.core import hello_world


class TestHelloWorld:
    """Test cases for the hello_world function."""

    def test_hello_world_basic(self):
        """Test basic functionality without debug."""
        result = hello_world("test input")
        assert result == "test input"

    def test_hello_world_with_debug(self, capsys):
        """Test functionality with debug enabled."""
        result = hello_world("test input", debug=True)
        assert result == "test input"
        
        # Check that debug message was printed
        captured = capsys.readouterr()
        assert "Hello World" in captured.out

    def test_hello_world_without_debug(self, capsys):
        """Test functionality with debug disabled."""
        result = hello_world("test input", debug=False)
        assert result == "test input"
        
        # Check that no debug message was printed
        captured = capsys.readouterr()
        assert "Hello World" not in captured.out

    def test_hello_world_default_debug(self, capsys):
        """Test that debug defaults to False."""
        result = hello_world("test input")
        assert result == "test input"
        
        # Check that no debug message was printed
        captured = capsys.readouterr()
        assert "Hello World" not in captured.out

    def test_hello_world_different_inputs(self):
        """Test with different types of input."""
        # Test with string
        assert hello_world("string") == "string"
        
        # Test with number
        assert hello_world(42) == 42
        
        # Test with list
        test_list = [1, 2, 3]
        assert hello_world(test_list) == test_list
        
        # Test with dict
        test_dict = {"key": "value"}
        assert hello_world(test_dict) == test_dict
