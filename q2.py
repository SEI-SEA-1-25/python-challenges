# Variables
input_string = input("Enter a string 🧵")

def reverse(s):
  result = ''
  for char in s:
    result = char + result

  return result

print(f"{input_string} in reverse 🐈‍⬛ : {reverse(input_string)}")