import types

class Obiekt:
    def rysuj(self):
        print('[ nieznany obiekt ]')

    wypelnienie = 'o'

class Prostokat(Obiekt):

    def __init__(self,w ,l ):
        self.width = w
        self.length = l

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def rysuj(self):
        print(self.length*self.wypelnienie)
        for i in range(self.width):
            print(self.wypelnienie+ (self.width*2)*' ' + self.wypelnienie)
        print(self.length * self.wypelnienie)

class Choinka(Obiekt):
    def __init__(self,h):
        self.height = h

    def rysuj(self):
        inc = 1
        for i in range(self.height+1):
            if inc > 1:
                print(self.wypelnienie.center(15),end='')
            ##
            for j in range(inc):
                ##if inc > 1:
                s = 3*j*self.wypelnienie
                print(s.center(15))
            inc = inc + 1

class ChoinkaZPrezentami(Choinka):
    def __init__(self,h):
        self.height = h

    def rysuj(self):
        Choinka.rysuj(self)
        print("""________
                 |      |
                 |      |
                 |      |
                 --------""".center(15))


#########################################
p1 = Prostokat(5,10)
p1.rysuj()
print()
c = Choinka(3)
c.rysuj()
czp = ChoinkaZPrezentami(3)
##czp.rysuj()
typ = type(c)
typ2 = type(Choinka)
print(typ)
##typ = type(p1)
print(typ)
print(typ2)
print('------------------------------')
for i in range(10):
    userChoice = input("Jaki obiekt chcesz narysowac \n 1 - prostokat \n 2 - choinka \n 3 - choinka z prezentem?")
    if int(userChoice) == 1:
        objectToDraw = Prostokat(5,10)
    elif int(userChoice) == 2:
        objectToDraw = Choinka(4)
    elif int(userChoice) == 3:
        objectToDraw = ChoinkaZPrezentami(4)
    else:
        print('Dokonales niepoprawnego wyboru')
    typeOfObject = type(objectToDraw)
    if issubclass(typeOfObject,type(c)):
        objectToDraw.rysuj()
    else:
        print("Obiekt nie jest choinka, lub choinka z prezentami wiec nie bedzie narysowany!")
