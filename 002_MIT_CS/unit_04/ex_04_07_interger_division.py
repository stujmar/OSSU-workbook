def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    # added the following line to avoid the error:
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

print(integerDivision(6, 3))