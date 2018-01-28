import random

def blur(lista):
	blista = []
	for i in range(20):
		if i == 0:
			blista.append(lista[i])
		elif i == 19:
			blista.append(lista[i])
		else:
			blista.append((lista[i-1]+lista[i]+lista[i+1])/3)
	return blista

lista = []

for i in range(20):
    lista.append(random.randint(0,100))

print(lista)
lista2 = blur(lista)
print(lista2)

