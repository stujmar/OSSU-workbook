# Functions a block of resuable code

# it has a name, a docstring (help) and a body
# parameters that are passed a as a kind of list arguments\


def is_even(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('Running the is_even function on', i)
    return i % 2 == 0

print(is_even(3))

