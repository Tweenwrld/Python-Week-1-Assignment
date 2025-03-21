def calculator():
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform operation based on user input
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        # Check for division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Invalid operation. Please use +, -, *, or /")

# Run the calculator
if __name__ == "__main__":
    calculator()