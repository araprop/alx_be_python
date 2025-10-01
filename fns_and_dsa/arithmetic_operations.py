def perform_operation(num1: float, num2: float, operation: str):
    """
    perform basic arithmetic operations between 2 numbers
    param: (float)num1, (float)num2, (str)operation
    operation: add, subtract, multiply, divide
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"