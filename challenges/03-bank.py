print("Welcome to Chase bank. We suck!")

balance = 4000

# print out their balance
# ask them what they want to do
# do that thing
# as long as they don't say they're done...
# ... keep asking and doing

def print_balance():
  print(f"Your balance is:\n{balance}")

def deposit():
  user_input = input("How much would you like to deposit?\n")

  return int(user_input)
def withdrawal():
  user_input = input("How much would you like to withdrawal?\n")

  return int(user_input)

keep_going = "y"

print_balance()

while keep_going == "y":
  command = input("\nWhat would you like to do? (deposit, withdrawal, balance)\n")
  if command == "deposit":
    balance += deposit()
  elif command == "withdrawal":
    balance -= withdrawal()
  
  print_balance()
  keep_going = input(f"Do you want another transaction? (y/n)")

print("Have a nice day!")