#!/usr/bin/env python3.8

#1:
print("1##########")
#def CoinChange(k,nom):
    
#2:
print("")
print("2##########")

import random as r
N=1000
random0and1=[r.choice([0,1]) for i in range(N)]
#print(random0and1)
def ZeroOne(a):
    n=0
    for i in a:
        if i==0:
            n+=1
        else:
            yield n
            n=0

s=0
n=0
for i in ZeroOne(random0and1):
    s+=i
    n+=1
print("srednia odleglosc:", s/n)

#3:
print("")
print("3##########")
def Fibonacci():
    a,b=0,1
    yield a
    yield b
    while True:
        a,b=b,a+b
        yield b

def EvenOdd(a,b="even"):
    for i in a:
        if b=="even" and not i%2:
            yield i
        if b=="odd" and i%2:
            yield i
def GenUntill(a,b):
    for i in a:
        if i>b:
            break
        yield i
    

print("parzyste:",sum(GenUntill(EvenOdd(Fibonacci()),100))) 
print("nieparzyste:",sum(GenUntill(EvenOdd(Fibonacci(),"odd"),100))) 
            

#4:
print("")
print("4##########")
def Range(start,stop=None,step=1.):
    start=float(start)
    if stop==None:
        start,stop=0.,start
    while True:
        if step>0 and start>=stop:
            break
        if step<0 and start<=stop:
            break
        if step==0:
            break
        yield start
        start += step

r1=(range(7), range(-7), range(2,7), range(7,2), range(2,7,2), range(2,7,-2), range(7,2,2), range(7,2,-2))
r2=(Range(7), Range(-7), Range(2,7), Range(7,2), Range(2,7,2), Range(2,7,-2), Range(7,2,2), Range(7,2,-2))

testN=0  #numer testu do zmieniania 0-7
print("range:")
for i in r1[testN]:
    print(i)
print("my range:")
for i in r2[testN]:
    print(i)

#5:
print("")
print("5##########")
from math import log 

def logarithm():
    u=0.
    x0=1.
    a=0.05
    i=1
    x=1.
    while x<= 1.5:
        yield x, u, log(x)
        u = u + a/x
        x = x0 + i*a
        i += 1
for i in logarithm():
    print(i)