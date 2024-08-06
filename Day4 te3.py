"""Write a program that calculates the area of a circle.  Use a try-except block to prevent division by zero when the user enters a zero radius. In the except block, display a message explaining the error."""


import math

def calculate_circle_area(radius):
    try:
        area = math.pi * (radius ** 2)
        return area
    except ZeroDivisionError:
        print("Error: Radius cannot be zero. Please enter a valid radius.")

def main():
    while True:
        try:
            radius = float(input("Enter the circle's radius: "))
            if radius < 0:
                print("Error: Radius cannot be negative. Please enter a valid radius.")
                continue
            area = calculate_circle_area(radius)
            print(f"The area of the circle is: {area:.2f}")
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
