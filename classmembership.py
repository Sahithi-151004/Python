'''class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class B:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class C:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
a=A("Atchuth",17)
b=B("Atchuth","Bh-1")
c=C("Atchuth","90")
a.display()
b.display()
c.display()
print(isinstance(a,A))
print(isinstance(b,B))
print(isinstance(c,C))'''
class A:
    def school(self, name,age):
        print(name,age)
    def school(self,name,age,marks):
        print(name,age,marks)
a=A("LPU",23,67)
A.school()
