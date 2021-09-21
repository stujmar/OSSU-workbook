# Branching program, multiple possible paths.

def check_ex(x):
    if x >= 100:
        print('x is huge!')
    elif x < 100 and x != 5:
        print('x is neither huge nor 5')
    else:
        print('else is probably 5')

check_ex(105)
check_ex(15)
check_ex(5)

# while loops can do things an undeterminded amout of times.

number = input("input a number:")
while number != "done":
    print("don't type", number, "type done")
    number = input("type done:")

x = 0
while x <= 100:
    print(x)
    x = x + 1