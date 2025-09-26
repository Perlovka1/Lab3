class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Пополнение: +{amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Снятие: -{amount}")
            return True
        return False
    
    @property
    def balance(self):
        return self._balance
    
    def get_transactions(self):
        return self._transactions

# Пример использования
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)

print(f"Баланс: {account.balance}")
print("История операций:")
for transaction in account.get_transactions():
    print(transaction)