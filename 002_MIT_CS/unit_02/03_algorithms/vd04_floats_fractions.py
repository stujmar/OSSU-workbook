x = float(5.0)
p = 0
while ((2**p)*x) % 1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1
 