# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
user_input1 = input("What calculation would you like to do?")
user_input2 = input('What is number 1?')
user_input3 = input('What is number 2?')
num1 = int(user_input2)
num2 = int(user_input3)
print(num1/num2)