balance = 0
done = False

def finish():
    end_state = input('Are you done?\n')
    if end_state == 'yes':
        global done
        done = True
        print('Thank you!')
    else 


def deposit(amount):
    global balance
    balance += amount
    print(f'Your current balance is ${balance}!\n ')
    finish()

def withdraw(amount):
    global balance
    amount = round(amount, 2)
    balance -= amount
    print(f'Your current balance is \n{balance} ')
    finish()


def check_balance():
    print(f'Your current balance is \n${balance}')
    finish()

print("Welcome to Chase bank.\n")

while not done:
    task = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    if task == 'check_balance':
        check_balance()
    elif task == 'deposit':
        amount = float(input('How much would you like to deposit?\n'))
        deposit(amount)
    elif task == 'withdraw':
        amount = float(input('How much would you like to withdraw?\n'))
        withdraw(amount)

print("Have a nice day!")

