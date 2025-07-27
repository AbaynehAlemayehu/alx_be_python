# fns_and_dsa/arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Args:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: The result, or an error message for invalid input / division by zero.
    """
    operation = str(operation).strip().lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
