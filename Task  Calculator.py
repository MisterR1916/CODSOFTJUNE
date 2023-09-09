# Task : CALCULATOR
def calculator():
  number1 = float(input("Enter the first number: "))
  number2 = float(input("Enter the second number: "))
  operator = input("Enter the operation (+, -, *, /): ")  
  if operator == "+":
    result = number1 + number2
  elif operator == "-":
    result = number1 - number2
  elif operator == "*":
    result = number1 * number2
  elif operator == "/":
    result = number1 / number2
  else:
    print("Invalid operator.") 
  print(f"{number1} {operator} {number2} = {result}")
calculator()
