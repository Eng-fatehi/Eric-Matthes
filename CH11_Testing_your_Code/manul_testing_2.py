def calculate_rectangle_area(length, width):
    """Function to calculate the area of a rectangle."""
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive values.")
    return length * width


# Manual test case 1: Valid input
try:
    result = calculate_rectangle_area(5, 3)
    assert result == 15, f"Test Case 1 failed: Expected 15, but got {result}"
    print("Test Case 1 passed.")
except ValueError as ve:
    print(f"Test Case 1 failed: {ve}")

# Manual test case 2: Invalid input (negative length)
try:
    calculate_rectangle_area(-2, 4)
    print("Test Case 2 failed: Expected ValueError, but no exception raised.")
except ValueError as ve:
    print("Test Case 2 passed.")

# Manual test case 3: Invalid input (zero width)
try:
    calculate_rectangle_area(6, 0)
    print("Test Case 3 failed: Expected ValueError, but no exception raised.")
except ValueError as ve:
    print("Test Case 3 passed.")

# ... Additional manual test cases ...

print("All manual test cases completed.")