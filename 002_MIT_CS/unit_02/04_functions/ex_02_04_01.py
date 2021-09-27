def a(x):
   '''
   x: int or float.
   '''
   return x + 1

# could return int or float
# print(type(a(1)))
# print(type(a(1.0)))

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0

# Always returns a float
# print(type(b(1)))
# print(type(b(1.0)))

def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

# Could return int or float
# print(type(c(1, 2)))
# print(type(c(1.0, 2.0)))
# print(type(c(1, 2.0)))

def d(x, y):
   '''
   x: Can be int or float.
   y: Can be int or float.
   '''
   return x > y

# Always returns a boole
# print(type(d(1, 2)))
# print(type(d(1.0, 2.0)))
# print(type(d(1, 2.0)))

def e(x, y, z):
   '''
   x: Can be int or float.
   y: Can be int or float.
   z: Can be int or float.
   '''
   return x >= y and x <= z

# Always returns a boolean
# print(type(e(1, 2, 3)))
# print(type(e(1.0, 2.0, 3.0)))
# print(type(e(1, 2.0, 3.0)))

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2

# No return statement
# print(type(f(1, 2)))
# print(type(f(1.0, 2.0)))
# print(type(f(1, 2.0)))