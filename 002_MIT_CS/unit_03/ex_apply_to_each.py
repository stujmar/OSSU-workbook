# Exercise Apply to Each 01

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

applyToEach(testList, abs)
print(testList)