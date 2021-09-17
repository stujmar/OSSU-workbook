# Write a program to read throught a file and pirnt the contents of the file line by line all in upper case.
# Wrap the file read in a try block and print the contents of the file
# except IOError as e:

import os

print(os.listdir("."))


my_file = open('my_file.txt')
print(my_file.read())