# test_example.py
import pytest
from Sample import generate_random_number, add_numbers

def test_generate_random_number():
    """Test the random number generator function."""
    min_val = 1
    max_val = 10
    random_number = generate_random_number(min_val, max_val)
    assert min_val <= random_number <= max_val, f"Random number {random_number} is out of range"

def test_add_numbers():
    """Test the add_numbers function."""
    result = add_numbers(2, 3)
    assert result == 5, f"Expected 5, but got {result}"
