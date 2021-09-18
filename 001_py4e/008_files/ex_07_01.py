# Write a program to read throught a file and pirnt the contents of the file line by line all in upper case.
# Wrap the file read in a try block and print the contents of the file
# except IOError as e:

import os

print(os.listdir("."))

collected_lines = []
my_file = open('my_file.txt')
print(my_file.read())

mbox = open('mbox-100.txt', 'r')
print(mbox)

# Get the lines from the file
for line in mbox:
    if line.startswith('X-DSPAM'):
        line = line.rstrip()
        collected_lines.append(line)
print(collected_lines)

# Function to check and return lines.
def check_file(str, file, collection):
    for line in file:
        if line.startswith(str):
            line = line.rstrip()
            collection.append(line)
    return collection

check_file('X-DSPAM', mbox, collected_lines)

# print(mbox.read())
