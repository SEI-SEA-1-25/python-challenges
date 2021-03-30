balance = 50000000
print("💲 Welcome to Gringott's Bank 💲")

def deposit():
  return float(input("Deposit amount?"))

def withdraw():
  return float(input("Withdraw amount?"))

def print_balance():
  print(f"Balance is: {balance}")

print_balance()
is_finished = "no"

while is_finished != "yes":
  command = input("Deposit, withdraw, or balance?")
  if command == "deposit":
    balance += deposit()
  elif command == "withdraw":
    balance -= withdraw()

  print_balance()
  is_finished = input("Are you finished?")

print("Have a nice day!")