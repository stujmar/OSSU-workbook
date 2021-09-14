# Strings

str1 = "Hello"
str2 = "World"
bob = str1 + " " + str2
print(bob)

str3 = "123"
apple = "20"
print(int(str3) + int(apple))

# String chars are indexed from 0

fruit = "banana"
letter = fruit[0]
print(letter)

for letter in fruit:
    print(letter)

zot = 'abc'
try: 
    print(zot[5])
except:
    print("Error")
print("length:", len(zot))

word = "banana"
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print("There are", count, "As in", word)