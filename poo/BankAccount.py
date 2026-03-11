class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount} en la cuenta de {self.account_holder}")
        else:
            print("No se puede depositar en una cuenta inactiva")

    def withdraw(self, amount):
        if self.is_active:
            if amount > self.balance:
                print("No se puede retirar una cantidad mayor al saldo")
            else:
                self.balance -= amount
                print(f"Se ha retirado {amount} de la cuenta de {self.account_holder}")
        else:
            print("No se puede retirar en una cuenta inactiva")
        
    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta de {self.account_holder} ha sido desactivada")
    
    def __str__(self):
        return f"Cuenta de {self.account_holder}:\nSaldo = {self.balance}\nEstado = {'Activa' if self.is_active else 'Inactiva'}"
    

account1 = BankAccount("Cristian", 1000)

account1.deposit(500)

account2 = BankAccount("Antonio", 2000)

account2.withdraw(1000)
account2.deactivate_account()

print(account1)
print(account2)
