class Kwadraty:
    def __init__(self,s):
        self.num = s
        self.lista = ['a','b','c','d']

    def __iter__(self):
        return self

    def f(self):
        return self.lista[self.num%4]

    def __next__(self):
        self.num += 1
        #return (self.num-1)**2
        return self.f()

counter = 0
for i in Kwadraty(5):
    print(i)
    if counter > 10:
        break
    counter=counter+1