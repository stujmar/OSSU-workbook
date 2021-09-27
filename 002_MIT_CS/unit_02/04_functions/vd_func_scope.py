# Video Callback Functions and Scope

def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x
x = 3
z = f(x)

# A frame or scope is a place where a variable can be stored.
# A frame is a place where a function can store a variable.
# A scope is a place where a function can store a variable.
# OK, so the scope is the frame.

# When there is no return statement then None is returned.
# You can have a function preform an action or side effect.

def func_a():
    print('in func_a')
def func_b(y):
    print('in func_b')
    return y
def func_c(z):
    print('in func_c')
    return z()
print("one")
print(func_a())
print("two")
print(5 + func_b(5))
print("three")
print(func_c(func_a))