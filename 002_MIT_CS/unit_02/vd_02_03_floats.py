# Floats and Fractions

# How are floats represented in the computer.
# Floats are represented in binary.
# Floats are represented in base 2

# a function to print a number in binary
# this was copilot I don't know if it right.
def print_binary(num):
    # convert the number to a string
    num_str = str(num)
    # convert the string to a list of characters
    num_list = list(num_str)
    # convert the list of characters to a list of integers
    num_list = [int(x) for x in num_list]
    # convert the list of integers to a list of binary digits
    num_list = [bin(x)[2:].zfill(8) for x in num_list]
    # convert the list of binary digits to a string
    num_str = ''.join(num_list)
    # print the string
    print(num_str)

print_binary(302)

def decimal_to_binary(num):
    # deal with negative numbers
    if num < 0:
        isNeg = True
        num  = abs(num)
    else:
        isNeg = False
    result = ''
    # deal with if it is 0
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    if isNeg:
        result = '-' + result
    print(result)

decimal_to_binary(-302)