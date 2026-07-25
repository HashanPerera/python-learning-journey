"""
This file demonstrates:
- Using *args
- Passing multiple positional arguments
"""

# Function using *args
def add_numbers(*numbers):
    """Return the sum of all numbers."""
    total = 0

    for number in numbers:
        total += number

    return total


print("=== Using *args ===")

print(add_numbers(10, 20))
print(add_numbers(5, 10, 15))
print(add_numbers(1, 2, 3, 4, 5))

print("\n=== Iterating Through *args ===")


def print_names(*names):
    """Print all names."""

    for name in names:
        print(name)


print_names("John", "Nathan", "Emily")
