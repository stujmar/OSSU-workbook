# Exercise 4.7.3

def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger

# Choose a test suite that has a test for every path of the code and tests some extremes like 0, -1, and -2