# Working through the example from the video
# Debugging example

# The Code:

def isPal(x):
    assert type(x) == list
    temp = x[:]
    # This line was changed from temp.reverse()
    temp.reverse()
    if temp == x:
        return True
    else:
        return False

# def silly(n):
#     for i in range(n):
#         result = []
#         elem = input('Enter element: ')
#         result.append(elem)
#     if isPal(result):
#         print('Yes, it is a palindrome')
#     else:
#         print('No, it is not a palindrome')

def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes, it is a palindrome')
    else:
        print('No, it is not a palindrome')


silly(3)

# This code likely has bugs.