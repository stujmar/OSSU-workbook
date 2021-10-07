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