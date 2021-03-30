string = input("Enter a string: ")
characters = list(string)
characters.sort()
result = ''.join(characters)

print(f"A: {result}")