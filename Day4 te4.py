"""Create a custom exception class named "ValueOutOfRangeError". Write a program that takes a number as input and checks if it's within a specific range. Use a try-except block to catch the custom exception and display a relevant error message."""
class ValueOutOfRangeError(Exception):
    def __init__(self, value, min_value, max_value):
        message = f"Value {value} is outside the range [{min_value}, {max_value}]."
        super().__init__(message)

def get_number(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if value < min_value or value > max_value:
                raise ValueOutOfRangeError(value, min_value, max_value)
            return value
        except ValueOutOfRangeError as e:
            print(e)
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def main():
    min_value = 1
    max_value = 100
    prompt = f"Enter a number between {min_value} and {max_value}: "
    value = get_number(prompt, min_value, max_value)
    print("Number is within the range.")

if __name__ == "__main__":
    main()
