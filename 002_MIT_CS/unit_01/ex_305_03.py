# Tuples and Lists - Exercise 3

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

# probably wont work.
listA.sort

print(listA)

# better bet.
listA.sort()


print(listA)

listA.insert(0, 100)

print(listA)

listA.remove(3)

print(listA)

listA.append(7)

print(listA)

print(listA + listB)

listB.sort()
listB.pop()
print("listB: ", listB)
# listB.remove('a')

listA.extend([4, 1, 3, 4])

print(listA.count(4))

print(listA.index(1))

print("pop(4): ", listA.pop(4))

listA.reverse()

print(listA)