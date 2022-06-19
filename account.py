from datetime import datetime
class Account:
    def __init__(self,full_name, number):
        self.full_name =full_name
        self.number =number
        self.account_balance=0
        self.deposits=[] #Add a new attribute to the class Account called deposits which by default is an empty list.
        self.withdraws=[]  #Add another attribute to the class Account called withdrawals which by default is an empty list.
        self.transaction=100
        self.withdrawal_transact={}
        self.deposit_transact={}
        self.now=datetime.now()
        self.date=self.now.strftime('%d/%M/%Y')
       
    def deposit(self,amount):
        if amount<=0:
            return f"must be greater than 0"
        else:
            self.account_balance+=amount
            self.deposits.append({amount})
            self.withdrawal_transact['date']=self.date
            self.withdrawal_transact['amount']=amount
            self.withdrawal_transact['narrations']=  "Confirmed, you have deposited", {amount}," Your new balance is", {self.account_balance}


            return self.withdrawal_transact

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
             self.deposit_transact['date']=self.date
             self.deposit_transact['amount']=amount
             self.deposit_transact['narrations'] =  "Confirmed, you have withdrawn", {amount}," Your new balance is", {self.account_balance}

    
       
             return self.deposit_transact


    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for statements in self.withdraws:
            print(statements)
    def current_balance(self):
        return self.account_balance
        
#  Update the withdrawal method to store each withdrawal transaction as a dictionary like like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }
