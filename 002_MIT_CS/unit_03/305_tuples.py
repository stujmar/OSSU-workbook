# Kinds of data structures,
# A tuple is an ordered sequence of elements.
# ordered/indexed

my_empty_tuple = ()
my_tuple = ("one", 2)
print(my_tuple[0])

tuple_two = ("three")

# You can't concatonate tuples
# tuple_three = my_tuple + tuple_two
# print(tuple_three)

# Swapping variables the old way
x = 1
y = 2

temp = y
y = x
x = temp

# This is the new tuple way
(x, y) = (y, x)

aTuple = ((),(),(),())
def getData(our_tuple):
    nums = ()
    words = ()
    for t in our_tuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)
# This doesn't work but in theory we can interate over a tuple.
# print(getData((1, "1", 2, "23", 34, 291, "pill")))