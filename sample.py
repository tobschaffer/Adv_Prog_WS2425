def fibonacci_sequence(n):
    """
    New function description from Tobias
    Hi all i just come back :)
    """
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Using the generator
# New function description from Patricia
# Test Hosnasoofi
for number in fibonacci_sequence(100):
    print(number)














