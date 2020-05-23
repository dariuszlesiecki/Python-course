#!/usr/bin/env python3.8

import random as r

#1:
from time import time_ns
from sys import version
powt=1000
N=10000

def forStatement():
    k = []
    for i in range(N):
        k.append(i)
    return k

def listComprehension():
    return [i for i in range(N)]

def mapFunction():
    return map(lambda x: x, range(N))

def generatorExpression():
    return (i for i in range(N))

def tester(func):
    t  = time_ns()
    for _ in range(powt):
        func()
    t -= time_ns()
    return abs(t)


print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

####TEST 1 i
'''3.8.2 (default, Feb 26 2020, 02:56:10) 
[GCC 7.4.0]
forStatement         => 742269000
listComprehension    => 501336100
mapFunction          => 583100
generatorExpression  => 510200'''
####TEST 2 i**2
'''
w kazdej funkcji zwracajacej obiekt zamiast "i" daje "i**2"

3.8.2 (default, Feb 26 2020, 02:56:10) 
[GCC 7.4.0]
forStatement         => 2784716300
listComprehension    => 2510605000
mapFunction          => 451400
generatorExpression  => 556900'''
####TEST 3 sum for
'''
zmieniam funkcje tester
def tester(func):
    t  = time_ns()
    for _ in range(powt):
        s=0
        for i in func():
            s=s+i
    t -= time_ns()
    return abs(t)

3.8.2 (default, Feb 26 2020, 02:56:10) 
[GCC 7.4.0]
forStatement         => 886404200
listComprehension    => 734760900
mapFunction          => 1266248600
generatorExpression  => 999061300'''
####TEST 4 fun sum
'''
zmieniam funkcje tester
def tester(func):
    t  = time_ns()
    for _ in range(powt):
        sum(func())
    t -= time_ns()
    return abs(t)
3.8.2 (default, Feb 26 2020, 02:56:10) 
[GCC 7.4.0]
forStatement         => 819477100
listComprehension    => 525591300
mapFunction          => 738720700
generatorExpression  => 433961000'''
####TEST 5 list()
'''
zmieniam funkcje
def mapFunction():
    return list(map(lambda x: x, range(N)))


def generatorExpression():
    return list((i for i in range(N)))

3.8.2 (default, Feb 26 2020, 02:56:10) 
[GCC 7.4.0]
forStatement         => 740812800
listComprehension    => 481856700
mapFunction          => 881702500
generatorExpression  => 617879900'''

#2:
n=10000
punkty=[r.uniform(-1,1)**2 + r.uniform(-1,1)**2 for _ in range(n)]
pi=len(list(filter(lambda x: x<=1, punkty)))*4/n
print(pi)

#3:
m=[[2,2,5],
   [3,2,1],
   [4,9,2]]
m2=[[3,5,0],
    [0,5,5],
    [2,2,2]]

print(list(map(max,m))) #max w kazdym wierszu
print(list(map(max,zip(*m)))) #max w kazdej kolumnie
print([list(map(sum, zip(*i))) for i in zip(m, m2)]) #suma

#4:
from functools import reduce

k=[[1,3],[2,4],[3,5],[4,8],[5,10]]

print(reduce(lambda a,b : a+[b[0]] ,k))

#5:
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,5,6,8,9,2,2,3,5,7]

def f5(a,b):
    n=len(a)
    xsr= reduce(lambda x,y: x +y,a) /n
    ysr= reduce(lambda x,y: x +y,b) /n
    #D=reduce(lambda x,y: )
    return xsr
print(f5(x,y))




