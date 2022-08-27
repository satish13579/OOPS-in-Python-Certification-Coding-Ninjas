from math import gcd
class Fraction:
    def __init__(self,num,den):
        self.n=num
        self.d=den
    def add(self,x,y):
        if(y==self.d):
            self.n+=x
        else:
            self.lcm=self.d*y
            self.n=(self.n*(self.lcm//self.d))+(x*(self.lcm//y))
            self.d=self.lcm
        self.sim()
    def mul(self,x,y):
        self.n*=x
        self.d*=y
        self.sim()
    def sim(self):
        self.g=gcd(self.n,self.d)
        self.n//=self.g
        self.d//=self.g
    def prit(self):
        print("{}/{}".format(self.n,self.d))
a,b=map(int,input().split())
f1=Fraction(a,b)
n=int(input())
for i in range(n):
    k,a,b=map(int,input().split())
    if(k==1):
        f1.add(a,b)
    else:
        f1.mul(a,b)
    f1.prit()
