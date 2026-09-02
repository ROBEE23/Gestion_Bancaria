import json
import os
import random

FILE_NAME = "bank.json"

class Account:
    def __init__(self, owner, account_number, balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def to_dict(self):
        return {
            "owner": self.owner,
            "account_number": self.account_number,
            "balance": self.balance
        }

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    for acc_num, acc_info in data.items():
                        self.accounts[acc_num] = Account(
                            acc_info["owner"], acc_num, acc_info["balance"]
                        )
                except json.JSONDecodeError:
                    self.accounts = {}

    def save_data(self):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, f, indent=4)

    def create_account(self, owner):
        acc_num = str(random.randint(10000, 99999))
        while acc_num in self.accounts:
            acc_num = str(random.randint(10000, 99999))
        
        new_acc = Account(owner, acc_num)
        self.accounts[acc_num] = new_acc
        self.save_data()
        return acc_num

    def get_account(self, acc_num):
        return self.accounts.get(acc_num)

    def transfer(self, sender_num, receiver_num, amount):
        sender = self.get_account(sender_num)
        receiver = self.get_account(receiver_num)
        
        if sender and receiver and sender.withdraw(amount):
            receiver.deposit(amount)
            self.save_data()
            return True
        return False

def main():
    bank = BankSystem()
    while True:
        print("\n=== SISTEMA BANCARIO ===")
        print("1. Crear Cuenta")
        print("2. Consultar Saldo")
        print("3. Depositar")
        print("4. Retirar")
        print("5. Transferir")
        print("6. Salir")
        
        choice = input("Selecciona una opción (1-6): ").strip()

        if choice == "1":
            name = input("Nombre del titular: ").strip()
            if name:
                acc_num = bank.create_account(name)
                print(f"[✓] Cuenta creada exitosamente. Tu número de cuenta es: {acc_num}")
        
        elif choice == "2":
            acc_num = input("Número de cuenta: ").strip()
            acc = bank.get_account(acc_num)
            if acc:
                print(f"\nTitular: {acc.owner} | Saldo actual: ${acc.balance:.2f}")
            else:
                print("[!] Cuenta no encontrada.")

        elif choice == "3":
            acc_num = input("Número de cuenta: ").strip()
            acc = bank.get_account(acc_num)
            if acc:
                try:
                    amount = float(input("Monto a depositar: "))
                    if acc.deposit(amount):
                        bank.save_data()
                        print(f"[✓] Depósito realizado. Nuevo saldo: ${acc.balance:.2f}")
                    else:
                        print("[!] El monto debe ser mayor a 0.")
                except ValueError:
                    print("[!] Monto inválido.")
            else:
                print("[!] Cuenta no encontrada.")

        elif choice == "4":
            acc_num = input("Número de cuenta: ").strip()
            acc = bank.get_account(acc_num)
            if acc:
                try:
                    amount = float(input("Monto a retirar: "))
                    if acc.withdraw(amount):
                        bank.save_data()
                        print(f"[✓] Retiro realizado. Nuevo saldo: ${acc.balance:.2f}")
                    else:
                        print("[!] Fondos insuficientes o monto inválido.")
                except ValueError:
                    print("[!] Monto inválido.")
            else:
                print("[!] Cuenta no encontrada.")

        elif choice == "5":
            sender_num = input("Tu número de cuenta: ").strip()
            receiver_num = input("Número de cuenta destino: ").strip()
            try:
                amount = float(input("Monto a transferir: "))
                if bank.transfer(sender_num, receiver_num, amount):
                    print("[✓] Transferencia realizada con éxito.")
                else:
                    print("[!] Fallo en la transferencia. Verifica las cuentas y los fondos.")
            except ValueError:
                print("[!] Monto inválido.")

        elif choice == "6":
            print("\nGracias por usar el sistema bancario.")
            break
        else:
            print("[!] Opción no válida.")

if __name__ == "__main__":
    main()
