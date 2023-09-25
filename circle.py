import math
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return (math.pi)*((self.r)**2)
        
    def perimeter(self):
        return 2*math.pi*self.r

c1=circle(7)
print(c1.area())
print(c1.perimeter())
#sample change 