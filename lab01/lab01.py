#!/usr/bin/env python3.8

def f(x,a,b):
    return a*x +b


from sys import argv
if len(argv)>1:
    k="".join(argv[1:])
    print(f'{k=}')
    male=[i for i in k if i.islower()]
    print('male litery:',male)
    duze=[i for i in k if i.isupper()]
    print('duze litery:',duze)
    numbers=[int(i) for i in k if i.isnumeric()]
    print('cyfry:',numbers)
    nielitery=[i for i in k if not i.isalpha()]
    print('bez liter:',nielitery)
    malebez=[]
    for i in male:
        if i not in malebez:
            malebez.append(i)
    print('male bez powtorzen:',malebez)

    malekrotka=[(i,male.count(i)) for i in malebez]
    print('male z liczba powtorzen:',malekrotka)
    malekrotka.sort(key=lambda x:x[1])
    print('posortowane:',malekrotka)
    samogloski=('a','e','i','o','u','y')

    a=sum(k.lower().count(i) for i in samogloski)
    b=sum(1 for i in k if i.isalpha() and i.lower() not in samogloski)
    print(f'{a=}',f'{b=}')
    krotki=[(x,f(x,a,b)) for x in numbers]
    print('cyfra, f(x):',krotki)
    xsr=sum(x for x,y in krotki)/len(krotki)
    ysr=sum(y for x,y in krotki)/len(krotki)
    D=sum((x-xsr)**2 for x,y in krotki)
    a=(1/D)* sum(y*(x-xsr) for x,y in krotki)
    b=ysr-a*xsr
    print(f'{a=}',f'{b=}')
else:
    print("za malo elementow przy wywolaniu")