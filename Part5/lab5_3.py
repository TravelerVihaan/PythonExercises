'''
Zadanie 4. Utwórz słownik (np. położenia) zawierający wpisy nazwa obiektu → położenie. Stwórz
klasy:
• Urządzenie – posiada nazwę, położenie oraz masę. Po stworzeniu wpisuje się do słownika
położenia.
• UrządzenieLatające – dziedziczy po klasie Urządzenie, posiada maksymalną prędkość oraz
metodę lećDo, która zmienia położenie, wypisuje informację o locie oraz zmniejsza masę
(lot zużywa paliwo).
• UrządzenieWojskowe – dziedziczy po klasie Urządzenie, posiada metodę zaatakuj
przyjmującą jako argument nazwę obiektu do zaatakowania. Położenie obiektu pobierane
jest ze słownika położenia. Jeśli UrządzenieWojskowe nie jest tam, gdzie jego cel, to nie
może zaatakować. Zaatakowanie zmniejsza masę (atakowanie zużywa amunicję) i usuwa cel
ze słownika położenia.
• Dron – dziedziczy po klasach UrządzenieLatające i UrządzenieWojskowe, posiada metodę
zniszcz przyjmującą jako argument nazwę obiektu do zniszczenia. Metoda ta powoduje lot
do miejsca w którym jest cel, a nastepnie zaatakowanie go (lećDo klasy UrządzenieLatające
oraz zaatakuj klasy UrządzenieWojskowe).
Stwórz obiekt klasy Dron, dodaj do słownika położenia jakiś cel (np. terrorystę w Iranie) i naślij na
niego drona.
Wypisz masę drona po zakończonej akcji.

Do programu z zadania 4. dodaj klasę KurczakBojowy dziedziczącą po klasie
UrządzenieWojskowe, posiadającą zmienną opisującą poziom głodu, oraz klasę Beczka. Stwórz listę
20 dronów (obiekty klasy Dron), 5 kurczaków bojowych (obiekty klasy KurczakBojowy) oraz jedną
beczkę (obiekt klasy Beczka). Wymieszaj listę i przejdź po każdym z jej elementów. Jeśli element
jest urządzeniem latającym, zwiększ jego maksymalną prędkość lotu. Jeśli jest urządzeniem,
zmniejsz masę o połowę. Nakarm wszystkie kurczaki bojowe (wyzeruj poziom głodu). Po
natrafieniu na beczkę, wypisz „Bum!”.
Wykorzystaj funkcje isinstance oraz issubclass.
Do wymieszania listy można wykorzystać funkcję shuffle w module random.
'''

import random

polozenia = { 'terrorysta' : 'iran'}

class Urzadzenie:

    def __init__(self, nazwa, polozenie, masa):
        self.nazwa = nazwa
        self.polozenie = polozenie
        self.masa = masa
        polozenia[self.nazwa] = self.polozenie

class UrzadzenieLatajace(Urzadzenie):

    maxspeed = 150

    def lecDo(self, nowepolozenie):
        self.polozenie = nowepolozenie
        self.masa -= 10

class UrzadzenieWojskowe(Urzadzenie):

    def zaatakuj(self, cel):
        if self.polozenie == polozenia[cel]:
            print('Atak udany!')
            self.masa -= 2
            del polozenia[cel]
        else:
            print('Nie udalo sie zaatakowac')

class Dron(UrzadzenieLatajace, UrzadzenieWojskowe):

    def zniszcz(self, dozniszczenia):
        self.lecDo(polozenia[dozniszczenia])
        self.zaatakuj(dozniszczenia)

class KurczakBojowy(UrzadzenieWojskowe):
    glod = 5

class Beczka:
    pass

#/////////////////////////////////////////////////////////
dronik = Dron('dron1', 'polska', 150)
print(polozenia)
dronik.zaatakuj('terrorysta')
dronik.zniszcz('terrorysta')
print(polozenia)
print('----------------------------------')
#////////////////////////////////////
lista = []
for i in range(16):
    if i < 10:
        lista.append(Dron('dron'+str(i), 'anglia', 150))
    elif i > 9 and i < 15:
        lista.append(KurczakBojowy('kurczak'+str(i), 'hiszpania', 200))
    else:
        lista.append(Beczka())

random.shuffle(lista)

for j in lista:
    print(type(j))
    if issubclass(type(j),UrzadzenieLatajace):
        j.maxspeed+=20
        print('UrzadzenieLatajace')
    if issubclass(type(j),Urzadzenie):
        j.masa = j.masa/2
        print('Urzadzenie')
    if isinstance(j,KurczakBojowy):
        j.glod = 0
        print('Kurczak')
    if isinstance(j,Beczka):
        print('Bum!')
