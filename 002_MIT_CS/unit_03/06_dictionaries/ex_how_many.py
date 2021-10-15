# ExerciseL: 3.6 (how many)

# Consider this
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

for animal in animals.keys():
    print(animals[animal])

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    for key in aDict.keys():
        count += len(aDict[key])
    return count

print(how_many(animals))