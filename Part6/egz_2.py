'''
Napisz funkcje zwracajaca kopie stringu ze zmienionymi malymi literami na
duze i duzymi na male.
String moze zawierac inne znaki niz litery - nie sa one zamieniane.
Mozna wykorzystac metody:
str.isupper(), str.islower(), ktore odpowiednio sprawdzaja czy dany string
zawiera znaki odpowiedniego typu (zwraca true lub false)
oraz str.upper(), str.lower() do zamiany znaków
'''

def reverseString(sentence):
    sen2 = ''
    for i in sentence:
        if i.isupper():
            sen2 = sen2 + i.lower()
        elif i.islower():
            sen2 = sen2 + i.upper()
        else:
            sen2 = sen2 + i
    return sen2

#-----------------------------
sentence = 'Lipiec 1999'
sentence2 = reverseString(sentence)
print(sentence2)