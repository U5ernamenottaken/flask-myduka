class BankAccount:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_name = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened
    def withdraw(self):
        self.amount = int(input('Enter amount to withdraw: '))
        return self.balance-self.amount

    def deposit(self):
        self.amount = int(input('Enter amount to deposit: '))
        return self.balance+self.amount
    def display_info(self):
        return self.balance

account_1 = BankAccount(1234,4000,'Jane',2020-12-12)
account_2 = BankAccount(5467,5000,'Mary',2021-10-23)
# print(account_1.withdraw())
# print(account_1.deposit())
print(account_1.display_info())


