import random

class Error(Exception):
    pass

class OutOfLuck(Error):
    def __init__(self, val):
        self.value = val
        self.message = 'Wylosowano liczbe 0! '
    def __str__(self):
        return repr(self.value)

# PLIK ISTNIEJACY
try:
    a = 2/0
except:
    print('Wystapil jakis wyjatek!')
else:
    print('Wszystko ok!')

try:
    x = random.randint(0,3)
    print(x)
    if x == 0:
        raise OutOfLuck(x)
except OutOfLuck:
    print('Wylosowano liczbe 0! ')
else:
    print('Nie zostal zgloszony wyjatek przy losowaniu')

try:
    file = open('plik.txt','r')
except FileNotFoundError:
    print("Nie ma takiego pliku!")
else:
    linesNumber = 0
    for line in file:
        print(line, end='')
        linesNumber = linesNumber+1
    file.close()
    print()
    print('Liczba linii to: ' + str(linesNumber))