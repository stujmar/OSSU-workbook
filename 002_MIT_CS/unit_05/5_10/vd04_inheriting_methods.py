# Using Inherited Methods
import datetime

# Class Person
class Person(object):
    def __init__(self, name):
        """ create a person called name """
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    def getLastName(self):
        """ return self's last name """
        return self.lastName
    def __str__(self):
        """ return self's name """
        return self.name
    def setBirthday(self, month, day, year):
        """ sets self's birthday to birthDate """
        self.birthday = datetime.date(year, month, day)
    def getAge(self):
        """ returns self's current age in days """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days//365

# Inherit from Person
class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        # initialize Person attributes
        Person.__init__(self, name)
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)
    def lecture(self, topic):
        return self.speak('It is obvious that ' + topic)

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classyear):
        MITPerson.__init__(self, name)
        self.year = classyear
    
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)
    
class Grad(Student):
    pass

class Transfer_Student(Student):
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad) or isinstance(obj, Student)

billy = UG('Billy', 2017)
faculty = Professor('Doctor Arrogant', 'course six')
print(faculty.	getIdNum())
print(faculty.getLastName())
print(faculty.speak('Greetings'))
print(faculty.lecture('it is elementary'))
print(billy.speak('what does it mean?'))