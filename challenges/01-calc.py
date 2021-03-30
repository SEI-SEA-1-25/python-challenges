# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
method = input('What calculation would you like to do? (add, sub, mult, div)')
num1 = input('What is number 1?')
num1 = int(num1)
num2 = input('What is number 2?')
num2 = int(num2)

if method == 'add':
    result = num1 + num2
elif method == 'sub':
    result == num1 - num2
elif method == 'div':
    result == num1 / num2
elif method == 'mult':
    result = num1 * num2

print(f'Your result is {result}')