# integer plus an integer
my_int = 2 + 3
print(type(my_int), my_int)

# string plus a string
my_str = "Hello" + " " + "World"
print(type(my_str), my_str)

print(type(1), type(1.0))

number = 1
print("number was a:", type(number))
number = float(number)
print("now it is a:", type(number))

# integers combined with floats results in a float. Python 2 was a mess and didn't do this.