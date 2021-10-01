# Working through the example from the video
# Debugging example

# The Code:

def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse()
    if temp == x:
        return True
    else:
        return False

def silly(n):
    for i in range(n):
        result = []
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes, it is a palindrome')
    else:
        print('No, it is not a palindrome')

# This code likely has bugs.