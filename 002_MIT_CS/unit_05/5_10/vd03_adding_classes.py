# Adding another class to the program.

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

s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2018)
s3 = UG('Arnold Schwarzenegger', 2019)
s4 = Grad('Mart Dabby')

student_list = [s1, s2, s3, s4]

Billy = Transfer_Student('Bobert')

print(isStudent(s1))
print(isStudent(Billy))

print(s1.speak('I am a student'))
print(s1.getClass())
print(s4.speak('I am a student'))
# print(s4.getClass())
