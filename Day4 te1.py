"""Write a program that asks the user for their age. Use a try-except block to handle the case where the user enters a non-numeric value. If an error occurs, display a message asking for a valid number."""
def get_user_age():
    """Asks the user for their age and returns the input as an integer."""
    while True:
        try:
            age = int(input("Please enter your age: "))
            return age
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Runs the age input program."""
    user_age = get_user_age()
    print(f"Your age is: {user_age}")

if __name__ == "__main__":
    main()
