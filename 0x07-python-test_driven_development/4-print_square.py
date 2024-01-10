def print_square(size):
    """
    Print a square with the character '#'.

    Args:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer or if it is a float.
    - ValueError: If size is less than 0.

    Returns:
    - None
    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

# Test cases
print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")

try:
    print_square(-1)
except Exception as e:
    print(e)
