import random
a=input("enter rock paper or scisscor  ")
b=(random.randrange(0,4 ))
if(b==1):
 print("it is stone from computer you have won if it is paper from your side otherwise you lose")
elif(b==2):
    print("it is paper from computer you have won if it is scissor from your side otherwise you lose")
else:
    print("it is scissor from computer you have won if it is stone from your side otherwise you lose")


