# Fibonacci and Dictionaries

def fib(n):
    """
    Fibonacci numbers
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))

def fib_efficeint(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficeint(n-1, d) + fib_efficeint(n-2, d)
        d[n] = ans
        return ans
d = {1:1, 2:2}
print(fib_efficeint(6, d))

# Memoization!
n = 36
print(fib_efficeint(n, d))
print(fib(n))

# Wow big difference!