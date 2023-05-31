

# def add(a, b):
#     """Compute and return the sum of two numbers.

#     Usage examples:
#     >>> add(9.0, 2.0)
#     11.0
#     >>> add(4, 2)
#     6.0
#     """
#     return float(a + b)



# """Sample failing tests.

# The output must be an integer
# >>> 5 + 7
# 12

# The output must not contain quotes
# >>> print("Hello, World!")
# Hello, World!

# The output must not use double quotes
# >>> "Hello," + " World!"
# 'Hello, World!'

# The output must not contain leading or trailing spaces
# >>> print("Hello, World!")
# Hello, World!

# The output must not be a blank line
# >>> print()

# """


# ...

def divide(a, b):
    """Compute and return the quotient of two numbers.

    Usage examples:
    >>> divide(84, 2)
    42.0
    >>> divide(15, 3)
    5.0
    >>> divide(42, -2)
    -21.0

    >>> divide(42, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    return float(a / b)