# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


string = input("let me alph some thaaangs: \n")
# letters = [
#   'a',
#   'b',
#   'c',
# ]

# letters.sort() // --> ['a','b','c']
letters = list(string)
letters.sort()
print(letters)
result = ''.join(letters)
print(result)
