num1=int(input("enter your first digit ="))
num2=int(input("enter your first digit ="))
num3=int(input("enter your first digit ="))
num4=int(input("enter your first digit ="))
sum=num1+num2+num3+num4
large = 0
for i in reversed(range(sum)):
    if i==num1 or i==num2 or i==num3 or i==num4:
        large=i
print(large)        
