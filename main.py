from bank_account import BankAccount

print("Welcome to the Bank of Brinlee!")
customer_name = input("Please enter your name: ")

account = BankAccount(customer_name)




def make_deposit(account):

    try:
        amount = float(input("How much would you like to deposit? $"))
    except ValueError:
        print("Please enter a valid number.")    
        return
    
    if account.deposit(amount):
        print(f"Deposited ${amount:.2f}.")
    else:
        print("Deposit must be a positive amount.")

def make_withdrawal(account):
    
    try:
        withdraw_amount = float(input("How much would you like to withdraw? $"))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    if account.withdraw(withdraw_amount):
        print(f"Withdrew ${withdraw_amount:.2f}.")
    else:
        print("Withdrawal failed. Enter a positive amount that does not exceed your balance.")

def view_account_info(account):
    print(f"Name: {account.customer_name}")
    print(f"Account #: {account.account_number}")
    print(f"Balance: ${account.balance:.2f}")


running = True

while running:
   
    print("--------------------------------")
    print("Please choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")
    print("--------------------------------")
    
    choice = input()

    if choice == "1":
        make_deposit(account)
    elif choice == "2":
        make_withdrawal(account)
    elif choice == "3":
        view_account_info(account)
    elif choice == "4":
        print("Thank you for your business!")
        running = False
    else:
        print("Invalid choice. Please try again.")