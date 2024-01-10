# 4-print_square.py

def print_square(size):
    """
    Print a square with the character '#'.

    Args:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0.

    Returns:
    - None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

# 4-main.py

#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

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

# tests/4-print_square.txt

# No doctests in this case

# Run the tests
# guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/4-print_square.txt
