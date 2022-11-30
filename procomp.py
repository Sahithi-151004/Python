a=str(input())
b=int(a[0])
c=int(a[-1])
p=b**c
print(p)
d=int(a)
if 10000 <= d <= 99999999:
    if p%2==0:
        print("True")
    else:
        print("False")
else:
    print("error")
    
