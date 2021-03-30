# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
my_string = input('Give me a string to alphabetize ')
new_list = list(my_string)
new_list.sort()
alphabetized_string = ''.join(new_list)
print(alphabetized_string)