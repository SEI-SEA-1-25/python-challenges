# Challenge 3 - Bank Transactions
# Create a prompt that asks the user if they would like to display their balance, 
# withdraw or deposit. Write three methods to perform these calculations and output the result to the user.

# Gather user input using the input function. Note that input always returns user input as a string. 
# You have to manually convert it to an int or a float to make it behave like number. 
# Also, end the input prompt with a \n newline character if you want the user to type in on the next line.

# age = input("How old are you?\n")
# age = int(age)

# Here is a sample output:

# Your current balance is
# 4000
# What would you like to do? (deposit, withdraw, check_balance)
# deposit
# How much would you like to deposit?
# 1000
# Your current balance is 5000
# Are you done?
# yes
# Thank you!

user_choice = ["deposit", "withdraw", "check_balance"]
balance = 0
balance = int(balance)

age = input("How old are you?\n")
age = int(age)

# age < 18 -> return True
# else -> return false
def is_user_age_valid(age):
    # print(age)
    if age < 18:
        print("You must be 18 or older to continue Sorry\n")
        return False
    else:
        return True

returned = is_user_age_valid(age)       
if returned == True:
    options = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    if options not in user_choice:
        print("Please choose valid options")
    elif options == "deposit":
        user_deposit = input("How much would you like to deposit?\n")
        user_deposit = int(user_deposit)
        balance += user_deposit
        print(f"Your balance after deposit: {balance}")
    elif options == "withdraw":
        user_withdraw = input("How much would you like to withdraw?\n")
        user_withdraw = int(user_withdraw)
        balance -= user_withdraw
        print(f"Your balance after withdraw: {balance}")
    else:
        print(f"This is your current balance: {balance}")
