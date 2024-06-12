def results():
  num_one = float(input("What's number 1?"))
  num_two = float(input("What's number 2?"))

  return (num_one, num_two)

operation = input("+, -, / or *?\n 🧮 : ")


# add
if operation == "+":
  num_one, num_two = results()
  result = round(num_one + num_two, 2)
  print(f"Your result is {result}")
#else if sub
elif operation == "-":
  num_one, num_two = results()
  result = round(num_one - num_two, 2)
  print(f"Your result is {result}")
#else if multi
elif operation == "*":
  num_one, num_two = results()
  result = round(num_one * num_two, 2)
  print(f"Your result is {result}")
#else if divide
elif operation == "/":
  num_one, num_two = results()
  result = round(num_one / num_two, 2)
  print(f"Your result is {result}")
#catch
else:
  print("🤯 No go")