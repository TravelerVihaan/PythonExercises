class Kwadraty:
    def __init__(self,num, end):
        self.num = num
        self.end = end
        self.lista = ['a','b','c','d']

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        #stopowanie iteratora
        square = (self.num-1)**2
        if self.end == square:
            raise StopIteration
        return square
        #return self.f()

# PROGRAM GLOWNY
#counter = 0
for i in Kwadraty(4, 25):
    print(i)
    if i > 1000:
        break
    #counter=counter+1