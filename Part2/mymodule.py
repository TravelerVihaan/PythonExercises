#This is module using in lab2_7
import math

######################
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

######################
def sincos(x):
    rad = math.radians(x)
    result_sin = math.sin(rad)
    result_cos = math.cos(rad)
    #print('{:5.3f},{:5.3f}'.format(result_sin,result_cos))
    return (result_sin,result_cos)