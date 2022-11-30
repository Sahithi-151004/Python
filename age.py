a=int(input("Enter the first student age = "))
b=int(input("Enter the second student age = "))
c=int(input("Enter the third student age = "))
if a>b and a>c :
    print(a,"is the oldest")
elif b>a and b>c:
    print(b,"is the oldest")
else:
    print(c,"is the oldest")
if a<b and  a<c:
    print(a,"is the youngest")
elif b<c and b<a:
    print(b,"is the youngest")
else:
    print(c,"is the youngest")
