# Loops and iteration

# This is a loop.
n = 5 
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")
print(n)

# Don't make infinite loops!

# zero trip loops
# not garunteed to run ever
n = 0
while n < 0:
    print(n)
    n = n + 1   
# never runs

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
# Would be infinite loop but we break it.

# continue keyword
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# For most loops use definite loops