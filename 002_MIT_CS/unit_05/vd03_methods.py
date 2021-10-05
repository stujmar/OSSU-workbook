# In a class we ways to manipulate data
# We can use methods to manipulate data

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distnace(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<{0}, {1}>".format(self.x, self.y)

# Now we have a method on coordinate class that can calculate distance

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(c.x)
print(origin.y)

print(c.distnace(origin))
print(c)

# Checking if an object is an instance of a class
print(isinstance(c, Coordinate))