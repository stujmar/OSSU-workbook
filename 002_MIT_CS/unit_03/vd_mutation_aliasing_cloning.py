# List are different from tuples because they are mutable

# This can introdue problems.

# Mutation Aliasing and Cloning.

# List are mutable.
# Lists behave differently than immutables types.

# A list is an object in memory.
# A variable points to this object.
# Multiple variables can point to the same object.

people = ['John', 'Mary', 'Bob', 'Alice']
other_people = people
third_people = people[:]
fourth_people = people.copy()

people.append('Stu')

print("people:", people)
print("other_people:", other_people)
print("third_people:", third_people)
print("fourth_people:", fourth_people)

a = 1
b = a
warm = ['red', 'yellow', 'orange']
hot = warm
hot.append('pink')
print(warm)

# Having the same data in an object doesn't mean that they are the same object.

cool = ['blue', 'green', 'gray']
chill = ['blue', 'green', 'gray']

print(cool == chill) # True

chill[1] = 'purple'

print(cool == chill) # False

freeze = cool[:]
# How does list[:] make a copy of the list?

def copy_list(list):
    """
    Very inefficient way to copy a list.
    """
    new_list = []
    for item in list:
        new_list.append(item)
    return new_list

unsorted_list = [99, 1, 5, 3, 20, 4]
unsorted_list.sort() # Doesn't return anything, but does mutate the list.
print(unsorted_list)

mess = [1, 4, 9, 3, 1, 88, 29, 1]
sorted(mess) # Returns a new list, but doesn't mutate the original list.
print(mess)
mess = sorted(mess) # Mutates the list. Returns mutated list.
print(mess)

# Put a list in a list.
dogs = ['Fido', 'Buddy', 'Rover', 'Snoopy']
big_dogs = ['Clifford', 'Cerberus']
all_dogs = dogs + big_dogs
dogs.append(big_dogs)

print(dogs)

big_dogs.append('Buster')

print(dogs)

for dog in all_dogs:
    print(dog) # no buster

L1 = [1, 2, 3]
L2 = [2, 4, 5]

def remove_dups(L1, L2):
    """
    Remove duplicates from L1 and L2.
    """
    for item in L1[:]:
        if item in L2:
            L2.remove(item)
            L1.remove(item)
    return L1 + L2

print(remove_dups(L1, L2))