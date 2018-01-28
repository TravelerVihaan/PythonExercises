'''
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
        if self.end == (self.num-1)**2:
            raise StopIteration
        return (self.num-1)**2
        #return self.f()

# PROGRAM GLOWNY
#counter = 0
for i in Kwadraty(4, 25):
    print(i)
    if i > 1000:
        break
    #counter=counter+1
    '''

def f(n):
    return n**2

def gen(k):
    for i in range(k):
        yield f(i)

for z in gen(10):
    print(z)


print('----------------------------')

class Kwadraty:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return (self.num-1)**2

for i in Kwadraty():
    print(i)
    if i > 100:
        break
