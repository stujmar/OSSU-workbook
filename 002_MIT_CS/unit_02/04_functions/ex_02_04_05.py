# Exercises 2.4.5

def foo(x, y = 5):
    """
    Problem One.
    """
    def bar(x):
        return x + 1
    return bar(y * 2)

# Estimated output: 11  
print(foo(3))
# Actual output: 11

def foo(x, y = 5):
    """
    Problem Two.
    """  
    def bar(x):
        return x + 1
    return bar(y * 2)

# Estimated output: 1          
print(foo(3, 0))
# Actual output: 1

def foo (x):
    """
    Problem Three.
    """
    def bar (z, x = 0):
        return z + x
    return bar(3, x)

# Estimated output: 5
print(foo(2))
# Actual output: 5

def foo (x):
    """
    Problem Four.
    """
    def bar (z, x = 0):
      return z + x
    return bar(3)

# Estimated output: 3
print(foo(5))
# Actual output: 3