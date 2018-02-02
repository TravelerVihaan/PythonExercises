'''
Napisz funkcje zwracajaca ilosc dni w podanym jako argument miesiacu
oraz roku.
W roku przestepnym (majacym 366 dni) luty ma 29 dni.
Rok jest przestepny jesli jest podzielny przez 4,
z wyjatkiem lat ktore sa podzielne przez 100 - wtedy musza byc podzielne
przez 400. Przyjmij, ze argumentami procedury moga byc liczby calkowite
(zadbaj o wlasciwe sprawdzenie poprawnosci zakresu tych liczb
'''
import calendar

def czyPrzestepny(miesiac, rok):
    if rok%4 == 0:
        if rok%100 == 0:
            if rok%400 == 0:
                year_days = 366
            else:
                year_days = 365
        else:
            year_days = 366
    else:
        year_days = 365

    month_days = calendar.monthrange(rok,miesiac)
    month_days = month_days[1]

    print('Liczba dni w '+str(rok)+' roku: '+str(year_days))
    print('Liczba dni w '+str(miesiac) +' miesiacu: '+str(month_days))

#------------------------------
czyPrzestepny(2,2000)