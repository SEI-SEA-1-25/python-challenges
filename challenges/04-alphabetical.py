# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alpha():
    query = input('Give me a string to alphabetize')
    alph_list = list(query)
    alph_list.sort()

    updated = ''
    for letter in alph_list:
        updated = updated + letter
        print(updated)

alpha()