class Account:
    def __init__(self,full_name, number, account_balance):
        self.full_name =full_name
        self.number =number
        self.account_balance=account_balance
    def deposit(self,amount):
        self.amount=amount
        return f"your new balance is {self.account_balance + amount}" 
    def withdraw(self,cash) :
        self.cash=cash  
        return f"You withdrawn {self.account_balance - cash}"
    