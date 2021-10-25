# Example Gradebook
from Student import *

class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = [] # list of Student objects
        self.grades = {} # maps idNum -> list of grades
        self.is_sorted = True # true if self.students is sorted

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.idNum] = []
        self.is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.idNum].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def get_grades(self, student):
        """Return a list of grades for student"""
        try: # return copy of student's grades
            return self.grades[student.idNum][:]
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def all_students(self):
        """Return a list of students in the grade book"""
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True
        return self.students[:]

my_gradebook = Grades()

Billy = UG('Billy Borb', '2018')
print(Billy)
my_gradebook.add_student(Billy)

print(my_gradebook.all_students())

for student in my_gradebook.all_students():
    print(student.getLastName())
