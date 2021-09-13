# Building our own functions

# Extending Python with additional functionality
def function_name():
    print("cool new things for functions to do")

# Function was defined but never invoked or "called".
# Store and reuse code.
# Functions are a way to organize your code.

print(max('Hello World'))
print(max(1, 2, 3, 4, 5))

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet("es")
greet("fr")
greet("en")

# Parameters and Arguments
# Parameters are the names of the arguments that a function takes.
# Arguments are the values that are passed to the function.

# Fruitful functions return a value.
# Can assign the return value to a variable.
def return_greeting():
    return "Well hello"

my_greeting = return_greeting()

print(return_greeting(), "Stu.")
print(my_greeting, "Ally.")

def add_two(a,b):
    return a + b

print(add_two(1, 2))

# The last line of the function implicitly returns the value of the last expression?