#!/usr/bin/env python3.8

#1:
print("1##########")

def fun1(file, n):
    with open(file) as f:
        k=f.readlines()
    print(k[:n]) #n poczatkowych
    print(k[-n:]) #n koncowych
    print(k[::n]) #co n-tego
    print([line.split(" ")[n-1] for line in k]) #n-te slowo
    print([line[n-1] for line in k]) #n-ty znak

fun1("plik1.in",2)

#2:
print("2##########")

import glob
y=[]
yrange=[]

for file in glob.glob("*.in"):
    with open(file) as f:
        k=f.readlines()
        y2=[float(line.split(" ")[1]) for line in k]
        yrange.append(y2)
        for i in range(len(y2)):
            if i>=len(y): y.append(0)
            y[i]=y[i]+y2[i]
yr=[]
yra=[]
print(yrange)
for i in range(40):
    for j in range(len(yrange)):
        yr.append(yrange[j][i])
    yra.append(max(yr)-min(yr))


for i in range(len(y)):
    y[i]=y[i]/len(glob.glob("*.in"))
print(y)

wyniki = open("zad2", "w")
with open(glob.glob("*.in")[1]) as f:
    k=f.readlines()
x=[line.split(" ")[0] for line in k]


for i in range(len(yra)):
    w=str(x[i]) +" " +str(y[i])+" "+str(yra[i]) + "\n"
    wyniki.write(w)
wyniki.close()



#3:
print("3##########")

def fun3():
    plik = open("zad3", "w")
    plik.writelines('''Matplotlib jest biblioteką do tworzenia wykresów (https://matplotlib.org/). Wykorzystamy ją do wygenerowania prostego wykresu. Poniżej minimum konieczne, aby ten cel osiągnąć:

import matplotlib.pyplot as plt
#wyrysowanie krzywej y(x), 'o' oznacza styl punktu
plt.plot(x, y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnościami
plt.errorbar(x, y, marker='*', yerr=dy)
#opis osi
plt.xlabel('x')
#zapis do pliku, format określony przez rozszerzenie w nazwie
plt.savefig('res.pdf')

A to może się przydać do łatwego wczytywania plików (ale dzisiaj można z tego skorzystać tylko w skrypcie generującym wykresy)

import numpy as np
x,y=np.loadtxt(nazwa, unpack=True)''')
    plik.close()
fun3()



