# Example of Exception Usage

def main():
    try:
        print("Enter a number: ")
        num = int(input())
        print("You entered: ", num)
    except ValueError:
        print("That's not a number!")
    except:
        print("Something went wrong!")
    else:
        print("No exceptions were raised!")
    # This lets us always do something like cleanup even if there is an exception.
    finally:
        print("This is always printed!")

def clean_input():
    while True:
        try:
            n = int(input("Enter an integer: "))
            n = int(n)
            break
        except ValueError:
            print("Oops! That was no valid number. Try again...")
    print("Correct input of an integer")

def gradeData(data):
    for student in data:
        try:
            grade = int(student[-1])
        except ValueError:
            print("Error: Invalid grade")
            continue
        if grade < 0 or grade > 100:
            print("Error: Invalid grade")
            continue
        if grade < 60:
            print("Warning: Grade is less than 60")
        elif grade < 70:
            print("Warning: Grade is less than 70")
        elif grade < 80:
            print("Warning: Grade is less than 80")
        elif grade < 90:
            print("Warning: Grade is less than 90")
        else:
            print("Grade is good")

our_data = [
    ['Eric', 'Grimson', '80'],
    ['John', 'Doe', '100'],
    ['Jane', 'Doe', '90'],
    ['John', 'Smith', '70'],
    ['Jane', 'Smith', '75'],
    ['Bill', 'Gates'],
    ['Deadpool', '100'],
    ['Dudepool', 'Von', 'Drinksaver', '100']
]

gradeData(our_data)