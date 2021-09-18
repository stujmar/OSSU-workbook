# Write a program to read throught a file and pirnt the contents of the file line by line all in upper case.
# Wrap the file read in a try block and print the contents of the file
# except IOError as e:

import os

# print(os.listdir("."))

collected_lines = []
my_file = open('my_file.txt')
# print(my_file.read())

mbox = open('mbox-100.txt', 'r')
# print(mbox)

# Get the lines from the file
# for line in mbox:
#     if line.startswith('X-DSPAM'):
#         line = line.rstrip()
#         collected_lines.append(line)
# print(collected_lines)

# Open the file
def open_file(file_name):
    try:
        file = open(file_name)
        return file
    except IOError as e:
        print("Error: File not found", e)
        return None

# Function to check and return lines.
def check_file(str, file, collection):
    for line in file:
        if line.startswith(str):
            line = line.rstrip()
            collection.append(line)
    return collection

# Return the length of the collection
def return_length(collection):
    return len(collection)

our_file = open_file('mbox-100.txt')
collected_lines = check_file('X-DSPAM', our_file, collected_lines)
hits = return_length(collected_lines)
print(hits)

# print(mbox.read())
