# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

prompt = '>'

print('What calculation would you like to do? (add, sub, mult, div)')
calc = input(prompt)
if calc in ['add', 'sub', 'mult', 'div']:
  print('What is number 1?')
  num1 = input(prompt)
  num1 = int(num1)
  print('What is number 2?')
  num2 = input(prompt)
  num2 = int(num2)
else:
    print('that operation is not a valid choice')

def calculation():
  if calc == 'add':
    print(num1 + num2)
  elif calc == 'sub':
    print(num1 - num2)
  elif calc == 'mult':
    print(num1 * num2)
  elif calc == 'div':
    print(num1 / num2)

calculation()