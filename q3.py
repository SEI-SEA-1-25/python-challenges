# init balance var
balance = 50000000
print("💲 Welcome to Gringott's Bank 💲")

# if ask for deposit, enter here
def deposit():
  return float(input("Deposit amount?"))

# if ask for withdraw, enter here
def withdraw():
  return float(input("Withdraw amount?"))

# if ask for balance, tell current balance
def print_balance():
  print(f"Balance: {balance}")

# keeps loop going:
print_balance()
is_finished = "no"

# while loop. while user doesn't close loop
# ask what action they'd like
while is_finished != "yes":
  command = input("Deposit, withdraw, or balance?")
  if command == "deposit":
    balance += deposit()
  elif command == "withdraw":
    balance -= withdraw()

  print_balance()
  # input ASKS THE USER to define the what it equates to.
  is_finished = input("Are you finished?")

#goodbye message
print("Have a nice day!🍎 🍎 🍎 ")