import math

def MyListComprehensions(items_set,transformation_fun,requirement, optional_arg=None):
    new_set = []
    if optional_arg is None:
        print("Brak dodatkowych argumentow")
        for i in range(len(items_set)):
            new_set.append(transformation_fun(items_set[i]))
    else:
        print("Istnieja dodatkowe argumenty")
        for i in range(len(items_set)):
            new_set.append(transformation_fun(items_set[i],optional_arg))


        #print(transformation_fun(2,2))

    print(new_set)

#####################
test_list = []
for i in range(10):
    test_list.append(i*2)

MyListComprehensions(test_list, math.pow, lambda x: True, 2)

MyListComprehensions(test_list, math.sin, lambda x: True)

MyListComprehensions(test_list, math.cos, lambda x: True)