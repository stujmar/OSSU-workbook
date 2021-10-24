# Global Variables

# Global variables are variables that are defined outside of any function.
# They are accessible throughout the program.

# They can be dangerous, because they can be modified by the user.
# They break the scope of functions. They can step on vars in functions.

numFibCalls = 0

def fib(n):
    """
    Fibonacci numbers
    """
    global numFibCalls
    numFibCalls += 1
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
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficeint(n-1, d) + fib_efficeint(n-2, d)
        d[n] = ans
        return ans
d = {1:1, 2:2}
print(fib_efficeint(6, d))

# Memoization!
n = 30


print(fib_efficeint(n, d))
print("calls:", numFibCalls)
print(fib(n))
print("calls:", numFibCalls)

# wow!
