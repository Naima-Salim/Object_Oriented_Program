#creating an instance of a class
class Account:
    def __init__(self, account_name):
        self.account_name=account_name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]

#Assignment
# Add these methods to class Account - deposit, withdraw.
#Create two instances of account and verify they work as expected.

#Assignment
# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.
    def deposit(self,amount):
        if amount<=0:
            return f"deposit amount must be greater than zero"
        else:
          self.balance+=amount
          self.deposits.append(amount)
        return (f"Hello Naima Salim, you have deposited {amount} in your account and your new balance is {self.balance}")
    
    def withdraw(self,amount):
        if amount > self.balance:
            return f"insufficient amount"
        elif amount <=0:
            return f"withdraw amount must be greater than zero"
        else:
            self.withdrawals.append(amount)
            self.balance-=amount+100
            return f"Hello Naima Salim you have withdrawn {amount} your new balance is {self.balance}"

    
    def deposits_statement(self):
        for n in self.deposits:
            print(f" your deposit is {n}")

    def withdrawals_statement(self):
        for n in self.withdrawals:
            print(f"you have withdrawn {n}")

       
