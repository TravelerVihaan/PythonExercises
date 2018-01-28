file = open('plik.txt','r')

linesNumber = 0
for line in file:
    print(line, end='')
    linesNumber = linesNumber+1

file.close()
print()
print('Liczba linii to: ' + str(linesNumber))
