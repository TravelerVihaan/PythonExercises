import time

def printCredits(nazwap, nazwaf, *arguments, **keywords):
    time.sleep(1)
    print('{:^80}'.format(nazwap))
    time.sleep(1)
    print(nazwaf.center(80))
    time.sleep(1)
    keys = keywords.keys()
    for kw in keys:
       s = kw + ":" + keywords[kw]
       print(s.center(80))
       time.sleep(1)
    

printCredits("Program pokazowy", "Zemsta markiza Cul-de-Sac", Scenariusz="Autor", Scenografia="Autor", Kamerowanie="Brak", Kostiumy="Natura")

