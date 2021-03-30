# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("Please select an operation:")
print(operation  + "has been selected")

n1 = int(input("Enter a number:"))
n2 = int(input("Enter another number:"))



if(operation == "addition"):
    print("You result is " + str(n1+n2))

elif(operation == "subtraction"):
    print("You result is " + str(n1-n2))

elif(operation == "multiplication"):
    print("You result is " + str(n1*n2))

elif(operation == "division"):
    print("You result is " + str(n1/n2))

else:
    print("please do it again with a valied operaror")