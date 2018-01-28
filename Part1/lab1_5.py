import time

def printCredits(nazwap, nazwaf, *arguments, **keywords):
    time.sleep(1)
    #print( '{:^80}'.format(nazwap))
    # WYPISANIE NAPISU 'PROGRAM POKAZOWY'
    np=''
    print('')
    for l in nazwap:
        np=np+l
        print('\r{:^80}'.format(np), end='')
        time.sleep(0.5)
    time.sleep(1)
    #####################
    # WYPISANIE NAPISU 'PROGRAM POKAZOWY'
    nf=''
    print('')
    for l in nazwaf:
        nf=nf+l
        print('\r{:^80}'.format(nf), end='')
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
       print('')
       for l in s:
           ss=ss+l
           print('\r{:^80}'.format(ss), end='')
           time.sleep(0.5)
       #print(s.center(80))
       time.sleep(1)
    

printCredits("Program pokazowy", "Zemsta markiza Cul-de-Sac", 60, 4, Scenariusz="Autor", Scenografia="Autor", Kamerowanie="Brak", Kostiumy="Natura")
