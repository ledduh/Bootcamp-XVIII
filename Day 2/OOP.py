class BankAccount(object): 

    def __init__(self):
        pass

    def withdraw():
        pass
    def deposit():
        pass

class SavingsAccount(BankAccount):#class SavingsAccount inherits from BankAccount

    def __init__(self): #Balance is established first
        self.balance = 500

    def deposit(self, amount): 
        if (amount < 0): #if the amount being deposited is less than 0 it gives a return of invalid deposit amount
            return "Invalid deposit amount"
        else:
            self.balance += amount #if the deposited amount is above 0 it should return the balance 
            return self.balance

    def withdraw(self, amount):
        if ((self.balance - amount) > 0) and ((self.balance - amount) < 500):
            return "Cannot withdraw beyond the minimum account balance" #if the amount in the account is greater than 0 and less than 500 it should return Cannot withdraw beyond the minimum account balance
        elif (self.balance - amount) < 0: #if amount is less than 0 it returns Cannot withdraw beyond the current account balance
            return "Cannot withdraw beyond the current account balance"
        elif amount < 0: #if the amount in the account is less than o it returns Invalid withdraw amount
            return "Invalid withdraw amount"
        else:
            self.balance -= amount
            return self.balance #the balance is returned after a withdrawal is made

class CurrentAccount(BankAccount):

    def __init__(self):
        self.balance = 0 #current account has 0 amount 


    def deposit(self, amount):
        if amount < 0: #if the amount being deposited is less than 0 it gives a return of invalid deposit amount
            return "Invalid deposit amount"
        else:
            self.balance += amount #if the deposited amount is above 0 it should return the balance
            return self.balance


    def withdraw(self, amount):
        if amount < 0: #if the amount in the account is less than o it returns Invalid withdraw amount
            return "Invalid withdraw amount"
        elif self.balance < amount:
            return "Cannot withdraw beyond the current account balance" #if the balance is less than the amount which is to be withdrawn it returns Cannot withdraw beyond the current account balance
        else:
            self.balance -= amount
            return self.balance #the balance is returned after a withdrawal is made
