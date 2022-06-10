class Account:
    def __init__(self,full_name, number):
        self.full_name =full_name
        self.number =number
        self.account_balance=0
        self.deposits=[] #Add a new attribute to the class Account called deposits which by default is an empty list.
        self.withdraws=[]  #Add another attribute to the class Account called withdrawals which by default is an empty list.
        self.transaction=100
    def deposit(self,amount):
        if amount<=0:
            return f"must be greater than 0"
        else:
            self.account_balance+=amount
            self.deposits.append({amount})
            return f"Confirmed, you have deposited {amount}. Your new balance is {self.account_balance}"

        # self.amount=1000
        # self.amount=1500
        # self.amount=7500

            
    def withdraw(self,amount) :
        if amount> self.account_balance:
            return f"Insuffiecient funds"
        elif amount<=0:
            return f"must be greater than 0" 
        else:

             self.account_balance -= amount + self.transaction
             self.withdraws.append({amount})
    
       
        return f"You've withdrawn {amount} your new balance is {self.account_balance}"


    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for statements in self.withdraws:
            print(statements)
    def current_balance(self):
        return self.account_balance
        
         