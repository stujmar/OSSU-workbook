# Program Efficiency

# Computers are getting faster, but data sets are getting bigger and bigger.

# Choice of implementation is different than choice of algorithm.

# Running time of algorithms is the time it takes to run the algorithm.
# You can count the operations in the algorithm. 

def c_to_f(c):
    return c * 9 / 5 + 32

def mysum(x):
    total = 0
    for i in range(x):
        total += i
    return total

# count of operations varies for different implementations and inputs.

# We want to evaluate the algorithm
# Independent of the computer
# Independent of the data set
# and predictable as the size of the data set increases.

# Orders of Growth
# O(1) - Constant
# O(log n) - Logarithmic
# O(n) - Linear
# O(n log n) - Linearithmic
# O(n^2) - Quadratic
# O(2^n) - Exponential

