def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    count = exp - 1 
    results = base
    while count > 0:
        results *= base
        count -= 1
    return results

print(iterPower(2, 3))