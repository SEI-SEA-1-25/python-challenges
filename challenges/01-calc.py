# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


# operator functions 
#add
def add(a, b):
    return a + b

# sub
def subtract(a, b):
    return a - b

# multiply
def multiply(a, b):
    return a * b

# divide   
def divide(a, b):
    return a / b

print('Select an operation:') 
print("+")
print("-")
print("*")
print("/")

# user input
choice = input('Pick an operator:')
A = int(input('Enter first number: '))
B = int(input('Enter second number: '))

if choice == '+':
    print(A, "+", B, "=", add(A, B))
elif choice == '-':
    print(A, "-", B, "=", subtract(A, B))
elif choice == '*':
    print(A, "*", B, "=", multiply(A, B))
elif choice == '-':
    print(A, "/", B, "=", divide(A, B))