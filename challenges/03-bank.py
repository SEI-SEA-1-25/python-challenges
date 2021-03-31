print("Welcome to Chase bank.")
balance = 400
# print out their balance
# ask them what they want to do
# do that thinkg
# as long as they don't say they're done...
# keep asking and doing

def print_balance():
    print(f"Your balance is:\n{balance}")


def deposit():
    user_input = input("How much would you like to deposit?\n")

    return int(user_input)


def withdraw():
    user_input = input("How much would you like to withdraw?\n")

    return int(user_input)



keep_going = "y"

print_balance()

while keep_going == "y":
    command = input("\nWhat would you like to do?\n(deposit, withdraw, balance?)")

    if command == "deposit":
        balance += deposit()
    elif command == "withdraw":
        balance -= withdraw()

    print_balance()

    keep_going = input("Do you want to do another operation? (y/n)") # keep going gets updated each time

    print("Have a nice day!")

print_balance()