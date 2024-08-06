# Define a lambda function to convert a string to uppercase
uppercase_string = lambda s: s.upper()

# Define a lambda function to remove vowels from a string
remove_vowels = lambda s: ''.join([c for c in s if c.lower() not in 'aeiou'])

# Define a lambda function to filter out odd numbers from a list
even_numbers = lambda numbers: list(filter(lambda x: x % 2 == 0, numbers))

# Import the reduce function from the functools module
from functools import reduce

# Define a lambda function to sum up all numbers in a list
sum_numbers = lambda numbers: reduce(lambda x, y: x + y, numbers)

# Define a lambda function to sort a list of strings by length
sort_strings_by_length = lambda strings: sorted(strings, key=len)

# Example usage:

# Uppercase string
print("Uppercase string:")
original_string = "hello world"
print(f"Original: {original_string}")
print(f"Uppercase: {uppercase_string(original_string)}")

# Remove vowels
print("\nRemove vowels:")
original_string = "hello world"
print(f"Original: {original_string}")
print(f"No vowels: {remove_vowels(original_string)}")

# Even numbers
print("\nEven numbers:")
numbers = [1, 2, 3, 4, 5, 6]
print(f"Original: {numbers}")
print(f"Even numbers: {even_numbers(numbers)}")

# Sum of numbers
print("\nSum of numbers:")
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
print(f"Sum: {sum_numbers(numbers)}")

# Sort strings by length
print("\nSort strings by length:")
strings = ["hello", "world", "abc", "def", "ghi"]
print(f"Original: {strings}")
print(f"Sorted: {sort_strings_by_length(strings)}")

"""
output:
Uppercase string:
Original: hello world
Uppercase: HELLO WORLD

Remove vowels:
Original: hello world
No vowels: hll wrld

Even numbers:
Original: [1, 2, 3, 4, 5, 6]
Even numbers: [2, 4, 6]

Sum of numbers:
Original: [1, 2, 3, 4, 5]
Sum: 15

Sort strings by length:
Original: ['hello', 'world', 'abc', 'def', 'ghi']
Sorted: ['abc', 'def', 'ghi', 'hello', 'world'] """
