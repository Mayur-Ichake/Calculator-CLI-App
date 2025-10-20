# calculator.py
#  Hints/Mini Guide:
#  1.Use functions for each operation (+, -, *, /)
#  2.Take user input using input()
#  3.Loop until user chooses to exit

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:                    #if b is not equal to 0
        return a / b
    else:
        return "Error! Division by zero."

# Main calculator loop
def calculator():
    while True:
        # Display menu
        print("\n--- Simple Calculator CLI App---")
        print("Select operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        # user choice input
        choice = input("Enter choice (1/2/3/4/5): ")

        # Exit condition
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        # Check valid choice
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter First number: "))
                num2 = float(input("Enter Second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation (1-5).")

# Run the calculator
if __name__ == "__main__":
    calculator()
