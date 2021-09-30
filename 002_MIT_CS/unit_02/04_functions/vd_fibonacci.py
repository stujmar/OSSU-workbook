# Fibonacci, Leonardo of Pisa

# Start with a pair of rabits.

# AI wrote the following line.
# Each rabbit has a pair of holes; one for a head, one for a tail.

# Each rabbit produces a pair of offspring before dying.

# month 1: One set of rabbits
# month 2: Two rabbits, one pair of holes each 1 female

# Recursive case
# n = 3
# Females(n) = Females(n-1) + Females(n-2)

def fibonacci(x):
    """
    assumes x an int >= 0
    returns Fibonacci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(3))
print(fibonacci(1))
print(fibonacci(0))
print(fibonacci(5))

