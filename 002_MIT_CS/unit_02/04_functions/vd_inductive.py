# Inductive Reasoning

def multi_iter(a, b):
    """
    Multiplies two numbers together.
    Using iteration.
    """
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def multi_recur(a, b):
    """
    Multiplies two numbers together.
    Using recursion.
    """
    if b == 0:
        return 0
    return a + multi_recur(a, b - 1)

# sum of integers from 1 to n
def sum_recur(n):
    """
    Sums integers from 1 to n.
    Using recursion.
    """
    if n == 0:
        return 0
    return n + sum_recur(n - 1)

# Test reursion on the base case
# Then assume that it will work on the non base case