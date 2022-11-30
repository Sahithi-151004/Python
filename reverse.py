s=input()
x=list(s)
a=x[0]
x[0]=x[-1]
x[-1]=a
print("".join(x))
