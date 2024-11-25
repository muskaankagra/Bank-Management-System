# class BankAccount:
#     def __init__(self, account_number, name, balance=0):
#         self.account_number = account_number
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")
#         else:
#             print("Insufficient balance or invalid withdrawal amount.")

#     def check_balance(self):
#         print(f"Current balance: ₹{self.balance}")


# class BankManagementSystem:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self):
#         account_number = input("Enter account number: ")
#         if account_number in self.accounts:
#             print("Account number already exists.")
#             return
#         name = input("Enter account holder's name: ")
#         initial_balance = float(input("Enter initial deposit amount: "))
#         self.accounts[account_number] = BankAccount(account_number, name, initial_balance)
#         print(f"Account for {name} created successfully with balance ₹{initial_balance}.")

#     def access_account(self):
#         account_number = input("Enter account number: ")
#         if account_number not in self.accounts:
#             print("Account not found.")
#             return

#         account = self.accounts[account_number]
#         print(f"Welcome, {account.name}!")
#         while True:
#             print("\n1. Deposit")
#             print("2. Withdraw")
#             print("3. Check Balance")
#             print("4. Exit")
#             choice = input("Select an option: ")

#             if choice == "1":
#                 amount = float(input("Enter deposit amount: "))
#                 account.deposit(amount)
#             elif choice == "2":
#                 amount = float(input("Enter withdrawal amount: "))
#                 account.withdraw(amount)
#             elif choice == "3":
#                 account.check_balance()
#             elif choice == "4":
#                 print("Thank you for using the bank management system!")
#                 break
#             else:
#                 print("Invalid option. Please try again.")

#     def main_menu(self):
#         while True:
#             print("\n1. Create Account")
#             print("2. Access Account")
#             print("3. Exit")
#             choice = input("Select an option: ")

#             if choice == "1":
#                 self.create_account()
#             elif choice == "2":
#                 self.access_account()
#             elif choice == "3":
#                 print("Exiting the system. Goodbye!")
#                 break
#             else:
#                 print("Invalid option. Please try again.")


# if __name__ == "__main__":
#     system = BankManagementSystem()
#     system.main_menu()
