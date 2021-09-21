# Odd Tuples

def oddTuples(aTup):
    results = []
    for i in range(len(aTup)):
        if i % 2 == 0:
            results.append(aTup[i])
    return tuple(results)

