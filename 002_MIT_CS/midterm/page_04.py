# Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. 
# For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

# This function takes in a list of strings and returns a list of strings. Your function should not modify aList.
aList = ["apple", "cat", "dog", "banana"]
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    return [x for x in aList if len(x) < 4]
    
print(lessThan4(aList))

def my_work(aList):
    results = []
    for item in aList:
        if len(item) < 4:
            results.append(item)
    return results


print(my_work(aList))
