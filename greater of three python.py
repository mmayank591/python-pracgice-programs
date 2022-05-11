a=int(input("enter 1st number   "))
b=int(input("enter 2nd number  "))
c=int(input("enter 3rd number     "))
if(a==b==c):
 print("all are equal")
elif(a==b):
    if(c>a):
      print(a,"is equal to",b,"and",c,"is gteater than ",a,"and",b)
    else:
        print("a is equal to and b and c is less than a and b")
 
elif(b==c and a>b):
 print(b,"is equal to",c,"and",a,"is gteater than ",b,"and",c)
elif(c==a and b>a):
 print(c,"is equal to",a,"and",b,"is gteater than ",c,"and",a)
elif(a>b and a>c):
 print(a,"is greater than",b,"and",c)
elif(b>a and b>c):
 print(b," is greater than ",a,"and",c)
else:
 print(c,"is greater than",a,"and",b)
