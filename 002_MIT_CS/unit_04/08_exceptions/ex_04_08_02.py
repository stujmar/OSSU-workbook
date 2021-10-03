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
#actual print output: 1, 0

# index error
# fancy_divide([0, 2, 4], 4)
# actual print output: -1, 0

# denom is 0 maybe ... 1, 1, 1?
# fancy_divide([0, 2, 4], 0)
# actual print output: 0, error

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

# denom is 2. output: 0, 0, 0,
# fancy_divide_two([0, 2, 4], 1)
# 1, 0

# fancy_divide_two([0, 2, 4], 4)
# 1 0 0

# fancy_divide_two([0, 2, 4], 0)
# -2, 0

def fancy_divide_three(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

# denom is 2. output: -2, 0,
# fancy_divide_three([0, 2, 4], 1)
# 1, 0

# fancy_divide_three([0, 2, 4], 4)
# 1 0 0 

fancy_divide_three([0, 2, 4], 0)
# 0 -2
