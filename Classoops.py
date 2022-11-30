class college:
    def student(self):
        self.name=input("1:")
        self.marks=int(input("2:"))
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
a=college()
a.student()
a.display()
