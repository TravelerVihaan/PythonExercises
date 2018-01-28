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
        print(self.length*'-')
        for i in range(self.width):
            print('|'+ (self.width*2)*' ' + '|')
        print(self.length * '-')

class Choinka(Obiekt):
    def __init__(self,h):
        self.height = h

    def rysuj(self):
        inc = 1
        for i in range(self.height):
            if inc > 1:
                print('*'.center(15),end='')
            for j in range(inc):
                ##if inc != 1:
                s = 3*(j)*'*'
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
c = Choinka(3)
c.rysuj()
czp = ChoinkaZPrezentami(3)
czp.rysuj()