# How do we use a class?

class fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    def get_numerator(self):
        return self.numerator
    def get_denominator(self):
        return self.denominator
    def return_decimal(self):
        return self.numerator / self.denominator
    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return fraction(numerator, denominator)
    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return fraction(numerator, denominator)
    

my_half = fraction(1, 2)
print(my_half)
print(my_half.return_decimal())

print(my_half.get_numerator())
print(my_half.get_denominator())

my_third = fraction(1, 3)

print(my_half + my_third)

class intSet(object):
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'

s = intSet()
s.insert(3)
s.insert(4)
s.insert(3)
print(s.member(3))
print(s.member(5))
print(s)
s.remove(5)
