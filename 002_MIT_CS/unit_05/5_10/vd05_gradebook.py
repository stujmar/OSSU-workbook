# Example Gradebook

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

