"""
This file demonstrates:
- Defining functions
- Calling functions
- Parameters
- Arguments
- Return values
"""

# Function without parameters
def greet():
    """Print a welcome message."""
    print("Welcome to Python Programming!")


# Function with parameters
def greet_user(name):
    """Greet a user by name."""
    print(f"Hello, {name}!")


# Function with multiple parameters
def introduce(first_name, last_name):
    """Print a person's full name."""
    print(f"Full Name: {first_name} {last_name}")


# Function that returns a value
def add_numbers(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2


# Function that returns a string
def create_email(first_name, last_name):
    """Generate an email address."""
    return f"{first_name.lower()}.{last_name.lower()}@example.com"


# ----------------------------
# Calling the functions
# ----------------------------

print("=== Function Without Parameters ===")
greet()

print("\n=== Function With Parameters ===")
greet_user("John")
greet_user("Nathan")

print("\n=== Multiple Parameters ===")
introduce("John", "Smith")

print("\n=== Return Value ===")
result = add_numbers(15, 10)
print("Sum:", result)

print("\n=== Generate Email ===")
email = create_email("John", "Smith")
print("Email:", email)

#######################################################
print("\n=== Automation Example ===")
def launch_browser(browser):
    """Simulate launching a browser."""
    return f"Launching {browser} browser..."

message = launch_browser("Chrome")
print(message)