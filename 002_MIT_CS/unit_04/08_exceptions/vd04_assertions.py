# Defensive Programming: Assertions

# An assertion is a sanity check that you can use to detect bugs in your code.

# a type of exception that is raised when an assertion fails

def avg(grades):
    assert not len(grades) == 0, 'No grades data'
    return sum(grades) / len(grades)

# we assert that the lenght of the grades list is not 0
# if it is 0, we raise an AssertionError

# you can assert on inputs and outputs.
# you can also assert on the values of variables.

# Where should we use assertions?
# Assertions are used to check that the program is working correctly.
# They are used to detect bugs in the program.
# They are used to detect errors in the input data.
# Anywhere you might see a potential error.
