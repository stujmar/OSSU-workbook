# An exception is like a planned error that occurs during the execution of a program.
# An exception can be a signal that something unexpected happened.

# What do we need to do to handle an exception?

try:
    a = 12
except:
    print("An exception occurred")

print(a)

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a/b)
    print("OK")
except ZeroDivisionError:
    print("Division by zero!")
except ValueError:
    print("Invalid input!")
except:
    print("An exception occurred")
print('outside')