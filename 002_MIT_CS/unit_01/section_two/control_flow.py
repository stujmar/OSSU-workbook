# for loops

# count to 10
for number in range(1, 11):
    print(number)

print("\n")

# count down from 10 to 1
for number in range(10, 0, -1):
    print(number)
print("blast off.")

# build a for loop out of a while loop
# for some reason...
count = 1
while count <= 10:
    print(count)
    count += 1

# the break keyword.
# break is used to exit a for loop or a while loop before the loop completes.

for number in range(1, 11):
    if number == 5:
        print("we are breaking at five")
        break
    print(number)


