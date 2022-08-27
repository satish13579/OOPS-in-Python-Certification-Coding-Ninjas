from copy import deepcopy
class Polynomial:
    def __init__(self):
        self.degCoeff = []
    def setCoefficient(self,index,value):
        if(len(self.degCoeff)<index):
            for i in range(len(self.degCoeff),index):
                self.degCoeff.append(0)
            self.degCoeff.append(value)
        elif(len(self.degCoeff)>index):
            del self.degCoeff[index]
            self.degCoeff.insert(index,value)
        else:
            self.degCoeff.append(value)
    def __add__(self,o):
        self.temp=[]
        c1=len(self.degCoeff)
        c2=len(o.degCoeff)
        cmin=min(c1,c2)
        cmax=max(c1,c2)
        for i in range(cmin):
            self.temp.append(self.degCoeff[i]+o.degCoeff[i])
        for i in range(cmin,cmax):
            if(c1<=i):
                self.temp.append(o.degCoeff[i])
            else:
                self.temp.append(self.degCoeff[i])
        return self.temp
    def __sub__(self,o):
        self.temp=[]
        c1=len(self.degCoeff)
        c2=len(o.degCoeff)
        cmin=min(c1,c2)
        cmax=max(c1,c2)
        for i in range(cmin):
            self.temp.append(self.degCoeff[i]-o.degCoeff[i])
        for i in range(cmin,cmax):
            if(c1<=i):
                self.temp.append(0-o.degCoeff[i])
            else:
                self.temp.append(self.degCoeff[i])
        return self.temp
    def __mul__(self,o):
        self.temp={}
        self.li=[]
        c1=len(self.degCoeff)
        c2=len(o.degCoeff)
        for i,ele1 in enumerate(self.degCoeff):
            for j,ele2 in enumerate(o.degCoeff):
                ele=ele1*ele2
                pow=i+j
                if pow not in self.temp.keys():
                    self.temp[pow]=ele
                else:
                    self.temp[pow]+=ele
        m=max(self.temp.keys())
        for i in range(m+1):
            if i not in self.temp.keys():
                self.li.append(0)
            else:
                self.li.append(self.temp[i])
        return self.li
def run():
    count1 = int(input())
    degree1 = list(map(int,input().split()))
    coeff1 = list(map(int,input().split()))
    first = Polynomial()
    for i in range(count1):
        first.setCoefficient(degree1[i], coeff1[i])
    count2 = int(input())
    degree2 = list(map(int,input().split()))
    coeff2 = list(map(int,input().split()))
    second = Polynomial()
    for i in range(count2) :
        second.setCoefficient(degree2[i], coeff2[i])
    choice = int(input())
    result = Polynomial() 
    if choice == 1:
        result = first + second
        for i,ele in enumerate(result):
            if(ele!=0):
                print("{}x{}".format(ele,i),end=" ")
    elif choice == 2:
        result = first - second
        for i,ele in enumerate(result):
            if(ele!=0):
                print("{}x{}".format(ele,i),end=" ")
    elif choice == 3:
        result = first * second
        for i,ele in enumerate(result):
            if(ele!=0):
                print("{}x{}".format(ele,i),end=" ")
    elif choice == 4:
        third = deepcopy(first)
        if (third.degCoeff == first.degCoeff) :
            print("true")
        else :
            print("false")
    else:
        fourth = deepcopy(first)
        if (fourth.degCoeff == first.degCoeff) :
            print("true")
        else :
            print("false")
run()
