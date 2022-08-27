class ComplexNumbers:
    def __init__(self,real,img):
        self.r=real
        self.i=img
    def add(self,a,b):
        self.r+=a
        self.i+=b
    def mul(self,a,b):
        self.x=((self.r*a)-(self.i*b))
        self.y=((self.r*b)+(self.i*a))
        self.r,self.i=self.x,self.y
    def prit(self):
        print("{} + i{}".format(self.r,self.i))
a,b=map(int,input().split())
c1=ComplexNumbers(a,b)
a,b=map(int,input().split())
c2=ComplexNumbers(a,b)
key=int(input())
if(key==1):
    c1.add(c2.r,c2.i)
elif(key==2):
    c1.mul(c2.r,c2.i)
c1.prit()
