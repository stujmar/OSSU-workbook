# Excersize 4.8.2

def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            # print("i", i)
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")

# estimated print output: Divide by zero error?
# denom is 2. 
# fancy_divide([0, 2, 4], 1)

# index error
# fancy_divide([0, 2, 4], 4)

# denom is 0 maybe ... 1, 1, 1?
# fancy_divide([0, 2, 4], 0)

def fancy_divide_two(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
