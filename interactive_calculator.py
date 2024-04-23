def add(*numbers):
    return sum(numbers)

def subtract(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

# Function to perform the operation based on user input
def perform_operation(operation, *numbers):
    if operation == 'add':
        return add(*numbers)
    elif operation == 'subtract':
        return subtract(*numbers)
    elif operation == 'multiply':
        return multiply(*numbers)
    elif operation == 'divide':
        return divide(*numbers)
    else:
        raise ValueError("Invalid operation. Supported operations are 'add', 'subtract', 'multiply', 'divide'.")

# Main function for the interactive calculator
def calculator():
    print("Welcome to the Interactive Calculator!")

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        operation = {
            '1': 'add',
            '2': 'subtract',
            '3': 'multiply',
            '4': 'divide'
        }.get(choice)

        if operation:
            numbers_str = input("Enter the numbers separated by spaces: ")
            numbers = [float(num) for num in numbers_str.split()]

            try:
                result = perform_operation(operation, *numbers)
                print("Result:", result)
            except ValueError as e:
                print(e)
        else:
            print("Invalid choice. Please select a number from 1 to 5.")

# Run the calculator
calculator()
