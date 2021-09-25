# Iterative algorithm to guess a number
# using loops

# Guess and check methods
# use a loop to generate guesses

def run_my_loop():
    x = int(input("Enter a number: "))

    def check_number(x):
        ans = 0

        while ans**3 < x:
            ans = ans + 1
        if ans**3 == x:
            # print(str(x) + " is not a perfect cube")
            print("Cube root of " + str(x) + " is " + str(ans))
        # else:

    for num in range(0, x + 1):
        check_number(num)

# run_my_loop()





