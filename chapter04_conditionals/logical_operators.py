"""
This file demonstrates:Logical Operators
- and
- or
- not
"""

print("=== AND ===")

age = 25
has_license = True

if age >= 18 and has_license:
    print("Allowed to drive.")

print("\n=== OR ===")

is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access Granted")

print("\n=== NOT ===")

logged_in = False

if not logged_in:
    print("Please log in.")

