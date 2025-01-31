class Account:
    def __init__(self, owner, balance, balance_on_deposit = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        deposit_amount = int(input("Write deposit amount : "))
        if self.balance > deposit_amount: 
            self.balance = self.balance - deposit_amount
            print("Your current balance : ", self.balance)
        else: 
            print("Not enough balance!")


    def withdraw(self):
        withdraw_amount = int(input("Write withdraw amount : "))
        if self.balance > withdraw_amount: 
            self.balance = self.balance - withdraw_amount
            print("Your current balance : ", self.balance)
        else: 
            print("Not enough balance!")

account = Account("Flaw", 100)
account.deposit()
account.deposit()

account.withdraw()
