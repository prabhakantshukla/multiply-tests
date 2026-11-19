def multiply(a, b):
    """
    Multiply two numbers together.
    
    Args:
        a: First number (should be an integer)
        b: Second number (should be an integer)
    
    Returns:
        The product of a and b
    
    Raises:
        TypeError: If either argument is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    
    # Note: In Python, bool is a subclass of int, so we need to explicitly check
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Both arguments must be integers, not booleans")
    
    return a * b


def test_multiply():
    """Test cases for the multiply function"""
    
    print("Running tests for multiply function...\n")
    
    # Test 1: Positive integers
    try:
        result = multiply(5, 3)
        assert result == 15, f"Expected 15, got {result}"
        print("✓ Test 1 passed: multiply(5, 3) = 15")
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
    
    # Test 2: Negative integers
    try:
        result = multiply(-4, 6)
        assert result == -24, f"Expected -24, got {result}"
        print("✓ Test 2 passed: multiply(-4, 6) = -24")
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
    
    # Test 3: Two negative integers
    try:
        result = multiply(-7, -8)
        assert result == 56, f"Expected 56, got {result}"
        print("✓ Test 3 passed: multiply(-7, -8) = 56")
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
    
    # Test 4: Multiplication by zero
    try:
        result = multiply(100, 0)
        assert result == 0, f"Expected 0, got {result}"
        print("✓ Test 4 passed: multiply(100, 0) = 0")
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
    
    # Test 5: Float input (should raise TypeError)
    try:
        multiply(5.5, 3)
        print("✗ Test 5 failed: Should have raised TypeError for float input")
    except TypeError as e:
        print(f"✓ Test 5 passed: Correctly rejected float input - {e}")
    
    # Test 6: String input (should raise TypeError)
    try:
        multiply("5", 3)
        print("✗ Test 6 failed: Should have raised TypeError for string input")
    except TypeError as e:
        print(f"✓ Test 6 passed: Correctly rejected string input - {e}")
    
    # Test 7: None input (should raise TypeError)
    try:
        multiply(None, 5)
        print("✗ Test 7 failed: Should have raised TypeError for None input")
    except TypeError as e:
        print(f"✓ Test 7 passed: Correctly rejected None input - {e}")
    
    # Test 8: Boolean input (should raise TypeError)
    try:
        multiply(True, 5)
        print("✗ Test 8 failed: Should have raised TypeError for boolean input")
    except TypeError as e:
        print(f"✓ Test 8 passed: Correctly rejected boolean input - {e}")
    
    # Test 9: Large integers
    try:
        result = multiply(1000000, 1000000)
        assert result == 1000000000000, f"Expected 1000000000000, got {result}"
        print("✓ Test 9 passed: multiply(1000000, 1000000) = 1000000000000")
    except AssertionError as e:
        print(f"✗ Test 9 failed: {e}")
    
    print("\nAll tests completed!")


if __name__ == "__main__":
    # Run the test suite
    test_multiply()
    
    # Interactive example
    print("\n" + "="*50)
    print("Interactive Example:")
    print("="*50)
    
    try:
        result = multiply(12, 7)
        print(f"multiply(12, 7) = {result}")
    except TypeError as e:
        print(f"Error: {e}")
