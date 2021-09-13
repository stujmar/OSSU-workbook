# Multi-way Branch

x = 5

if x < 2:
    print('small')
elif x < 10:
    print('medium')
else:
    print('large')
print('All done')

# As many elif (else if) as you want.

if x < 2:
    print('small')
elif x < 10:
    print('medium')
elif x < 20:
    print('big')
elif x < 40:
    print('large')
elif x < 100:
    print('huge')
else:
    print('enormous')
print('All done')

# unreachable code

if x < 2:
    print('below 2')
elif x >= 2:
    print('2 or greater')
else:
    print('unreachable')

# or

if x < 2:
    print('below 2')
elif x < 20:
    print('below 20')
elif x < 10:
    print('unreachable')
else:
    print('Something else')

# try except 
# wrap dangerous code in try except

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')