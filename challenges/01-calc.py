# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("What calculation would you like to do?")
user_input2 = input("What is number 1?")
user_input3 = input("What is number 2?")
number1 = int(user_input2)
number2 = int(user_input3)
# print(number1 / number2)

if operation == "add":
  print(f"Your result is {number1 + number2}")
elif operation == "sub":
  print(f"your result is {number1 - number2}")
elif operation == "mult":
  print(f"your result is {number1 * number2}")
elif operation == "div":
  print(f"your result is {number1 / number2}")
else:
  print("That was not a valid operation. You can type in 'add' or 'sub' or 'mult' or 'div' ")