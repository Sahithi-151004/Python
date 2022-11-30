def max (num1,num2):
    if num1>num2:
        print("num1 is greater")
    elif num2>num1:
        print("num2 is greater")
    else:
        print("both are equal")
max(20,10)
def emp(name,age):
    print("Name:",name,"Age:",age)
emp(age=25,name="harry")
#parameters with default values
def emp (name,msg="Welcome"):
    print("Hello",name,msg)
emp("Harry")
