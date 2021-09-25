
# bisection search to find a number between 0 and 99
def guess_number(n):
    print("Please think of a number between 0 and 100!")
    low = 0
    high = 99
    ans = (low + high) // 2
    while low <= high:
        mid = (low + high) // 2
        if mid == n:
            return mid
        elif mid < n:
            low = mid + 1
        else:
            high = mid - 1
    return None

# low = 0
# high = 100
# print('Please think of a number between 0 and 100!')
# while True:
#     guess = (high + low)//2
#     print('Is your secret number ' + str(guess) + ' ?')
#     a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
#     if a == 'c':
#         print('Game over. Your secret number was:', str(guess))
#         break
#     elif a == 'l':
#         low = guess
#     elif a == 'h':
#         high = guess
#     else:
#         print('Sorry, I did not understand your input.')