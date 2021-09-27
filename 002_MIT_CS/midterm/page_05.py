# aDict = {'name': 5, 'city': 2, 'cake': 3, 'beer': 3}
aDict = {2: 2, 5: 0, 7: 3}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a list of unique dictionary values
    '''
    unique_keys = {}
    for key in aDict:
        unique = True
        for check in aDict:
            if aDict[key] == aDict[check] and key != check:
                unique = False
        if unique:
            unique_keys[aDict[key]] = key
    results = []
    for key in unique_keys:
        results.append(unique_keys[key])
    return sorted(results)

print(uniqueValues(aDict))
