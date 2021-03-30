print("Welcome to Chase bank.")
print("Have a nice day!")
def dep_function():
  print('How much would you like to deposit?')
  dep = input(prompt)
  dep = int(dep)
  new_balance = current_balance + dep
  return new_balance

def draw_function():
  print('How much would you like to withdraw?')
  draw = input(prompt)
  draw = int(draw)
  new_balance = current_balance - draw
  return new_balance

prompt = '>'
current_balance = 4000
new_balance = 0

print(f'Your current balance is {current_balance}')
print('What would you like to do? (deposit, withdraw, check_balance)')
task = input(prompt)
if task in ['deposit', 'withdraw', 'check_balance']:
  pass
else:
  print('Not a valid option')
if task == 'deposit':
  dep_function()
elif task == 'withdraw':
  draw_function()
elif task == 'check_balance':
  pass
print(f'Your current balance is {current_balance}')
