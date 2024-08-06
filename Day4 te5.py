"""Simulate a scenario where you have a function that performs an operation and might raise an exception.  Write another function that calls the first function and wraps it in a try-except block. In the outer try-except, handle a different type of exception that might occur during the function call. This demonstrates handling exceptions at different levels in your code."""
def perform_operation(x, y):
    return x / y

def call_operation(x, y):
    try:
        result = perform_operation(x, y)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def main():
       try:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        result = call_operation(x, y)
        if result is not None:
            print(f"The result is: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
