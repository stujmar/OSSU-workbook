import os

print(os.listdir("."))

# I have no idea why the root is in a different directory
xfile = open('../008_files/test.txt')
for cheese in xfile:
    print(cheese)


yfile = open('../008_files/single_line.txt')
print(yfile.readline())

our_letter = open('../008_files/letter.txt')
for line in our_letter:
    if line.startswith('From:'):
        start = line.find(':') + 1
        print("the sender might be named:", line[start:])