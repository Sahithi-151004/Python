class Append:
    def __init__(self,a):
        self.a=a
    def midchar(self):
        x="*"
        b=len(self.a)
        if b%2==0:
            return(self.a[:b/2]+x+self.a[b/2:])
a=input()
obj=Append(a)
print(obj.midchar())
