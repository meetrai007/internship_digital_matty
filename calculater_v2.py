def calculate(num1, operator, num2):
  """functon to take two inputs with one operator and return result after calculation"""

  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Division by zero is not allowed")
    else:
      return num1 / num2
  else:
    print("Invalid operator")

while True:
  try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, or /): ")
    num2 = float(input("Enter the second number: "))

    result = calculate(num1, operator, num2)
    print(f"{num1} {operator} {num2} = {result}")

  except ValueError as e:
    print("Invalid input. Please use numbers and valid operators.")
  except ZeroDivisionError as e:
    print("Error:", e)

  print("Do you want to perform another calculation? (y/n)")
  choice = input().lower()
  if choice != "y":
    break