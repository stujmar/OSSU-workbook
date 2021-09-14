# Slicing strings

s = 'Monty Python'
m = s[0:5]
p = s[6:]
print(m, p)

# no out of bounds traceback
print(s[0:20])

# yes out of bounds traceback
# print(s[20])

# Overloading the plus operator?

h = 'hello'
w = 'world'
s = ' '
print(h + s + w)

# in used as a logical operator
fruit = 'banana'
print("is n in fruit:", 'n' in fruit)
print("is nan in fruit:", 'nan' in fruit)
print("is m in fruit:", 'm' in fruit)

# is it hard to predict comparing values of strings so just don't do it

# String library
greet = "Hello Bob"
zap = greet.lower()
print(zap, greet)
print('screaming'.upper())
type(greet)

# What all can we do on string?
print(dir(greet))

book = 'abcda'
print(book.find('b'))
print(book.find('a'))
print(book.replace('a', "BORG"))

messy = " data  "
messy = messy.strip()
print(messy)

# Check is a string starts with a give string
print("Nice to meet you.".startswith("Nice"))
print("Nice to meet you.".startswith("N"))
print("Nice to meet you.".startswith("Bad"))

email = "stujmar@school.com"
postion = email.find('@')
school = email[postion + 1:].replace('.com', '')
print(school)

# All internal strings are unicode
