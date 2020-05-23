#!/usr/bin/env python3.8

import random as r

#1:
print("")
print("1##########")
def fun1(a):
    s={}
    l=r.randrange(0,20)
    for i in range(0,l+1):
        key=r.random()
        s.setdefault(key,format(eval(a.format(key)),'.3f'))
    return s

print("wywolanie dla funkcji 3x+2: ",fun1('3*{}+2'))


#2:
print("")
print("2##########")
def fun2(*a):
    l=[]
    for i in a:
        for j in i:
            for k in a:
                if j not in k:
                    break
            else:
                l.append(j)
    return l

print("wspolne elementy: ",fun2([1,2,3,5],(2,3,44,5),[2,3,5,6]))


#3:
print("")
print("3##########")
def fun3(a,b,c=True):
    if c:
        return [(a[i],b[i]) for i in range(min(len(a),len(b)))]
    else:
        return [(a[i],b[i]) if i<min(len(a),len(b)) else (a[i],None) if len(a)>len(b) else (None,b[i]) for i in range(max(len(a),len(b)))]

print("funkcja przyjmujaca dwie sekwencje: ",fun3([1,3], [1,3,2,2,4],False))

#4:
print("")
print("4##########")
def maks(*a):
    m=max(a[0])
    for i in a:
        if max(i)>m:
            m=max(i)
    return m
def fun4(fun,*a):
    return fun(*a)
print("maksimum: ",fun4(maks,[2,3,5,1],[2,3,6,2,1,1]))
print("maksimum: ",fun4(maks,[2,3,5,1]))

#5:
print("")
print("5##########")
def fun5(a, b=(10,5,2)):
    s = {}
    for i in b:
        if a>0:
            n=a//i
            a=a-n*i
            s.setdefault(i,n)
    s.setdefault('r', a)
    return s

print("rozmienianie pieniedzy dla kwoty 19:",fun5(19) )
print("rozmienianie pieniedzy dla kwoty 148, inne nominaly:",fun5(148,(5,2,1)) )

#6:
print("")
print("6##########")
def fun6(x,a,b,s='r'):
    n=0
    found=0
    while(not found):
        if s=='r':
            y=r.randrange(a,b+1)
            found=1 if y==x else 0
            a+= 1 if y<x else 0
            b-= 1 if y>x else 0
        else:
            y=a+((b-a)//2)
            found=1 if y==x else 0
            a= a if y>x else y
            b= b if y<x else y
        n=n+1
    return n
print("ilosc krokow 'r':",fun6(3,0,10))
print("ilosc krokow podzial na pol:",fun6(3,0,10,'n'))
            