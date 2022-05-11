def fact(x):
   f=1
   for i in range(1,x+1):
        f*=i
   return f
x=int(input("enter the number"))
y=fact(x)
print(y)
