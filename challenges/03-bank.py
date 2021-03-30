print("Welcome to Chase bank.")
print("Have a nice day!")

def print_balance():
    print(f'Your balance is: \n{balance}')

def deposit():
    user_input = input("how much would you like to deposit?")
    return int(user_input)

def withdraw():
    user_input = input('how much would you like to withdraw?')
    return int(user_input)

is_done = "no"

while is_done != "yes":
    command = input("\nwhat would you like ot do? (deposit, withdraw, balance)\n")
    print_balance()
    is_done = input("are you done?")

print_balance