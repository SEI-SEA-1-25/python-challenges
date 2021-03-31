# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1


# Note: in python people use s instead of str for string
# started off calling the function 'copy'
user_input = input("What string do you want to reverse?")

def reverse(s):
    result = ''
    for letter in s:
        result = letter + result   #tacking on to left instead of right
    return result

print(f"{user_input} reversed is: {reverse(user_input)}")
