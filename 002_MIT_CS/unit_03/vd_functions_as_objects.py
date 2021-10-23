# Functions as objects.

def my_function(x):
    if type(x) == int:
        return x + 1
    else:
        return x

# Functions are considered first class data structures.

# Higher order programming. Using functions as arguments.

def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

# interesting.

my_list = [1, -4, 8, -9]
apply_to_each(my_list, abs)
print(my_list)

# cool.

apply_to_each(my_list, my_function)
print(my_list)


def apply_functs(L, x):
    for f in L:
        print(f(x))

# Where L is a list of functions.
# Once again, interesting.

# HOP is a higher order programming language.
map(my_function, my_list)
print(my_list)
# the map function, which takes a function and a list as arguments.
# map applies the function to each element of the list. Map gives back a list?

# n-ary functions.
# A function that takes n arguments.
