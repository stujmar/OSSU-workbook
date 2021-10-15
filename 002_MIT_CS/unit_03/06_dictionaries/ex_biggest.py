# Exercise 3.6 Biggest

# Consider the following.

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    max_val = 0
    max_key = ''
    for key in aDict:
        if len(aDict[key]) > max_val: # you can add a >= here to account for empty lists 
            max_val = len(aDict[key])
            max_key = key
    return max_key