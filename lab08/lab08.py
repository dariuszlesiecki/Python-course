#!/usr/bin/env python3

#1:
print("1##########")

class something(Exception):
    pass
class wrongRange(Exception):
    pass
class wrongNumber(Exception):
    pass

def isNumber(a):
    try:
        int(a)
        return True
    except:
        return False

def isevaluable(a):
    try:
        x=0
        eval(a)
        return True
    except:
        return False


def Integrate(f,a,b,i):
    try:
        if isNumber(a) and isNumber(b) and isNumber(i) and isevaluable(f):
            if b<=a:
                raise wrongRange
            elif i<=0:
                raise wrongNumber
            else:
                dx=(b-a)/i
                value=0
                for x in range(i):
                    x=a+x*dx
                    f1=eval(f)
                    x=x+dx
                    f2=eval(f)
                    value+=0.5*(f1+f2)*dx
            print("Calka: ", value)
        else:
            raise something
    except wrongRange:
        print("Podano złe granice całkowania!")
    except wrongNumber:
        print("Liczba przedziałów mniejsza bądź równa 0!")
    except something:
        print("Cos innego poszlo nie tak!")

Integrate("x**2",0,2, 10)


#2:
print("2##########")

class notNumber(Exception):
    pass
class negative(Exception):
    pass


def CheckFunction(a,b):
    try:
        if isNumber(a) and isNumber(b):
            if a>=0 and b>=0:
                print("Pole: ", a*b)
            else:
                raise negative
        else:
            raise notNumber
    except notNumber:
        print("Nie jest liczba!")
    except negative:
        print("Liczba ujemna!")

def Area(a,b):
    CheckFunction(a,b)

Area(5.5,5)

#3:
print("3##########")

import glob
import numpy as np

class notSquare(Exception):
    pass
class wrongSeparator(Exception):
    pass

def isSquare(a):
    rows=len(a)
    for row in a:
        if len(row)!= rows:
            return False
    return True

def matrixProduct():
    listOfMatrix=[]
    for file in glob.glob("*.txt"):
        try:
            with open(file) as f:
                k=f.readlines()
                a=[line.split(" ") for line in k]
                for i in a:
                    for j in range(0,len(i)):
                        if isNumber(i[j]):
                            i[j]=int(i[j])
                        else:
                            raise wrongSeparator
                listOfMatrix.append(a)

        except wrongSeparator:
            print("Seperator nie jest spacja")
    for m in listOfMatrix:
        try:
            if not isSquare(m):
                listOfMatrix.remove(m)
                raise notSquare
        except notSquare:
            print("Macierz nie jest kwadratowa")        
    for i in range(0,len(listOfMatrix)-1):
        a=listOfMatrix[i]
        for j in range(i+1,len(listOfMatrix)):
            b=listOfMatrix[j]
            print("result"+str(i)+": ")
            print(np.dot(a,b))

matrixProduct()

