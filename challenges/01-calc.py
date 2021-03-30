# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
 

def calculationFunct():
    method = input('what calculation would you like to do? (add, sub, mult, div)')
    number1 = int(input('What is the first number?'))
    number2 = int(input('What is the second number?'))
    msg = 'method is not valid, please try again 😇'

    if method == 'add':
        res = number1 + number2
    elif method == 'sub':
        res = number1 - number2
    elif method == 'mult':
        res = number1 * number2
    elif method == 'div':
        res = number1 / number2
    else:
        print(msg)
    return res
    # print(res)

result = calculationFunct()
print('Result is', result)