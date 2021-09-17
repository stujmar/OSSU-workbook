import os

print(os.listdir("."))

# I have no idea why the root is in a different directory
xfile = open('test.txt')
for cheese in xfile:
    print(cheese)


yfile = open('single_line.txt')
print(yfile.readline())

our_letter = open('letter.txt')
for line in our_letter:
    if line.startswith('From:'):
        start = line.find(':') + 1
        print("the sender might be named:", line[start:])