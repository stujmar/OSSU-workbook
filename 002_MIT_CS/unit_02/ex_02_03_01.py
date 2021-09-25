# Exercise 2.3.1

def question_one():
    iteration = 0
    count = 0
    while iteration < 5:
        # the variable 'letter' in the loop stands for every 
        # character, including spaces and commas!
        for letter in "hello, world": 
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        iteration += 1 

# question_one()

def question_two():
    iteration = 0
    while iteration < 5:
        count = 0
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        iteration += 1

# question_two()

def question_three():
    iteration = 0
    while iteration < 5:
        count = 0
        for letter in "hello, world":
            count += 1
            if iteration % 2 == 0:
                break
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        iteration += 1

question_three()

