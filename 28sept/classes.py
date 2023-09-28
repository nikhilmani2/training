class Animal:
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
        
class Dog(Animal):
    def speak(self):
        return self.name + ' says Woof!'
class Cat(Animal):
    def speak(self):
        return self.name + ' says Meow!'
fido=Dog('Fido')
isis=Cat('Isis')
print(fido.speak())
print(isis.speak())

class Animal:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs
        
class Bear(Animal):
    def __init__(self,name,legs=4,hibernate='yes'):
        Animal.__init__(self,name,legs)
        self.hibernate=hibernate
        
yogi=Bear('Yogi') 
print(yogi.name)
print(yogi.legs)
print(yogi.hibernate)

print("-------------------------------------------")

class Car:
    def __init__(self,wheels=4):
        self.wheels=wheels
        
class Gasoline(Car):
    def __init__(self,engine='Gasoline',tank_cap=20):
        Car.__init__(self)
        self.engine=engine
        self.tank_cap=tank_cap
        self.tank=0
        
    def refuel(self):
        self.tank=self.tank_cap
        
class Electric(Car):
    def __init__(self,engine='Electric',kWh_cap=60):
        Car.__init__(self)
        self.engine=engine 
        self.kWh_cap=kWh_cap
        self.kWh=0
        
    def recharge(self):
        self.kWh=self.kWh_cap
        
class Hybrid(Gasoline,Electric):
    def __init__(self,engine='Hybrid',tank_cap=11,kWh_cap=5):
        Gasoline.__init__(self,engine,tank_cap)
        Electric.__init__(self,engine,kWh_cap)
        
prius=Hybrid()
print(prius.tank_cap)
print(prius.kWh_cap)
print(prius.kWh) 
prius.recharge()
print(prius.kWh)                                      




                               