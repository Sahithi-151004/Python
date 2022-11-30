phy= int (input('enter the physics marks out of 100='))
math= int (input('enter the mathematics marks out of 100='))
sci= int (input('enter the science marks out of 100='))
chem= int (input('enter the chemistry marks out of 100='))
com= int (input('enter the computer marks out of 100='))
tot=((phy+math+sci+chem+com)/5)*100
if(tot<90):
    print('You Are Awarded Grade A')
elif(tot<80):
    print('You Are Awarded Grade B')
elif(tot<60):
    print('You Are Awarded Grade C')
elif(tot<40):
    print('You Are Awarded Grade D')
else:
    print("You are fucked up")
