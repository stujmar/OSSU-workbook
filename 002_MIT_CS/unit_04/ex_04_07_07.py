# Exercise 4.7.7

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
       # changed the following line from return 0 to return 1
      return 1
   else:
      return n * f(n-1)

print(f(3))
print(f(1))
print(f(0))

