class BankAccount:
    def __init__(self, name: str, accNumber: str, balance: int):
        self.__name = name
        self.__number = accNumber
        self.__balance = balance
 
    def deposit(self, amount: float):
        self.__balance += amount
        self.__balance = self.__service_charge()
 
    def withdraw(self, amount: float):    
        self.__balance -= amount
        self.__balance = self.__service_charge()
 
    @property
    def balance(self):
        return self.__balance
 
    def __service_charge(self):
        self.__balance -= self.__balance/100
        return self.__balance
 
if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)  