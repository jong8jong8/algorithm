def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
        # Caution!!!! The following is WRONG!
        # m = n
        # n = m % n (i.e., the updated m value by n)
        #
        # The correct one is the following.
        # temp = m
        # m = n
        # n = temp % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def show(self):
        print(f"{self.num}/{self.den}")
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)







# my_fraction = Fraction(3, 5)

# my_fraction.show()

# print(my_fraction)
# print(my_fraction.__str__())

# print(f"I ate {my_fraction} of pizza")

# print(type(my_fraction), my_fraction)

# val = str(my_fraction)
# print(type(val), val)

# f1 = Fraction(1, 4)
# f2 = Fraction(1, 2)
# print(f1.__add__(f2))
# f3 = f1 + f2
# print(f3)

# print(gcd(24, 10))

# f1 = Fraction(3, 5)
# f2 = f1
# print(f1.__eq__(f2))  # shallow equality
# print(f1 == f2)  

f1 = Fraction(3, 5)
f2 = Fraction(3, 5)
print(f1.__eq__(f2))  # deep equality (NotImplemented by default)
print(f1 == f2)  
