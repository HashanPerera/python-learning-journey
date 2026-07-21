"""
scope.py

This file demonstrates:
- Global scope
- Local scope
- Variable visibility
"""

# Global variable
browser = "Chrome"


def launch_browser():
    """Access a global variable."""
    print("Launching", browser)


launch_browser()

print("\n=== Local Scope ===")


def greet():
    """Create a local variable."""
    message = "Welcome to Python!"
    print(message)


greet()

# Uncommenting the next line will raise a NameError
# print(message)

print("\n=== Global vs Local ===")

username = "Admin"


def login():
    username = "TestUser"
    print("Inside function:", username)


login()

print("Outside function:", username)

print("\n=== Automation Example ===")

base_url = "https://example.com"


def open_application():
    print(f"Opening {base_url}")


open_application()