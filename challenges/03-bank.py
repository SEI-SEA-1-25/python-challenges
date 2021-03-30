print("Welcome to Chase bank.")

starting_balance = 4000
print(f"Your current balance is {starting_balance}")




loop_condition = True
while(loop_condition):
    action = input("What would you like to do? (deposit, withdraw, check_balance)")
    if(action =="deposit"):
        value = input("How much would you like to deposit?")
        starting_balance += int(value)
        print("Your current balance is "+ str(starting_balance))        
    elif(action =="withdraw"):
        value = input("How much would you like to deposit?")
        starting_balance -= int(value)
        print("Your current balance is "+ str(starting_balance))  
    elif(action =="check_balance"):
        print("Your current balance is "+ str(starting_balance))  
    else:
        print("that is not an option")
    
    done_condition = input("Are you done?")

    if(done_condition in ["yes","y", "Yes", "Y","YES"]):
        loop_condition = False


print("Have a nice day!")

