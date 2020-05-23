#1:
def newInstruction(s):
    newStr=""
    newStr=s+"+"+s+"-"+s+"-"+s+"+"+s
    return newStr


def fun1(n,s="F"):
    newStr=""
    for _ in range(n):
        newStr=newInstruction(s)
        s=newStr
    return s

import matplotlib.pyplot as plt

def Draw(n):
    ins=fun1(n)
    d=1
    xs=[0]
    ys=[0]
    x,y=0,0
    dx=1
    dy=0
    
    for ch in ins:
        if ch=="F":
            x=x+d*dx
            y=y+d*dy
            xs.append(x)
            ys.append(y)
        if ch=="+":
            if dx==1 and dy==0:
                dx,dy=0,1
            elif dx==0 and dy==1:
                dx,dy=-1,0
            elif dx==-1 and dy==0:
                dx,dy=0,-1
            elif dx==0 and dy==-1:
                dx,dy=1,0
        if ch=="-":
            if dx==1 and dy==0:
                dx,dy=0,-1
            elif dx==0 and dy==-1:
                dx,dy=-1,0
            elif dx==-1 and dy==0:
                dx,dy=0,1
            elif dx==0 and dy==1:
                dx,dy=1,0
    #print(xs,ys)
    plt.plot(xs, ys)
    name="plot"+str(n)+".png"
    plt.savefig(name)


#2 i 3:
convert=[[1,"I"],[4,"IV"],[5,"V"],[9,"IX"],[10,"X"],[40,"XL"],[50,"L"],
[90,"XC"],[100,"C"],[400,"CD"],[500,"D"],[900,"CM"],[1000,"M"]]

def ArabicToRoman(number):
    i=len(convert)-1
    #print(convert)
    Roman=""
    while number>0:
        while convert[i][0]>number: i-=1
        Roman+=convert[i][1]
        number-=convert[i][0]
    #print(Roman)
    return Roman

def RomanToArabic(number):
    Arabic=0
    k=[]
    for j in number:
        for i in convert:
            if j in i: k.append(i[0])
    i=0
    while i<len(k):
        if i<(len(k)-1):
            if(k[i]<k[i+1]):
                Arabic=Arabic+k[i+1]-k[i]
                i+=2
            else:
                Arabic=Arabic+k[i]
                i+=1
        else:
            Arabic=Arabic+k[i]
            i+=1
    #print(Arabic)
    return Arabic

