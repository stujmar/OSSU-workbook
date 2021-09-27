
# Swapping values with a tuple.
def one_one():
    x = "pi"
    y = "pie"

    print(x,y)
    x,y = y,x
    print(x,y)

# one_one()

# never run this
def one_two(x):
    while x > 3:
        one_two(x + 1)

i = 1
j = 2
# probably shouldnt run this either
def one_five():
    while i >= 0:
        print(i, j)

def one_nine(x):
    a = []
    while x > 0:
        a.append(x)
        one_nine(x-1)


