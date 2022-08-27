class Person:
    def SetValue(self,name,age):
        self.n=name
        self.a=age
    def GetValue(self):
        self.str="The name of the person is "+self.n+" and the age is "+self.a+"."
        print(self.str)
name=input()
age=input()
p=Person()
p.SetValue(name,age)
p.GetValue()
