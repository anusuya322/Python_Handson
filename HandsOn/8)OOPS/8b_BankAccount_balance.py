class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,dep_amount):
        self.__balance+=dep_amount
        #return self.__balance
    def withdraw(self,withdraw_amt):
        self.__balance-=withdraw_amt
        #return self.__balance
    def get_balance(self):
        return self.__balance

amt=int(input("Enter the amount:"))
obj=BankAccount(amt)
credit=int(input("Enter the amount to deposit:"))
obj.deposit(credit)
debit=int(input("Enter the amount to withdraw:"))
obj.withdraw(debit)
print("Balance amount:",obj.get_balance())

