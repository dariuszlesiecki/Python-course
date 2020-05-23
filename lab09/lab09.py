#!/usr/bin/env python3



#1:


#2:
import copy

class badSize(Exception):
    pass
class badElems(Exception):
    pass
class cantAdd(Exception):
    pass
class outofrange(Exception):
    pass

class Tab:

    def __init__(self,i,j,*elems):
        try:
            self.i=i
            self.j=j
            if self.i<=0 or self.j<=0:
                raise badSize
            if len(elems)!=i:
                raise badElems
            for i in elems:
                if len(i)!=j:
                    raise badElems
            self.T=[]
            for i in elems:
                self.T.append(i)
        except badSize:
            print("zły wymiar tablicy")
        except badElems:
            print("zle podane elementy")
    
    def size(self):
        return (self.i,self.j)
    
    def __add__(self,o):
        s1=self.size()
        s2=self.size()
        try:
            if s1[0]!=s2[0] or s1[1]!=s2[1]:
                raise cantAdd
            t=copy.deepcopy(self)
            for _i in range(0,self.i):
                for _j in range(0,self.j):
                    t.T[_i][_j]=self.T[_i][_j]+o.T[_i][_j]
            return t
        except cantAdd:
            print("rozmiary nie sa takie same")

    def __iadd__(self, o):
        s1=self.size()
        s2=self.size()
        try:
            if s1[0]!=s2[0] or s1[1]!=s2[1]:
                raise cantAdd
            for _i in range(0,self.i):
                for _j in range(0,self.j):
                    self.T[_i][_j]+=o.T[_i][_j]
            return self
        except cantAdd:
            print("rozmiary nie sa takie same")

    def __str__(self):
        s=""
        for _i in range(0,self.i):
            for _j in range(0,self.j):
                s=s+str(self.T[_i][_j])+" "
            s=s+"\n"
        return s
    def __getitem__(self, k):
        try:
            return self.T[k]
        except (IndexError, ValueError):
            print("poza tablica")

    def __setitem__(self, index, value):
        try:
            if type(value)!=int and type(self.T[index])!=int:
                if len(value)!=len(self.T[index]):
                    raise badSize
            elif type(value)==int and type(self.T[index])!=int:
                raise badSize
            self.T[index]=value
        except badSize:
            print("zly rozmiar")
            
        
        


t=Tab(2,2,[1,2],[3,4])
t2=Tab(2,2,[1,1],[1,1])

print(t)
print(t2)
#print(t.size())
t3=t+t2
print(t3)
t3+=t2
print(t3)
print(t)

print(t[1])
t[1]=[2,3]
t[1]=[1,2,3]
t[1]=6
t[1][1]=6
print(t[1])
