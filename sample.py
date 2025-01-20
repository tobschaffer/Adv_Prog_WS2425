def fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence up to n.
    Second line in description
    """
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Using the generator
# Test Hosnasoofi
for number in fibonacci_sequence(100):
    print(number)
