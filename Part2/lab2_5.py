list_numbers = []

for i in range(40):
    list_numbers.append(i)

print("Full list")
print(list_numbers)

for i in range(39,0,-2):
    del list_numbers[i]

print("After deleting every other element")
print(list_numbers)

ll = len(list_numbers)
print(ll)
newll = ll + int(ll/4)

for i in range(0,newll,4):
    list_numbers.insert(i,-1)

print("After extend list on the begining and end by -1 values")
print(list_numbers)

a=0
b=4
while b < len(list_numbers):
    for i in range(a,b):
        print(list_numbers[i],end=', ')
    print()
    a=b
    b=b+4

list_numbers.remove(list_numbers[len(list_numbers)-1])

print(list_numbers)

