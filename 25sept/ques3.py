class shoppingcart:
    def __init__(self):
        self.items={}
    def add(self,item,price,quantity=1):
        if(item in self.items):
            self.items[item]["quantity"]+=quantity
        else:
            self.items[item]={"price":price,"quantity":quantity} 
    def remove(self,item,quantity=1):
        if item in self.items:
            if self.items[item]["quantity"]<=quantity:
                del self.items[item]
            else:
                self.items[item]["quantity"]-=quantity
    def total(self):
        temp=0
        for item, data in self.items.items():
            temp+=data["price"]*data["quantity"]
        return temp
    def printitems(self):
        for item, x in self.items.items():
            print(f"{item} -- Quantity: {x['quantity']} -- Price: {x['price']}")

c1=shoppingcart()
c1.add("Chips",10,4)
c1.add("Pencil",4,5)
c1.add("Peanuts",100)
c1.printitems()
print(c1.total())
c1.remove("Chips",2)
c1.remove("Pencil",1)
c1.printitems()
print(c1.total())
                              
            
            