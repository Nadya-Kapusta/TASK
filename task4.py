#Параметры передаются в качестве аргументов командной строки
#Ввод осуществляется при помощи команды "python task-1.py file"

import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
f = open(file)
file1 = f.read().splitlines()

array = [int(elem) for elem in file1]
array2 = array.copy()
while len(array)>2:
    array.remove(max(array))
    array.remove(min(array))

total=0
total2=0

if len(array)==1:
    for a in array2:
        total=total+abs(int(a)-int(array[0]))
    print(total)
elif len(array)==2:
    for a in array2:
        total=total+abs(int(a)-int(array[1]))
        total2=total+abs(int(a)-int(array[0]))
    if total>total2: print(total2)
    else: print(total)