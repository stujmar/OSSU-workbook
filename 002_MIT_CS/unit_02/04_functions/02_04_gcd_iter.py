def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    divisor = min(a, b)
    while divisor > 0:
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        divisor -= 1