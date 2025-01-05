# Banking program

balance = 0
is_running = True

def show_balance(balance):
    print(f"your balance is ${balance:.2f}")

def deposit():

    amount = float(input("Enter your amount to be deposited: "))
    if amount < 0:
        print("this is not a valid amount")
        return 0
    else:
        return amount

def withdrawl(balance):

    amount = float(input("Enter your amount to be deposited: "))
    if amount > balance:
        print("your balance is insufficent")
        return 0
    else:
        return amount
    

while is_running:
    print("Welcome to Banking Program")
    print("1.Show_Balance")
    print("2.Deposit")
    print("3.Withdrawl")
    print("e.Exit")

    choice = ("Enter your input from(1-4): \n")

    if choice == "1": 
        show_balance(balance)
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdrawl(balance)
    elif choice == "4":
        is_running = False
    else: 
        print("Not a valid choice")

print("Thank you! Have a nice day")
    