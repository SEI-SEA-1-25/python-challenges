print("Welcome to Chase bank.")


# todo ## PRINT BALANCE
def print_balance():
    print(f"your balance is?\n")

# todo ## ASK WHAT THEY WANT


def deposit():
    user_input = input("How much to put in?\n")
    return int(user_input)


def withdraw():
    user_input = ("how much to take out?")
    return int(user_input)
# todo ## DO THAT


def print_balance():


print(f"Your balance is:\n{balance} ")


def deposit():

    user_input = input("How much would you like to deposit?\n")

    return int(user_input)


def withdraw():
    # todo ## ASK IF DONE. IF NO, REPEAT STEPS


user_input = input("How much would you like to withdraw? \n")
return int(user_input)
keep_going = "y"
print_balance()
while keep_going == "y":
command = input("\nWhat would you like to do? (deposit, withdraw, balance)\n")
print_balance()
if command == "deposit":
balance += deposit()
elif command == "withdraw":
balance -= withdraw()
keep_going = input("Do you want to do another operation? (y/n)")
