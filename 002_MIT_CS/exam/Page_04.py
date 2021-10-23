# Problem 4

def largest_odd_times(L):
    """ Assumes L is a non-empty list of times in seconds
        Returns the largest odd time in list L.
        Raises exception if L is empty or all even """
    largest = 0
    my_dict = {}
    if L == []:
        raise ValueError
    elif L == [0]:
        raise ValueError
    elif L == [1]:
        return 1
    else:
        for i in L:
            my_dict[i] = my_dict.get(i, 0) + 1
    for i in my_dict:
        if my_dict[i] % 2 == 1 and i > largest:
                largest = i
    if largest == 0:
        return None
    else:
        return largest

print(largest_odd_times([2, 2, 4, 4])) # > None
print(largest_odd_times([2, 2])) # > None
print(largest_odd_times([3, 3, 2, 0])) # > 2
print(largest_odd_times([3, 9, 5, 3, 5, 3])) # > 9
print(largest_odd_times([6, 8, 6, 8, 6, 8, 6, 8, 6, 8])) # > 8