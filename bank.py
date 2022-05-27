#creating an instance of a class
class Account:
    def __init__(self, Account_Name,amount):
        self.Account_Name=Account_Name
        self.amount=amount

#Assignment
# Add these methods to class Account - deposit, withdraw.
#Create two instances of account and verify they work as expected.
    def deposit(self,new_amount):
        amount+=new_amount
        return (f"Hello Naima Salim, you have deposited {self.amount} in your account {self.Account_Name} and your balance is {self.amount}")
    
    def withdraw(self,new_amount):
        amount-=new_amount
        return (f"Hello Naima Salim, you have withdrawn {self.amount} in your account {self.Account_Name} and your balance is {self.amount}")
