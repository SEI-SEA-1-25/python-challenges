# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input('what calculation woudl you like to do?')

number1 = int(input('What is number 1?'))
number2 = int(input('What is number 2?'))
print(number1 / number2)

if operation == 'add':
    print(f"Your result is {number1 + number2}")
elif operation == "sub":
    print(f"Your result is {number1 - number2}")
elif operation == "mult":
    print(f"Your result is {number1 * number2}")
elif operation == "div":
    print(f"Your result is {number1 / number2}")
else:
    print('That was not a valid operation. You can type in "add" or "sub" or "mult" or "div".')
