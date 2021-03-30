# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# Create a function that takes a string and returns the string with the letters in alphabetical order 
# (ie. hello becomes ehllo), Assume numbers and punctuation symbols will not be included in the string.

# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux


get_string = input("Please enter string: ")

def random_string (value):
    one_word = sorted(value)
    print(one_word)
    join_value = ''.join(one_word)
    print(join_value)
random_string(get_string)