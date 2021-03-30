# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = 'supercalifragilisticexpialidocious'
new_list = list(string)
# print(dir(string))
new_list = sorted(new_list)

new_string = ''.join(new_list)

print(new_string)
