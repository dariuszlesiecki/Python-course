#!/usr/bin/env python3

#1:
print("#1:")
class arithmeticOne:
    def __init__(self,a1,r,n):
        self.a1=a1
        self.r=r
        self.n=n
        self.i=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i<=self.n:
            an=self.a1
            self.a1+=self.r
            self.i+=1
            return an
        else:
            raise StopIteration



class arithmeticTwoNext:
    def __init__(self,a1,r,n):
        self.a1=a1
        self.r=r
        self.n=n
        self.i=1

    def __next__(self):
        if self.i<=self.n:
            an=self.a1
            self.a1+=self.r
            self.i+=1
            return an
        else:
            raise StopIteration    

class arithmeticTwo:
    def __init__(self,a1,r,n):
        self.a1=a1
        self.r=r
        self.n=n

    def __iter__(self):
        return arithmeticTwoNext(self.a1,self.r,self.n)


oneClass=arithmeticOne(1,2,5)
print("One class:")
for i in oneClass:
    print(i)
for i in oneClass:
    print(i) #doesnt work
print()

twoClasses=arithmeticTwo(1,2,5)
print("Two classes:")
for i in twoClasses:
    print(i)
print()
for i in twoClasses:
    print(i)
print()

#2:
print("#2:")
from math import pow
from scipy import integrate

class RandomNumber:
    def __init__(self):
        self.x=1

    def __iter__(self):
        return self

    def __next__(self):
        self.x=(44485709377909*self.x)%pow(2,48)
        return self.x

        

random=RandomNumber()
rand=iter(random)
for i in range(0,4):
    print(next(rand))


def myintegrate(f,xp,xk,n):
    #print("number of iterations:", n)
    
    yp=f(xp)
    yk=f(xk)
    dx=abs(xk-xp)
    dy=abs(yk-yp)
    area=dx*dy
    t=0  
    value=integrate.quad(f,xp,xk)[0]
    random=RandomNumber()
    rand=iter(random)
    for i in range(0,n):
        x=min(xp,xk)+next(random)%(max(xp,xk)-min(xp,xk)+1)
        y=min(yp,yk)+next(random)%(max(yp,yk)-min(yp,yk)+1)
        if(0<y<=f(x)):
            t+=1
        elif(0>y>=f(x)):
            t-=1
    out=area*t/n
    print("our integral:{}, integral:{}, iterations:{}".format(out,value,n))

myintegrate(lambda x:x*2+2,0,10,10000)

#3:
print("#3:")
class Pascal:
    def __init__(self,n):
        self.T=[1]
        self.n=n
        self.i=1

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.i<=self.n:
            tmp=[1]
            tmp2=self.T
            for i in range(0,len(self.T)):
                if i==len(self.T)-1:
                    tmp.append(1)
                else:
                    tmp.append(self.T[i]+self.T[i+1])
            self.T=tmp
            self.i+=1
            return (tmp2,sum(tmp2))
        else:
            raise StopIteration

pascal=Pascal(9)
for i in pascal:
    print("{} sum:{}".format(i[0],i[1]))

            