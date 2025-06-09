# Input two numbers and the operator from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the operation based on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    # Handle division by zero
    if num2 == 0:
        result = "Error: Division by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operator"

# Output the result
print("Result:", result)
