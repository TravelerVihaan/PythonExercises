'''Zdefiniuj klase Okrag konstruowana przez promien i posiadajaca metody
pole oraz drukuj ( z dokladnoscia do dwoch miejsc po przecinku, kazde z pol
na wydruku ma szerokosc 10 znakow) tak jak w przykladzie'''
import math

class Okrag:
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return (math.pi*math.pow(self.promien,2))

    def drukuj(self):
        pole_okregu = self.pole()
        print('{:10}'.format(self.__class__.__name__), end='')
        print('|', end='')
        print('{:10}'.format('promien'), end='')
        print('|', end='')
        print('{:10}'.format(str(self.pole.__name__)), end='')
        print()
        print('{:10}'.format(''), end='')
        print('|', end='')
        print('{:10}'.format(str(self.promien)), end='')
        print('|', end='')
        print('{:<10.2f}'.format(pole_okregu), end='')


#------------------------------
okrag1 = Okrag(5)
okrag1.drukuj()
