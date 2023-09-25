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
                           