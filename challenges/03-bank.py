print("Welcome to Chase bank.")
print("Have a nice day!")
balance = 4000

# print out their balance 
# ask them what they want to do
# do the thing
# as long as they don't say they are done...
# keep asking and doing

def print_balance():
    print (f"Your balaance is:\n{balance}")

def deposit():
    user_input = input("How much would you like to deposit?\n")
    return int(user_input)

def withdrawal():
    user_input = input("How much would you like to withdrawal?\n")
    return int(user_input)
keep_going = "y"

while keep_going == "y":
    command = input("\nWhat woudl you like to do?(deposit, withdraw, balance)\n")

    if command == "deposit":
        balance += deposit()
    elif command == "withdraw":
        balancae -= withdraw()
    print_balance()

    keep_going = input("Do you want to do another operation?(y/n)")
print_balance()
