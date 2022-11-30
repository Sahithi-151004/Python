a=int(input())
if 1000<=a<=9999:
    b=str(a)
    i=int(b[0])
    j=int(b[3])
    if i%2!=0 and j%2!=0:
        print("True")
    else:
        print("False")
