
# PLIK ISTNIEJACY
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

# PLIK NIEISTNIEJACY
try:
    file = open('plik2.txt','r')
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