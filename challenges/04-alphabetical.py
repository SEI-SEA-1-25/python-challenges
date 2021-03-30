# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.



alphabet = 'abcdefghijklmnopqrstuvwxyz'

stringToAlphabetize = input("Give me a string to alphabetize")

output = ""
for letter1 in alphabet:
    for letter2 in stringToAlphabetize:
        if(letter1 == letter2):
            output += letter1

print(output)