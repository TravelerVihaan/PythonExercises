import random
#FUN1
def sumaElementPoElemencie(list1, list2):
    sumaList = [list1[x]+list2[x] for x in range(20)]
    return sumaList

#FUN2
def sumaKazdyZKazdym(list1, list2):
    sumaKZK = [ i+j for i in list1 for j in list2]
    return sumaKZK

lista = []

for x in range(20):
    lista.append(random.randint(0,10))

#print(lista)

listal = []

for y in range(10):
    listal.append(lista)

print(listal[0])
print(listal[1])

suma = sumaElementPoElemencie(listal[0], listal[1])

print(suma)

suma2 = sumaKazdyZKazdym(listal[0], listal[1])

print(suma2)


