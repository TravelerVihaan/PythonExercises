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
'''

polozenia = { 'terrorysta' : 'iran'}

class Urzadzenie:

    def __init__(self, nazwa, polozenie, masa):
        self.nazwa = nazwa
        self.polozenie = polozenie
        self.masa = masa
        polozenia[self.nazwa] = self.polozenie

class UrzadzenieLatajace(Urzadzenie):

    def __init__(self, maxspeed, nazwa, polozenie, masa):
        self.nazwa = nazwa
        self.polozenie = polozenie
        self.masa = masa
        polozenia[self.nazwa] = self.polozenie
        self.maxspeed = maxspeed

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

#/////////////////////////////////////////////////////////
dronik = Dron(30, 'dron1', 'polska', 150)
print(polozenia)
dronik.zaatakuj('terrorysta')
dronik.zniszcz('terrorysta')
print(polozenia)