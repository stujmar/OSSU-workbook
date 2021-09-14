# Counting in a loop

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(str(zork) + ":", thing)
print("After", zork)

# sum would be a better varialbe name than zork
# add up all the numbers in a list
zippy = 0
print("Before:", zippy)
for thing in [9, 41, 12, 3, 74, 15]:
    zippy = zippy + thing
    print(str(zippy) + ":", thing)
print("Total:", zippy)

# Finding the average in a loop
count = 0
sum = 0
print("Before:", count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(str(count) + ":", sum)
print("Average:", sum / count)

# Filtering in a loop
print("Before:")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print(value, "is a big number")
print("After:")

# Searching for a value with a loop
found = False
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
print("Found:", found)

# finding the smallest value in a loop
smallest = None
for number in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
print("Smallest:", smallest)

# is and is not operators are very useful in Python
# is and is not are the same as == and !=
# is and is not are used to compare objects
# is and is not are used to compare the identity of objects
# == and != are used to compare the values of objects


