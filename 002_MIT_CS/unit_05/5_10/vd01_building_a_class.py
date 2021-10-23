import datetime

# Classes in OOP
# Classes are the blueprints for objects.
# Incredibly powerful and flexible.
# Our own data objects.

# We are going to build a little system to build people.

# They have a name and a birthday!

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


me = Person('Stuart Marsh')
print(me)
me.setBirthday(10, 3, 1984)
print(me.getAge())
print(me.getLastName())