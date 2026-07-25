"""
This file demonstrates:
- Using *args and **kwargs together
"""

def create_user(*roles, **details):
    """
    Display user roles and details.
    """

    print("Roles:")

    for role in roles:
        print("-", role)

    print("\nUser Details:")

    for key, value in details.items():
        print(f"{key}: {value}")


print("=== *args and **kwargs ===")

create_user(
    "Admin",
    "Tester",
    first_name="John",
    last_name="Smith",
    country="United Kingdom"
)

