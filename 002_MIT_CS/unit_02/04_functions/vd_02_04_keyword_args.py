# Keyword Arguments

def printName(firstName, lastName, reverse = False):
    if reverse:
        print (lastName + ', ' + firstName)
    else:
        print (firstName + ' ' + lastName)

# Default argument values
printName('John', 'Doe')
printName('John', 'Doe', False)
printName('John', 'Doe', True)