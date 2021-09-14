# Loop idioms

print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')

# Finding the largest number
largest = 0
for thing in [9, 41, 12, 3, 74, 15]:
    if thing > largest:
        largest = thing
print('Largest:', largest)



