import math
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
    def volume(self):
        return (math.pi)*(self.radius **2)*(self.height)
    
    def surface_area(self):
        return ((2*math.pi*(self.radius**2))+(2*math.pi*self.radius*self.height))
        
    
c  = Cylinder(2,3)
print(c.volume())   
print(c.surface_area()) 