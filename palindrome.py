num=int(input("Enter the number:"))
inv=0
rem=0
while num>0:
    rem=num%10
    num=num//10
    inv=inv*10
    inv=inv+rem
print(inv)
