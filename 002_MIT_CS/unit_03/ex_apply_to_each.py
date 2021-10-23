# Exercise Apply to Each 01

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

applyToEach(testList, abs)
print(testList)

# Exercise Apply to Each 02

def add_one(x):
    return x + 1
applyToEach(testList, add_one)

# Exercise Apply to Each 03

def square(x):
    return abs(x) * abs(x)
applyToEach(testList, square)