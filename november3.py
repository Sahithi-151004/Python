def pow(b,e):
    if e==0:
        return 1
    else:
        return (b*pow(b, e-1))
b=int(input())
e=int(input())
if 1<= b <=10**3 and 1<= e <= 10**3:
    print(pow(b,e))
