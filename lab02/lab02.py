#!/usr/bin/env python3.8
from sys import argv
import random

#1:
print("")
print("1##########")
def isPrime(x):
    if x>1:
        for i in range(2,x//2):
            if (x%i)==0:
                return False
        else:
            return True
    else:
        return False

print("13 pierwsza: ",isPrime(13))
print("12 pierwsza: ",isPrime(12))
print("")

#2:
print("")
print("2##########")
s1={}

while(len(s1)<50):
    x=int(random.randrange(0,100))
    if x not in s1.keys():
        s1[x]=isPrime(x)
print("slownik liczba:True/False  :",s1)


#3:
print("")
print("3##########")
myList = [random.randrange(0,11) for i in range(100)]
s2 = {}
x=0
for i in myList:
    s2.setdefault(i,[]).append(myList.index(i,x))
    x=myList.index(i,x)+1
print("slownik liczba:indeksy :",s2)


#4:
print("")
print("4##########")
s3={}
s4={}
mylist=[]
if len(argv) > 1: 
    number = int(argv[1])
    s3 = {i:random.randrange(2,15) for i in range(1,number+1)}
    myList = [(j,i) for i,j in s3.items()]
    s4 = {j:i for i,j in s3.items()}
    myList.append(s4)
print("slownik: ", s3)
print("lista: ", myList)


#5:
print("")
print("5##########")
l2=[random.randrange(0,20) for i in range(100)]
even={}
odd={}

for i,j in enumerate(l2):
    if j%2:
        odd.setdefault(j,[]).append(i)
    else:
        even.setdefault(j,[]).append(i)
print("even:",even)
print("odd:", odd)
s4 = { x:y if [i for i in y if i%3 == 0] else (y[-1],y[0]) for x,y in even.items() }
print("slownik: ",s4)

#6:
print("")
print("6##########")
d1={i:random.randrange(1,100) for i in range(1,11)}
d2={i:random.randrange(1,100) for i in range(1,11)}
print("d1:", d1)
print("d2:", d2)
for i in range(1,11):
    a=d1[i]
    b=d2[i]
    del d1[i]
    del d2[i]
    d1[a]=i
    d2[b]=i
print("d1 obrocone: ",d1)
print("d2 obrocone: ",d2)

d1d2={}
for i in d1.keys():
    if i in d2.keys():
        d1d2[i]=(d1[i],d2[i])
print("po polaczeniu: ",d1d2)

    