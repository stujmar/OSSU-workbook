# Exercise Unit 01, Section Two, Exercise 02
# We are practicing the for loop

def exercise_one():
    for num in range(2, 11, 2):
        print(num)
    print("Goodbye!")

# exercise_one()

def exercise_two():
    print("Hello!")
    for num in range(10, 0, -2):
        print(num)

# exercise_two()

def exercise_three(end):
    results = 0
    for num in range(1, end + 1):
        results += num
    print(results)

exercise_three(6)
