def question_one():
    num = 10
    for num in range(5):
        print(num)
    print(num)

# 0, 1, 2, 3, 4, 4,
# question_one()

def question_two():
    divisor = 2
    for num in range(0, 10, 2):
        print(num/divisor)

#  0.0, 1.0, 2.0, 3.0, 4.0
# question_two()

def question_three():
    for variable in range(20):
        if variable % 4 == 0:
            print(variable)
        if variable % 16 == 0:
            print('Foo!')

# 0, Foo!, 4, 8, 16, Foo!
# question_three()

def question_four():
    for letter in 'hola':
        print(letter)

# h, o, l, a
# question_four()