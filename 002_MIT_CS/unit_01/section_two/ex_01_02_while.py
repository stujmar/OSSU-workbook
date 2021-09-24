# Get a while loop to print 2, 4, 6, 8, 10 Goodbye!

def question_one():
    num = 2
    while num <= 10:
        print(num)
        num += 2
    print("Goodbye!")

def question_two():
    num = 10
    print("Hello!")
    while num >= 2:
        print(num)
        num -= 2

def question_three(end):
    sum = 0
    while end > 0:
        sum += end
        end -= 1
    print(sum)

question_three(6)