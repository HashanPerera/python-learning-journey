"""
This file demonstrates:
- Nested if statements
"""

age = 22
has_ticket = True

if age >= 18:
    print("Adult")

    if has_ticket:
        print("Entry Allowed")
    else:
        print("Ticket Required")
else:
    print("Entry Denied")

print("\n=== Nested Example ===")

username = "admin"
password = "password123"

if username == "admin":

    if password == "password123":
        print("Login Successful")
    else:
        print("Incorrect Password")

else:
    print("Unknown User")

