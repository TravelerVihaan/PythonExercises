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
        return a/b

    def multiplication(self, fraction2):
        result_l = self.getLicznik()*fraction2.getLicznik()
        result_m = self.getMianownik()*fraction2.getMianownik()
        return Ulamek(result_l, result_m)

    def __str__(self):
        return("STR: Licznik: {} , Mianownik {} ".format(self.licznik, self.mianownik))

#########################

ul  = Ulamek(1,2)
li = ul.getLicznik()
print(li)

fl = ul.toFloat()

print(ul)

ul2 = Ulamek(1,4)
print('Mnozenie ulamkow 1/2 * 1/4')
wynik = ul.multiplication(ul2)
print(wynik)


    
