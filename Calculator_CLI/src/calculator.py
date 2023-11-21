"""
This file has all the functions of calculator defined here.

"""

def addition(num1: float, num2:float) -> float:
    """Adds two numbers"""
    return num1 + num2

def subtract(num1: float, num2:float) -> float:
    """Subtracts the second number from the first number"""
    return num1 - num2

def multiply(num1: float, num2:float) -> float:
    """Multiplies the two numbers"""
    return num1 * num2

def divide(num1: float, num2: float) -> float:
    """Divides the first number by second number, float division
    Raises ZeroDivisionError for division by zero"""
    if num2 != 0:
        return num1 / num2
    else:
        raise ZeroDivisionError("Can't divide by zero")
    
def int_divide(num1: float, num2: float) -> float:
    """Divides the first number by second number, integer division.
    Raises ZeroDivisionError for division by zero"""
    if num2 != 0:
        return num1 // num2
    else:
        raise ZeroDivisionError("Can't divide by zero")

def power(num1: float, num2: float) -> float:
    """Returns the exponent result of first number raised to the power of second number"""
    return num1 ** num2

