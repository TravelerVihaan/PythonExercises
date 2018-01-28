import mymodule
import random

########################
def SincosModuleTest():
    list_sin = []
    list_cos = []
    for i in range(0,90,9):
        results = mymodule.sincos(i)
        list_sin.append(results[0])
        list_cos.append(results[1])
        #list_results.append(results)
        #print('kąt: {}; sin: {:5.3f}; cos: {:5.3f}\n'.format(i,results[0],results[1]))

    list_results = [(list_sin[x],list_cos[x]) for x in range(len(list_sin))]

    ln = len(list_sin)
    list_strings = [(str('%.3f' %list_sin[x]),str('%.3f' %list_cos[x])) for x in range(ln)]

    for i in range(ln):
        angle = i*9
        print('kąt: {}; sin: {}; cos: {}\n'.format(angle, list_strings[i][0], list_strings[i][1]))


########################
def BlurModuleTest():
    lista = []

    for i in range(20):
        lista.append(random.randint(0, 100))

    print(lista)
    lista2 = mymodule.blur(lista)
    print(lista2)
########################
SincosModuleTest()
print()
BlurModuleTest()
