class Fraction:
    def __init__(self,numerator,denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def printFraction(self):
        print(str(self.numerator)+'/'+str(self.denumerator))

    def multiplication(self, frac2):
        self.numerator = self.numerator*frac2.numerator
        self.denumerator = self.denumerator * frac2.denumerator

f1 = Fraction(3,5)
f2 = Fraction(5,3)

f1.printFraction()
f2.printFraction()
print("mnozenie")
f1.multiplication(f2)
f1.printFraction()