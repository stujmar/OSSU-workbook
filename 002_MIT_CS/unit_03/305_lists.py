# Lists
# They are arrays!
# Compound data construct?

# ordered (by index)
# denoted by square brackets []
# usually homogeneous, but don't have to be.

a_list = []
b_list = [2, 'a', 4, True]
L = [ 100, 101, 102]

print(len(b_list))
print(L[1])

# they are mutable
L[2] = 222
print(L)

count = 0
numbers = [1,3,4,63, 2]
for number in numbers:
    count += number
print(count)