"""
This file has the operations menu, taking input and returning result

"""
import calculator

# This defines a dictionary of all the operations functions, Here the functions are objects 
# the functions are referenced by their names without parentheses and arguments. 
# This means you're storing a reference to the function itself, not calling the function.
# To call the functions, we can do:
# operations[choice][0](num1, num2)
# This will pass num1 and num2 to the function we called
# [0] part ensures we select the first value in the tuple (function) as tuple has 2 values, function and its decription
operations = {
    "1" : (calculator.addition, "Addition"),
    "2" : (calculator.subtract, "Subtraction"),
    "3" : (calculator.multiply, "Multiplication"),
    "4" : (calculator.divide, "Divide"),
    "5" : (calculator.int_divide, "Integer Divide"),
    "6" : (calculator.power, "Exponent")
}

def get_operation():
    """
    Gets the operation choice from the user
    """

    print("We support following operations:")

    for key, (function, description) in operations.items():
        print(f"{key}. {description}")

    while True:
        operation = input("Please enter the serial number (1 to 6) for the operation you want to perform: ")
        if operation in operations:
            print("Selected operation is: ", operations[operation][1])
            return operation
        else:
            print("Invalid choice, please enter a number (1 to 6) only! ")

def get_numbers():
    """
    Gets the input numbers from the user, on which to perform calculations
    """

    while True:
        try:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid values, please enter numbers")

def main():
    """
    Main program, here the execution starts
    """
    print("Welcome to Calculator CLI!")
    continue_calculation = True         # Flag to check if the user wants to exit or continue the calculation

    while continue_calculation:
        operation = get_operation()
        operation_func = operations[operation][0]
        num1, num2 = get_numbers()
        result = operation_func(num1, num2)
        print("The result of your operation is:", result)

        # Following if the user wants to exit or continue the calculation
        another_calculation = input("Do you want to do another calculation? Enter \"yes\" or \"no\": ").lower()

        if another_calculation == "no":
            continue_calculation = False           # End the loop and exit the program
        elif another_calculation != "yes":
            print("Incorrect value entered. Please enter \"yes\" or \"no\" only")
            continue_calculation = True
            continue                               # Again execute the loop to get correct input 
    
    print("Thanks for using Calculator CLI!")

if __name__ == "__main__":
    main()
