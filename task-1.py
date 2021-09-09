#Параметры передаются в качестве аргументов командной строки
#Ввод осуществляется при помощи команды "python task-1.py n m"
import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
    m = int(sys.argv[2])

if n<1:
    print("ERROR, INVALID n VALUE")
if m<1:
    print("ERROR, INVALID m VALUE")
k = m
answ = '1'
while k!=1:
    answ = answ + str(k)
    k = k+(m-1)
    if k > n:
        k=k-n
print(answ)
