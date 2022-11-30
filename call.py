name="harry"
def sum():
    return name
print(sum())

def add_fun(a,b):
    return a+b
print(add_fun(3,4))

def add():
    a=int(input("Enter value:"))
    b=int(input("Enter value:"))
    c=a+b
    return c
sum=add()
print(sum)

def add(a,b):
    c=a+b
    return c
x=int(input("enter value:"))
y=int(input("enter value:"))
z=add(x,y)
print(z)
#lambda Function
#any number of arguments but can have only one expressions
c=lambda a:a+10
print(c(5))
x=lambda a,b:a*b*b
print(x(5,6))
x=lambda a,b,c:a+b+c
print(x(5,6,2))
#Recursion
def reccur_fact(n):
    if n==1:
        return n
    else:
        return n*reccur_fact(n-1)

#driver code
number=int(input("Enter the number you want the factorial:"))
if number==0:
    print("The Factorial is 0")
elif number<0:
    print("Enter Valid number")
else:
    print("the factiorial of",number,"is",reccur_fact(number))

#sum using reccursion
def sum(n):
    if n==1:
        return 1
    else:
        return (n+sum(n-1))
n=int(input("Enter Number: "))
z=sum(n)
print(z)

