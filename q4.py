## asks user to enter a string
string = input("Enter a string: ")
##turns string entered into a list of letters
characters = list(string)
## sorts the individual letters alphabetically 
characters.sort()
## joins the letters back into a string
result = ''.join(characters)

print(f"A: {result}")