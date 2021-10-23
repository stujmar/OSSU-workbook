# Problem 2-1

class A(object):
    def foo(self):
        print('hi')
class B(A):
    def foo(self):
        print('bye')

a = A()

# a is an instance of class A True

# Problem 2-2

def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print(m)
    for i in range(n):
        g(n)

# O(n)

# Problem 2-3

# Dictionarys are mutable.

# Problem 2-4

def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
    return answer

def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1: 
        return 1.0
    else: 
        return n*foo_two(n-1)

# Problem 2-5

