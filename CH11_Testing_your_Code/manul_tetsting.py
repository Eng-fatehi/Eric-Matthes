# Example script for manual testing

def add_numbers(a, b):
    """Function to add two numbers."""
    return a + b

# Manual test case 1
result = add_numbers(2, 3)
assert result == 5, f"Test Case 1 failed: Expected 5, but got {result}"

# Manual test case 2
result = add_numbers(-1, 1)
assert result == 0, f"Test Case 2 failed: Expected 0, but got {result}"

# ... Additional manual test cases ...

print("All manual test cases passed.")