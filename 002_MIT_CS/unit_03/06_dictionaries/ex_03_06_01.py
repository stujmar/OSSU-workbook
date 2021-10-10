animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

# Question One
print(animals)

# Question Two
print(animals['c'])

# Question Three
# print(animals['donkey']) >>> KeyError: 'donkey'

# Question Four
print(len(animals))
# 4? >>> It was 4!

# Question Five
animals['a'] = 'anteater'
print(animals['a'])
# >>> anteater

# Question Six
print(len(animals['a']))

# Question Seven
# True for keys not for values.
print('baboon' in animals) # >>> False
print('b' in animals) # >>> True

# Question Eight
print('donkey' in animals.values()) # >>> True

# Question Nine
print('b' in animals) # >>> True

# Question Ten
print(animals.keys())
print(animals.values())