a=str(input())
b=len(a)
if b==6:
    if a[0]+a[1]==a[4]+a[5] or a[0]+a[1]==a[5]+a[4]:
        print(a[2]+a[3])
    else:
        print(a[0]+a[1]+a[4]+a[5])
else:
    print("Enter valid input")
