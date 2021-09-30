# import circle
from circle import *

# pi = 3

print(pi)

# print(circle.pi)
print(pi)


# print(circle.area(3))
print(area(3))

# print(circle.circumference(3))
print(circumference(3))

nameHandle = open('kids', 'w')
for i in range(2):
    name = input("Enter name: ")
    nameHandle.write(name + '\n')
nameHandle.close()

# nameHandle = open('kids', 'r')
# for line in nameHandle:
#     print(line, end='')