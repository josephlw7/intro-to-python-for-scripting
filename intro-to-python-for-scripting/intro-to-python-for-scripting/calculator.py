def calculator():
    """"
    A calculator program that takes two number and an operator
    from the user and performs the calculation.
    """
    try:
        num1 =float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /):")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num1 == 0:
                print("Error: Cannot divideby zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

calculator()

        