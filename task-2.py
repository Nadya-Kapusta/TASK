#Параметры передаются в качестве аргументов командной строки
#Ввод осуществляется при помощи команды "python task-1.py file1 file2"
import sys

def Dots(line,X1,Y1):
    line1 = line # считываем строку
    c=1
    x=''
    y=''
    # выводим строку print(file1.strip())
    for i in line1:
        if c==2:
            y=y+i
        if i==' ':
            c=2
        if c==1:
            x=x+i
    x=float(x)
    y=float(y)
    x=x-X1
    y=y-Y1
    s=(x**(2)+y**(2))**0.5
    return(s)


if len(sys.argv) > 1:
    f1 = open(sys.argv[1],'r') #координаты окружности
    f2 = open(sys.argv[2],'r') #координаты точек
c=1
X=''
Y=''
R=''
x=''
y=''
while True:
    file1 = f1.read() 
    if not file1: # прерываем цикл, если строка пустая
        break
    for i in file1:
        if i==' ': c=2
        if i=='\n': c=3
        if c==1:
            X=X+i
        if c==2:
            Y=Y+i
        if c==3:
            R=R+i
    X=float(X)
    Y=float(Y)
    R=float(R)

while True:
    line=f2.readline()
    if not line: 
        break
    S=Dots(line, X,Y)
    if S>R: print("2")
    elif S<R: print("1")
    elif S==R: print("0")
