'''class school:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class standard(school):
    pass
a=standard("Atchu",18)
a.display()'''
class school:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class student(school):
    def __init__(self,name,age):
        school.__init__(self,name,age)
        self.name=name
        self.age=age
x=student("wxyz",789)
y=school("Abcd",123)
x.display()
y.display()
