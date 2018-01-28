import math

def zad3():
    list_sin = []
    list_cos = []
    for i in range(0,90,9):
        results = sincos(i)
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

def sincos(x):
    rad = math.radians(x)
    result_sin = math.sin(rad)
    result_cos = math.cos(rad)
    #print('{:5.3f},{:5.3f}'.format(result_sin,result_cos))
    return (result_sin,result_cos)

zad3()

