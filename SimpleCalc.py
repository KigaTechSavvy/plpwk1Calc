# Simple Calculator 
while True:
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /) or 'q' to quit: ")

    # Check if user wants to exit
    if operation.lower() == 'q':
        print("Exiting the calculator. Goodbye!")
        break  # Stop the loop and exit

    # Perform the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid operation! Please enter +, -, *, /, or 'q' to quit.")

    # Ask if the user wants to continue or exit
    again = input("Would you like to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break  # Exit the loop if user inputs anything other than 'yes'
