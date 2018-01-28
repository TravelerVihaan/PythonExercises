import math

class Ulamek:
    def __init__(self, l, m):
        self.licznik = l
        self.mianownik = m

    def getLicznik(self):
        return self.licznik

    def getMianownik(self):
        return self.mianownik

    def toFloat(self):
        a = self.getLicznik()
        b = self.getMianownik()
        return a / b

    def __str__(self):
        return ("STR: Licznik: {} , Mianownik {} ".format(self.licznik, self.mianownik))

    def __mul__(self, other):
        return Ulamek(self.licznik*other.getLicznik(),self.mianownik*other.getMianownik())

#########################
class SuperUlamek(Ulamek):

    def uprosc(self):

        a = self.getLicznik()
        b = self.getMianownik()
        if (a == b):
            d = a
            new_l = a / d
            new_m = b / d
            return SuperUlamek(new_l, new_m)

        if a > b:
            a, b = b, a

        while a != 0:
            a, b = b % a, a

        d = math.fabs(b)

        new_l = self.getLicznik() / d
        new_m = self.getMianownik() / d
        return SuperUlamek(new_l,new_m)

    def multiplication(self, fraction2):
        result_l = self.getLicznik()*fraction2.getLicznik()
        result_m = self.getMianownik()*fraction2.getMianownik()
        result_fraction = SuperUlamek(result_l, result_m)
        print(result_fraction)
        return result_fraction.uprosc()

#########################
'''
ul  = Ulamek(1,2)
li = ul.getLicznik()
print(li)

fl = ul.toFloat()

print(ul)

ul2 = Ulamek(1,4)
print('Mnozenie ulamkow 1/2 * 1/4')
wynik = ul.multiplication(ul2)
print(wynik)
'''
fraction1 = SuperUlamek(10,21)
fraction2 = SuperUlamek(-35,6)
wynik = fraction1.multiplication(fraction2)
print(wynik)

fraction3 = Ulamek(1,4)
fraction4 = Ulamek(2,8)

print('przeciazony operator mnozenia')
wynik2 = fraction3*fraction4
print(wynik2)



