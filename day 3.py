math= int (input("enter your maths marks ="))
phy= int (input("enter your physics marks ="))
chem= int (input("enter your chemistry marks ="))
eng= int (input("enter your english marks ="))
comp= int (input("enter your computer marks ="))
tot=(math+phy+chem+eng+comp)/5
if(tot>90):
    print ("you are awarded grade A+")
elif(tot>80):
    print ("you are awarded grade A")
elif(tot>70):
    print ("you are awarded grade B")
elif(tot>60):
    print ("you are awarded grade C")
elif(tot>40):
    print ("you are awarded grade D")
else:
    print ("You are Failed")
    
    
