print("Welcome to Chase bank.")
print("Have a nice day!")
balance = 4000
# print out their balances
# ask what they want to do
# do it for
# as long as they dont say they're done...
# keep asking 

def print_balance():
    print(f"Your balance is: \n{balance}")

def deposit_balance():
    user_input = input("How much would you like to deposit? \n")
    
    return int(user_input)

def withdraw_balance():
    user_input = input("How much would you like to withdraw? \n")

    return int(user_input)

is_done = "yes"

while is_done == "yes":
    command = input("\n what would you like to do? (withdraw, deposit, balance \n")

    print_balance()

    if command == "deposit":
        balance += deposit_balance()
    elif command == "withdraw":
        balance -= withdraw_balance()

    print_balance()
    is_done = input("Do you want to continue (yes/no)")

print_balance()