# Dictionary: it is a data structure that stores key-value pairs.

names = ["Ana", "Bia", "Cia", "Dia"]
ages = [12, 13, 14, 15]
grades = [9.5, 8.5, 7.5, 6.5]
course = ["CS101", "CS102", "CS103", "CS104"]

# Data is stored across lists and hard to cross reference.
# Dictionary is a data structure that stores key-value pairs.

def get_grade(name, name_list, grade_list):
    """
    Returns the grade of a student.
    """
    # Create a dictionary with the names as keys and grades as values.
    grade_dict = dict(zip(name_list, grade_list))
    # Get the grade of the student.
    return grade_dict[name]

# a way to index into a specific itrem would be using the key.
# instead of cross referencing the lists, we can use the dictionary.

# An empty dictionary is created.
student_grades = {}

# The dictionary is filled with the names and grades.
grades = {"Ana": 9.5, "Bia": 8.5, "Cia": 7.5, "Dia": 6.5}

print(grades['Ana'])

def try_key(name):
    our_grades = {"Ana": 9.5, "Bia": 8.5, "Cia": 7.5, "Dia": 6.5}
    try:
        print(our_grades[name])
    except KeyError:
        print("KeyError, there is no name:", name)

try_key('b0rk')

grades['b0rk'] = 100
print(grades['b0rk'])

# you can grab all the keys of all the values in a dictionary.
print(grades.keys())
print(grades.values())

# Keys must be unique.
# Values can be duplicated.

# What is hashable?
# A hashable object is an object that can be used as a key in a dictionary.