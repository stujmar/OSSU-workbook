def question_one():
    num = 0
    while num <= 5:
        print(num)
        num += 1
    print("Outside of loop")
    print(num)

# 0, 1, 2, 3, 4, 5, Outside of loop, 6
# question_one()

def question_two():
    numberOfLoops = 0
    numberOfApples = 2
    while numberOfLoops < 10:
        numberOfApples *= 2
        numberOfApples += numberOfLoops
        numberOfLoops -= 1
    print("Number of apples: " + str(numberOfApples))

# Don't run this function
# question_two()

def question_three():
    num = 10
    while num > 3:
        num -= 1
        print(num)

# question_three()

def question_four():
    num = 10
    while True:
        if num < 7:
            print('Breaking out of loop')
            break
        print(num)
        num -= 1
    print('Outside of loop')

# 10, 9, 8, 7, Breaking out of loop, Outside of loop
# question_four()

def question_five():
    num = 100
    while not False:
        if num < 0:
            break
    print('num is: ' + str(num))

# Don't run this function
# question_five()