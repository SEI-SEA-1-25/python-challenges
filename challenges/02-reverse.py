# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# def reverse_string():
#     inputsomething = input("what message would you like to reverse?")
#     x = ''
#     for letter in inputsomething:
#         x = letter + x
#     print(x)

# reverse_string()

# colin's code along
user_input = input("what message would you like to reverse?")
def reverse(s):
    result = ''
    for letter in s:
        result = letter + result

    return result
print(f'{user_input} reversed is: {reverse(user_input)}')