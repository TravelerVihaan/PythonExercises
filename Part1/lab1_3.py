def sprawdzenieLiczby(x):
    if x > 1:
        for i in range(2,x):
            if(x % i) == 0:
                print(x,' nie jest liczba pierwsza')
                break;
        else:
            print(x,' jest liczba pierwsza')
    else:
       print(x,"nie jest liczba pierwsza")


liczba = int(input("Podaj liczbe, ktora chcesz sprawdzic"))
sprawdzenieLiczby(liczba);

