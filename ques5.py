class Bank:
    def __init__(self):
        self.accounts={}
    def create(self,ac_number,balance=0):
        if ac_number not in self.accounts:
            self.accounts[ac_number]=balance
        else:
            print(f"Account {ac_number} already exists")
    def checkbalance(self,ac_number):
        if ac_number in self.accounts:
            return self.accounts[ac_number]
        else:
            return "Account is not there"
    def deposite(self,ac_number,amount):
        if ac_number in self.accounts:
            self.checkbalance(ac_number)
            self.accounts[ac_number]+=amount
            print("Deposite Successfull")
            self.checkbalance(ac_number)
        else:
            print("Account is not there")    
    def withdrawl(self,ac_number,amount):
        if ac_number in self.accounts:
            if amount>0 :
                if self.accounts[ac_number]>=amount:
                    self.checkbalance(ac_number)
                    self.accounts[ac_number]-=amount
                    print("Withdrawl Successfull")
                    self.checkbalance(ac_number)
                else:
                    print("Withrawal amount is more than balance")
            else:
                print("Amount must be positive")
        else:
            print("Account is not there")                           
b1=Bank()

b1.create("1001",1500)
b1.create("1002")  
b1.create("1003",100000)
print(b1.checkbalance("1001"))
print(b1.checkbalance("1002"))
print(b1.checkbalance("1003"))
b1.deposite("1002",5000)
print(b1.checkbalance("1001"))
print(b1.checkbalance("1002"))
print(b1.checkbalance("1003"))
b1.withdrawl("1003",7000)
print(b1.checkbalance("1001"))
print(b1.checkbalance("1002"))
print(b1.checkbalance("1003"))
b1.withdrawl("1001",100000)
print(b1.checkbalance("1001"))
print(b1.checkbalance("1002"))
print(b1.checkbalance("1003"))               