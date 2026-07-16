# task OOP Task 1.Create a class called BankAccount with the following attributes:
#  -account number -balance -owner name -date opened 
# 2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() -display_info()
#  3.Create two BankAccount objects that can deposit, withdraw and display_info
from datetime import datetime
today = datetime.today()
class BankAccount:
    def __init__(self,account_number,balance,owner_name,date_opened=today):
        self.account_name = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened
    def withdraw(self):
        amount = int(input('Enter amount to withdraw: '))
        self.balance = self.balance-amount
        return self.balance

    def deposit(self):
        amount = int(input('Enter amount to deposit: '))
        self.balance = self.balance + amount
        return self.balance
    def display_info(self):
        return self.balance

account_1 = BankAccount(1234,4000,'Jane')
account_2 = BankAccount(5467,5000,'Mary')
print(account_2.withdraw())
print(account_2.deposit())
print(account_2.display_info())


