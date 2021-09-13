# Decision making.
# If statements.
# If statements are used to make decisions.

x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
    print('Still bigger')
print('Finis')

# Comparision operators.
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# Use four spaces? not tabs?
# VS code writes 4 spaces when you click tab.

print('Start')
x = 5
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')
for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i =', i)
print('All Done')

# Nested if statements.

x = 42
if x > 1:
    print('More than 1')
    if x < 100:
        print('Less than 100')
print('All Done')

# If then else.
x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All done')

