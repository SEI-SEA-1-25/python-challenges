print("Welcome to Chase bank.")
#print balance
#ask what they want to do
# do that thing
#as long as they don't say they are done
#keep asking and going
balance = 4000
def print_balance():
    print(f'your balance is: {balance}')
print_balance()

def deposit():
    user_input = input('how much would you like to deposit?')
    return int(user_input)
def withdraw():
    user_input = input('how much would you like to withdraw?')
    return int(user_input)
# print_balance()
# deposit()
# withdraw()

keep_going = 'y'

while keep_going == 'y':
    command = input('what would you like to do? (deposit, withdraw or balance)')
    
    if command == 'deposit':
        balance += deposit()
    elif command == 'withdraw':
        balance -= withdraw()
    print_balance()
    keep_going = input('do you want to do another transaction (y/n)')
print_balance()
print("Have a nice day!")