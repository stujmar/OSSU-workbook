# Problem 2.4.4.1

a = 10
def f(x):
    return x + a
a = 3

# estimated output: int 4 
print(f(1))
# actual output: int 4 

# Problem 2.4.4.2

x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)

# estimated output: int 19
print(g(x))
# actual output: int 19