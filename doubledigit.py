a=int(input())
if 1000 <= a <= 9999:
    b=str(a)
    c=int(b[3].lower())
    if c%2==0:
         print(b[0]+b[1]+b[2]+"e")
    else:
       print(a)
