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
        print(numberOne + numberTwo)
    elif subtract:
        print(numberOne - numberTwo)
    elif multiply:
        print(numberOne - numberTwo)
    elif divide:
        print(numberOne / numberTwo)
    else:
        print('Enter a number')



