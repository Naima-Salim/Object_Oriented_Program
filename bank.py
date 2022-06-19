#creating an instance of a class
from datetime import datetime

class Account:
    def __init__(self, account_name):
        self.account_name=account_name
        self.balance=0
        self.loan=0
        self.transaction_fee=100
        self.date_time=datetime.now().strftime("%x %X")
        self.full=[]
        self.deposits=[]
        self.withdrawals=[]     
     
    def deposit(self,amount):
        if amount<=0:
            return f"deposit amount must be greater than zero"
        else:
          self.balance+=amount
          now=datetime.now()
          statement={"date":now, "amount":amount, "naration":f"Hello {self.account_name} you have deposited {amount} and your balance is {self.balance}"}
          self.deposits.append(statement)
          print(self.deposits)
        # return (f"Hello Naima Salim, you have deposited {amount} in your account and your new balance is {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            return f"insufficient amount"
        elif amount <=0:
            return f"withdraw amount must be greater than zero"
        else: 
            now=datetime.now()
            self.balance-=amount+self.transaction_fee
            statement={"date":now, "amount":amount,"narration":f"hello {self.account_name} you have withdrawn {amount} and your balance is {self.balance}"}
            self.withdrawals.append(statement)
            self.full.append(statement)
            print(self.withdrawals) 
            # return f"Hello Naima Salim you have withdrawn {amount} your new balance is {self.balance}"
    
    def deposits_statement(self):  
        for n in self.deposits: 
            print(f" your deposit is {n}")

    def withdrawals_statement(self):
        for n in self.withdrawals:
            print(f"you have withdrawn {n}")

    def full_statement(self):
        for states in self.full:
            self.date_time=states["date"]
            amounts=states["amount"]
            narration=states["narration"]
            print(f"{self.date_time}_________{amounts}_______{narration}")

    def current_balance(self):
        return {self.balance}        
       
    def borrow(self,amount):
        item = len(self.deposits)
        item_s = sum(self.deposits)
        limit = item_s*(1/3)
        amount+=(amount)*0.03

        if amount<=100:
            return "your loan must be more than 100 "
        elif self.loan>0:
            return f"Dear customer you still have a loan of {self.loan}"
        elif item<10:
            return f"Your deposits must be atleast 10"
        elif amount>=limit:
            return f"Dear customer you can't borrow {amount}is higher than a limit of {self.balance}"
        else:
            self.loan+=amount
            return f"Dear customer {self.account_name} your loan of ksh{amount} has been granted successfully"

    def loan_repay(self,amount):
        if amount<self.loan:
            paying = self.loan-amount
            return f"Dear customer you have paid {amount} and your loan balance is {paying}"
        else:
            over_pay = amount-self.loan
            self.balance+=over_pay
            return f"You succesfully completed paying your loan and the over pay is {over_pay} and your new balance is {self.balance}"

    def transfer(self,amount,account):
        fee= amount*0.05
        Total=fee+amount
        if amount<0:
            return f"Dear customer {self.account_name} your amount is too low"
        elif Total>self.balance:
            return f"Dear customer {self.account_name} you balance is {self.balance} and you need atleast {Total}"
        else:
            self.balance-=Total
            return f"Dear customer you  have sent {amount} to {account} and your new balance is {self.balance}"
