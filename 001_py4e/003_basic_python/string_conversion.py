# String conversion.

sval = '123'
print(type(sval))

# Results in an error. Can't convert a string to an integer.
# print(sval + 4)

ival = int(sval)
print(type(ival))
print(ival + 4)

# Error can't turn characters into an int
# int('Hello World')

# ask user for input through the command prompt
# only use input for learning purposes, maybe for debugging.
name = input('Please enter your name: ')

print('Hello', name)