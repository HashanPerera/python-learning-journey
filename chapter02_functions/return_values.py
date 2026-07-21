"""
return_values.py

This file demonstrates:
- Returning values from functions
- Storing returned values
- Using returned values in expressions
"""

# Return a number
def add_numbers(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2


# Return a string
def get_full_name(first_name, last_name):
    """Return a person's full name."""
    return f"{first_name} {last_name}"


# Return a boolean
def is_adult(age):
    """Return True if age is 18 or older."""
    return age >= 18


print("=== Returning Numbers ===")

result = add_numbers(10, 5)
print("Result:", result)

print("\n=== Returning Strings ===")

full_name = get_full_name("John", "Smith")
print(full_name)

print("\n=== Returning Boolean ===")

print(is_adult(20))
print(is_adult(15))

print("\n=== Automation Example ===")


def get_base_url():
    """Return the application's base URL."""
    return "https://example.com"


url = get_base_url()
print("Opening:", url)