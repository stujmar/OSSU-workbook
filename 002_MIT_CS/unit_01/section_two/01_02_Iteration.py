# Branching vs looping.
# Branching different paths of execution.
# Looping through a sequence of code.

x = 3
ans = 0
itersLeft = x
while itersLeft > 0:
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + "*" + str(x) + "=" + str(ans))