import sys

fun_list = dir(sys)
samogloski = 'aiueoy'
fun_dictionary = {}

"""
print(temp_list)

for i in range(len(temp_list)):
    fun_list.append(temp_list[i][2:len(temp_list[i])-2])
"""

print(fun_list)


for i in range(len(fun_list)):
    fun_name = fun_list[i]
    print(fun_name)
    if fun_name[0] in samogloski:
        fun_dictionary[fun_list[i]] = len(fun_list[i])

print('--------------------------------')
"""
dictionary_list = list(fun_dictionary.keys())
for i in dictionary_list:
    print(i)

print('--------------------------------')
sorted_d_list = sorted(fun_dictionary.keys())
for i in sorted_d_list:
    print(i)
"""
print('--------------------------------')
for nazwa, dlugosc in fun_dictionary.items():
    print(nazwa + ': ' + str(dlugosc))