# Don't forget about variables.

hi = "Hello there"
print(hi)

name = "John"
print(name)

# Concatenation
greet = "Hello, " + name
print(greet)

# overloading addition
# the type of an arguement tells the operator information on what to do.

echo = ("echo "*3).strip()
print(echo)
print(len(echo))
print(echo[0:4])

# Making a copy of a string
fecho = echo[:]

print('hello'[-1])

str1 = 'hello'
str2 = ','
str3 = 'world'
str4 = str1 + str3

print('a' in str3)
print(str4[1:9:2])
print(str4[::-1])