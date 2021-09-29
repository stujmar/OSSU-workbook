def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    def square(x):
        return x * x
    return square(x) * square(x)

print(fourthPower(2))