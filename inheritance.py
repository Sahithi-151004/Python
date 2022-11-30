class A:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

class B(A):
  def __init__(self, name, age):
    A.__init__(self, name, age)
a=A("Atchuth",17)
a.display()
