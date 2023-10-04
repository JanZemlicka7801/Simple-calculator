# Function add
def add(x, y):
    return x + y

# Function subtract
def subtract(x, y):
    return x - y

# Function multiply
def multiply(x, y):
    return x * y

# Function divide
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Main for calculations
def calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator: ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                print("Result: ", add(num1, num2))
            elif operator == '-':
                print("Result: ", subtract(num1, num2))
            elif operator == '*':
                print("Result: ", multiply(num1, num2))
            elif operator == '/':
                print("Result: ", divide(num1, num2))
            else:
                print("Invalid operator! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except Exception as e:
            print("An error occurred:", str(e))
        
        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the program
calculator()
