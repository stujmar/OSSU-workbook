# Bisection Search

def find_square_root(x):
    epsilon = 0.01
    numGuesses = 0
    low = 1.0
    high = x
    ans = (high + low)/2.0

    while abs(ans**2 - x) >= epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses = ' + str(numGuesses))
    print(str(ans) + ' is close to square root of ' + str(x))

# find_square_root(100)

def find_cubed_root(x):
    epsilon = 0.01
    numGuesses = 0
    low = 1.0
    high = x
    ans = (high + low)/2.0
    while abs(ans**3 - x) >= epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        numGuesses += 1
        if ans**3 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses = ' + str(numGuesses))
    print(str(ans) + ' is close to cube root of ' + str(x))

find_cubed_root(27)

# monotonically increasing function: look this up.
