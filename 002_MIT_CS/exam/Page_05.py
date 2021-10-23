# Problem 5

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    vals = {}
    # create dict to sum all value counts
    for i in aDict.values():
        vals.setdefault(i,0)
        vals[i] += 1   
    # use each v/val from aDict as the key to vals
    # keeping each k/key from aDict if the count is 1
    return sorted(k for k, v in aDict.items() if vals[v] == 1)

print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))
print(uniqueValues({1: 1, 2: 1, 3: 1}))