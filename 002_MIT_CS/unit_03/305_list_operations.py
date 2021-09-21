# Lists come with standard operations

x = [1,2,3]

# Adds something to a list
x.append(4)

print(x)

# Almost everything in python is an object

L1 = [1,2,3]
L2 = [4,5,6]

L3 = L1 + L2
print(L3)

L1.extend(L2)
print(L1)

data = [1, "bad", 3, 4, 5]
del(data[1])
print(data)

# Removes the last element
names = ["Stu", "Ally", "Peepole"]
names.pop()
print(names)

# Removes a matching element
booleans = [True, False, "Maybe"]
booleans.remove("Maybe")
print(booleans)

# Turns string into list with each char as an element
my_string = "abc"
print(list(my_string))

print("abc".split("b"))

