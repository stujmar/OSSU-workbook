class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

# Question One
# w1 = Weird(X, Y)
# print(w1.getX())
# error

# Question Two
# print(w1.getY())
# error

# Question Three
w2 = Wild(X, Y)
print(w2.getX())
# should be 7, it was.

# Question Four
print(w2.getY())
# should be 8, it was.

# Question Five
w3 = Wild(17, 18)
print(w3.getX()) # >>> 17

# Question Six
print(w3.getY()) # >>> 18

# Question Seven
w4 = Wild(X, 18)
print(w4.getX()) # >>> 7

# Question Eight
print(w4.getY()) # >>> 18

# Question Nine
X = w4.getX() + w3.getX() + w2.getX()
print(X)
# >>> 31

# Question Ten
print(w4.getX()) # >>> 7

# Question Eleven
Y = w4.getY() + w3.getY() # >>> 36
Y = Y + w2.getY() # >>> 36 + 8 = 44
print(Y)
# 44? yes.

# Question Twelve
print(w2.getY()) # >>> 8