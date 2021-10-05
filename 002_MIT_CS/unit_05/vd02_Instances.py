# Define a Class
# Create an instance of a class

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

# What attributes does an instance of a class have?
# Data attributes
# Methods, or procedurual attributes

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(c.x)
print(origin.y)