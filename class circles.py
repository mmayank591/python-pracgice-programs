class circle:
    def __init__(self,radius):
        self.radius=radius
    def area (self):
        return 3.14*self.radius*self.radius
    def circufrence(self):
        return 2*3.14*self.radius

#circle1=circle(5)               BY DEFAULT METHOD
p#rint(circle1.area())
x=int(input("enter the radius of circle "))               #BY TAKING VALUE FROM FROM USER
print(circle1.area())
