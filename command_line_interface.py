import argparse

def main():
    print("Welcome to the Command-Line Calculator!")
    print("Welcome to the Command-Line Calculator!")
    print("Usage: python command_line_interface.py OPERATION NUMBERS")
    print("Example: python command_line_interface.py add 5 3 2")
    print("Supported operations: add, subtract, multiply, divide")
    print("Note: Separate each number with a space")

    try:
        parser = argparse.ArgumentParser(description='Command-Line Calculator')
        parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help='The mathematical operation to perform (add, subtract, multiply, divide)')
        parser.add_argument('numbers', nargs='+', type=float, help='The numbers to perform the operation on')

        args = parser.parse_args()
        
        result = perform_operation(args.operation, *args.numbers)
        
        print("Result:", result)
    except ValueError as e:
        print("Error:", e)
    except argparse.ArgumentError as ae:
        print("Invalid input. Please provide a valid operation and numbers.")

def perform_operation(operation, *numbers):
    if operation == 'add':
        return sum(numbers)
    elif operation == 'subtract':
        if len(numbers) < 2:
            raise ValueError("Subtraction requires at least two numbers.")
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result
    elif operation == 'multiply':
        return multiply(*numbers)
    elif operation == 'divide':
        return divide(*numbers)

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(*numbers):
    if len(numbers) < 2:
        raise ValueError("Division requires at least two numbers.")
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

if __name__ == '__main__':
    main()
