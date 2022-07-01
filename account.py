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
        self.statement=[]
        self.loan=0
       
    def deposit(self,amount):
        if amount<=0:
            return f"must be greater than 0"
        else:
            self.account_balance+=amount
            self.deposits.append({amount})
            self.withdrawal_transact['date']=self.date # to add items to a dict you need a key and value
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

    def full_Statement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration= transaction["Narration"]
            time= transaction["time"]
            date= time.strftime("%x/%X")
            print(f"{date}:   {Narration}   {amount}")

    def loaning(self,amount):    
        item = len(self.deposits)
        item_s = sum(self.deposits)
        limit = item_s*(1/3)
        amount+=(amount)*0.03 
       
        if amount<=100:
            return "Sorry we can't give you this loan, your loan must be more than 100 "
        elif self.loan>0:
            return f"Dear customer you still have a loan of {self.loan}"
        elif item<10:
            return f"Your deposits must be atleast 10"

        elif amount>=limit:
            return f"Dear customer you can't borrow {amount}is higher than a limit of {self.account_balance}"

        else:
            self.loan+=amount
            return f"Dear customer {self.full_name} your loan of ksh{amount} has been granted successfully" 

    def loan_repay(self,amount): 
        if amount<self.loan:
            self.loan-=amount
            return f"Dear customer you have paid {amount} and your loan balance is {paying}"
        else:
            over_pay = amount-self.loan
            self.account_balance+=over_pay
            return f"You succesfully completed paying your loan and the over pay is {over_pay} and your new balance is {self.account_balance}"                   
        
    def transfer(self,amount,new_name):
        # fee= amount*0.05
        # Total=fee+amount
        if amount<0:
            return f"Dear customer {self.full_name} your amount is too low"
        elif amount>self.balance:
            return f"Dear customer {self.full_name} you balance is {self.account_balance} and you need atleast {Total}"
        elif isinstance(new_name, Account):
            self.account_balance-=amount
            new_name.deposit(amount)
            new_name.balance+=amount
            return f"Dear customer you  have sent {amount} to {new} and your new balance is {account_balance}" 

               
#  Update the withdrawal method to store each withdrawal transaction as a dictionary like like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }

#all this thing am having an issue with. They think I don't understand but its  the mode of teaching thats the issue
#I literally love the language but the fact that they see me and feel i don't
#know what am doing is the issue. If only they believed in me as I believe in me
#maybe i'd be able to prove them wrong. But i seriously don't know how to go about that.
 