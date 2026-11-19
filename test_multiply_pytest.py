"""
Pytest-compatible test file for the multiply function.
This can be run with: pytest test_multiply_pytest.py -v
"""

import pytest
from multiply import multiply


class TestMultiply:
    """Test class for multiply function"""
    
    def test_positive_integers(self):
        """Test multiplication of positive integers"""
        assert multiply(5, 3) == 15
        assert multiply(10, 10) == 100
        assert multiply(1, 100) == 100
    
    def test_negative_integers(self):
        """Test multiplication with negative integers"""
        assert multiply(-4, 6) == -24
        assert multiply(4, -6) == -24
        assert multiply(-7, -8) == 56
    
    def test_multiplication_by_zero(self):
        """Test multiplication by zero"""
        assert multiply(100, 0) == 0
        assert multiply(0, 100) == 0
        assert multiply(0, 0) == 0
    
    def test_large_integers(self):
        """Test multiplication of large integers"""
        assert multiply(1000000, 1000000) == 1000000000000
        assert multiply(999999, 999999) == 999998000001
    
    def test_float_input_raises_error(self):
        """Test that float input raises TypeError"""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            multiply(5.5, 3)
        
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            multiply(5, 3.14)
    
    def test_string_input_raises_error(self):
        """Test that string input raises TypeError"""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            multiply("5", 3)
        
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            multiply(5, "3")
    
    def test_none_input_raises_error(self):
        """Test that None input raises TypeError"""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            multiply(None, 5)
        
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            multiply(5, None)
    
    def test_boolean_input_raises_error(self):
        """Test that boolean input raises TypeError"""
        with pytest.raises(TypeError, match="Both arguments must be integers, not booleans"):
            multiply(True, 5)
        
        with pytest.raises(TypeError, match="Both arguments must be integers, not booleans"):
            multiply(5, False)
    
    def test_list_input_raises_error(self):
        """Test that list input raises TypeError"""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            multiply([5], 3)
    
    def test_dict_input_raises_error(self):
        """Test that dict input raises TypeError"""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            multiply({5: 5}, 3)


# Parametrized tests for better coverage
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (5, 7, 35),
    (-2, 3, -6),
    (-2, -3, 6),
    (0, 100, 0),
    (100, 1, 100),
])
def test_multiply_parametrized(a, b, expected):
    """Parametrized test cases for multiply function"""
    assert multiply(a, b) == expected


@pytest.mark.parametrize("invalid_input", [
    5.5,
    "5",
    None,
    True,
    False,
    [5],
    {5: 5},
    (5,),
])
def test_invalid_input_types(invalid_input):
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        multiply(invalid_input, 5)
    
    with pytest.raises(TypeError):
        multiply(5, invalid_input)
