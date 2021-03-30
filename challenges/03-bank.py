print("Welcome to Chase bank.")

balance = 4000
done = 'no'

def bank():
    global balance
    global done

    while (done == 'no'):
        operation = input('What would you like to do? (deposit, withdraw, check_balance)')
    
        if (operation == 'deposit'):
            q_dep = int(input('How much would you like to deposit?'))
            balance = q_dep + balance
            print(f'Your current balance is {balance}')
            are_done = input('Are you done? (yes, no)')
        elif (operation == 'withdraw'):
            q_withdr = int(input('How much would you like to withdraw?'))
            balance = balance - q_withdr
            print(f'Your current balance is {balance}')
            are_done = input('Are you done? (yes, no)')
        elif (operation == 'check_balance'):
            print(f'Your current balance is {balance}')
            are_done = input('Are you done? (yes, no)')

        if (are_done == 'yes'):
            print('Thank you! Have a nice day!')

bank()
