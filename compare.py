num1=int(input("enter your first digit ="))
num2=int(input("enter your first digit ="))
num3=int(input("enter your first digit ="))
num4=int(input("enter your first digit ="))
large=0

if (num1>=num2) and (num1>=num3) and (num1>=num4):
    print(num1,"is the largest")
elif (num2>=num1) and (num2>=num3) and (num2>=num4):
    print(num4,"is the largest")
elif (num3>=num1) and (num3>=num2) and (num3>=num4):
    print(num3,"is the largest")
else:
    print(num4,"is the largest")
