class ATM:
    def __init__(self, balance=1000, pin="1234"):
        self.balance = balance
        self.pin = pin

    def authenticate(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN! Try again.")
            return False

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self):
        amount = float(input("Enter deposit amount: ₹"))
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: ₹"))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount!")

    def menu(self):
        if not self.authenticate():
            return
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM!")
                break
            else:
                print("Invalid choice! Please try again.")

# Run the ATM system
atm = ATM()
atm.menu()
