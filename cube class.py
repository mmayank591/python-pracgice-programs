class cube:
    def __init__(self,side):
        self.side=side
    def volume(self):
        return self.side*self.side*self.side
cube1=cube(5)
print(cube1.volume())
a=int(input("enter the side of cube "))
cube1=cube(a)
print(cube1.volume())
