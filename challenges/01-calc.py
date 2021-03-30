# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc():
    cal_input = input("What calculation would you like to do? (add, sub, mult, div)")
    num_1 = input("enter first number")
    num_2 = input("enter second number")
    message = "that calculation is not available, please try again"
    if cal_input == 'add':
        response = int(num_1) + int(num_2)
        print(f"The result is {response}")
    elif cal_input == 'sub':
        response = int(num_1) - int(num_2)
        print(f"The result is {response}")
    elif cal_input == 'mult':
        response = int(num_1) * int(num_2)
        print(f"The result is {response}")
    elif cal_input == 'div':
        response = int(num_1) / int(num_2)
        print(f"The result is {response}")
    else:
        print(message)
        
calc()
