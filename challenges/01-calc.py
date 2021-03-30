# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
user_input = input('what calculation would you like to do?')
num1 = int(input('what is num one'))
num2 = int(input('what is num two'))
print(num1 / num2)

if user_input == "add":
    print(f'your result is {num1 + num2}')
elif user_input == "sub":
    print(f'your result is {num1 - num2}')
elif user_input == "mult":
    print(f'your result is {num1 * num2}')
elif user_input == "div":
    print(f'your result is {num1 / num2}')
else:
    print("error input")