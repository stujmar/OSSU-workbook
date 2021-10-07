# How do we use a class?

class fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    def return_decimal(self):
        return self.numerator / self.denominator

my_half = fraction(1, 2)
print(my_half)
print(my_half.return_decimal())