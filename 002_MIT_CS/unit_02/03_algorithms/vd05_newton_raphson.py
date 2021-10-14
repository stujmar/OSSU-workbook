# Newton Raphson method for finding roots of a function?

# A general approximation algorithm for finding roots of a polynomial in one variable?
# Newton Raphson method

# p(x) = a0 + a1*x + a2*x^2 + ... + an*x^n

# if g is a good guess, then
# g(x) = p(x) - g

# Look up a dirivitive of a polynomial

epsilon = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))