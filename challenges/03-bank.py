

balance = 1000

print("Welcome to Chase bank. Select an option")
print("Deposit")
print("Withdraw")
print("Done")

try:
    while True:

        option = input("Select an option: ")
        
        if option == "Deposit":
            option_1 = float(input("Input deposit amount: $"))
            balance += option_1
            print(f"Balance: {balance}")

        elif option == "Withdraw":
            option_2 = float(input("Input withdrawal amount: $"))
            balance -= option_2
            print(f"Balance: {balance}")

        elif option == "Done":
            exit('Have a nice day!')

except ValueError:
    print('Input a number')