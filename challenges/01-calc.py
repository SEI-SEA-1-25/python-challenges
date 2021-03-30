# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Challenge 1 - Calculator
# Create a simple calculator that first asks the user what method they would like to use 
# (addition, subtraction, multiplication, division) and then asks the user for two numbers, 
# returning the result of the method with the two numbers. Here is a sample prompt:

# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

# Bonus: tell the user if the operation they entered isn't one of the valid choices.
prompt = ">"

choice = ["add", "sub", "mult", "div"]

print ("What calculation would you like to do? (add, sub, mult, div)")
options = input(prompt)
print (options)

# number = int(number)
def calculator(num1, num2):
    if options == "add":
        return num1 + num2
    elif options == "sub":
        return num1 - num2
    elif options == "mult":
        return num1 * num2
    else:
        return num1 / num2

if options in choice:
    print("Please enter your first number")
    first_num = input(prompt)
    first_num = int(first_num)

    print("Please enter your second number")
    second_num = input(prompt)
    second_num = int(second_num)
    print(calculator(first_num, second_num))
else:
    print("This is not the valid choices")

        

