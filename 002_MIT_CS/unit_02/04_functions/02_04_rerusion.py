# What is recursion?
# Divide and conquer
# Recursion is when a function calls itself.
# Decrease and conquer

# Simple way to iteratively multiply two numbers
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(mult_iter(3, 5))

# a * b == a + a *  (b - 1)
def mult_recur(a, b):
    if b == 1:
        return a
    else:
        return a + mult_recur(a, b - 1)

print(mult_recur(4, 4))