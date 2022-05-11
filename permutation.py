'''n=int(input("enter the total items"))
r=int(input("enter the no. of items to be arranged"))
fact_n=1
for i in range(1,n+1 ):#or(n,0,-1)
#calculate n  factorial
 fact_n*=i
#calculate n-r factorial
x=n-r
fact_x=1
for i in range(1,x+1):
 fact_x*=i
p=fact_n/fact_x
print("p=",p)'''

#-----------------------------------BY FUNCTION CREATION-----------------------------------------------------------------------
def fact(n):
   fact_n=1
   for i in range(1,n+1):
       fact_n*=i    
   return(fact_n)

x=int(input("enter total items  "))
y=int(input("enter the no. of items to be arranged  "))
fx=fact(x)
fy=fact(x-y)
p=fx/fy
print("p= ",p)

