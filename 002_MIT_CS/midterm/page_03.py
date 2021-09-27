def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    if x == b:
        return 1
    elif x < b:
        return 0
    else:
        return myLog(x/b, b) + 1


