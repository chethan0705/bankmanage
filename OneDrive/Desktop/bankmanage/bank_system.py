
class bank():
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

   

class account(bank):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
            print("Balance:", self.balance)
        else:
            print("Invalid amount")

bank_console = None


while True:
    print("\n1. Create account")
    print("2. Deposit")
    print("3. Display balance")
    print("4. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        name = input("Enter name:")
        account_no = input("Enter account no:")
        ph_no = int(input("Enter phone no:"))

        bank_console = account(name, account_no, 0)
        

    elif choice == 2:
        if bank_console is not None:
            amount = int(input("Enter amount to deposit:"))
            bank_console.deposit(amount)
        else:
            print("Please create an account first")

    elif choice == 3:
        if bank_console is not None:
            bank_console.display()
        else:
            print("Please create an account first")

    elif choice == 4:
        print("Completed")
        break

    else:
        print("Invalid choice")
