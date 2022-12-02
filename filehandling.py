
f=open('html.txt','w')
f.write("This is me psycheee")
f.close()
f=open('html.txt','r')
for each in f:
    print(each)