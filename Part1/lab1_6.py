import time

def printCredits(nazwap, nazwaf, lines_number,line_length=80, *arguments, **keywords):
    time.sleep(1)
    #print( '{:^80}'.format(nazwap))
    # WYPISANIE NAPISU 'PROGRAM POKAZOWY'
    np=''
    print('')
    for l in nazwap:
        np=np+l
        print('\r{:^%d}'.format(np, line_length), end = '')
        time.sleep(0.5)
    time.sleep(1)
    #####################
    # WYPISANIE NAPISU 'PROGRAM POKAZOWY'
    nf=''
    for i in range(lines_number):
        print('')
    for l in nazwaf:
        nf=nf+l
        print('\r{:^%d}'.format(nf, line_length), end='')
        time.sleep(0.5)
    time.sleep(1)
    ######################
    #print(nazwaf.center(80))
    #time.sleep(1)
    # WYPISANIE POZOSTALYCH NAPISOW
    keys = keywords.keys()
    for kw in keys:
       s = kw + ":" + keywords[kw]
       ss = ''
       for i in range(lines_number):
           print('')
       for l in s:
           ss=ss+l
           print('\r{:^%d}'.format(nf, line_length), end='')
           time.sleep(0.5)
       #print(s.center(80))
       time.sleep(1)
    

printCredits("Program pokazowy", "Zemsta markiza Cul-de-Sac", 4, 60, Scenariusz="Autor", Scenografia="Autor", Kamerowanie="Brak", Kostiumy="Natura")
