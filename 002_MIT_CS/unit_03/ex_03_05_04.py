# Exercise 3.5.4

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList

# Problem 1:
print(aList == bList) # >>> True

# Problem 2:
print(aList is bList) # >>> True

# Problem 3:
print(aList) # >>> [0, 1, 'hello', 3, 4, 5]

# Problem 4:
print(bList) # >>> [0, 1, "hello", 3, 4, 5]

# Problem 5:
cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
print(cList == dList) # >>> True not the same object but True the same values.

# Problem 6:
print(cList is dList) # >>> False They are the same values but are different objects stored in different memory locations.

# Problem 7:
cList[2] = 20
print(cList) # >>> [6, 5, 20, 3, 2]

# Problem 8:
print(dList) # >>> [6, 5, 4, 3, 2] dList is not changed.