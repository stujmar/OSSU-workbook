import datetime

# Classes can inherit from other classes.

# Create an MIT Person they have the attributes of a normal person plus an id number.

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

MIT = MITPerson('Eric')
print(MIT.speak('I like 6.00.1x!'))
print(MIT.getIdNum())
M3 = MITPerson('John')
print(M3.getIdNum())
M5 = MITPerson('Jon Bum')
print(M5.getIdNum())
MIT_2 = MITPerson('John')
MIT_2.getIdNum()
print(MIT_2.getIdNum())
print(MIT < MIT_2) # True because MIT's ID number is less than MIT_2's ID number.

my_list = [MIT, MIT_2, M3, M5]
for person in my_list:
    print(person, person.getIdNum())

my_list.sort()
for person in my_list:
    print(person, person.getIdNum())
