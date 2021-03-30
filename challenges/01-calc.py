# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

todo = input('what would you like to do today - add, subtract, divide, multiply')

#Options
responseOne = input('Enter first number')
responseTwo = input('Enter second number')

# Converts to numbers
numberOne = int(responseOne)
numberTwo = int(responseTwo)



# Calc

def calculate(num1, num2):
    if add:
        print(num1 + num2)
    elif subtract:
        print(num1 - num2)
    elif multiply:
        print(num1 - num2)
    elif divide:
        print(num1 / num2)
    else:
        print('Enter a number')



