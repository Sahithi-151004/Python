'''class school:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}{self.age}"
a=school("Hena",8)
print(a)'''
class school:
    def __init__(self,name):
        self.name=name
    def add(self):
        print("My Name Is "+self.name)
a=school("Atchuth")
a.add()

        
