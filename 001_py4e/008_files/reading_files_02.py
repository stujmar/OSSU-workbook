import os

print(os.listdir("."))

# I have no idea why the root is in a different directory
xfile = open('../008_files/test.txt')
for cheese in xfile:
    print(cheese)