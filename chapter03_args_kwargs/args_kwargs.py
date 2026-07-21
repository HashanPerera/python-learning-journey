"""
args_kwargs.py

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

print("\n=== Automation Example ===")


def launch_browser(browser, *extensions, **settings):
    """
    Simulate launching a browser with extensions
    and settings.
    """

    print(f"Browser: {browser}")

    print("\nExtensions:")
    for extension in extensions:
        print("-", extension)

    print("\nSettings:")
    for key, value in settings.items():
        print(f"{key}: {value}")


launch_browser(
    "Chrome",
    "AdBlock",
    "Grammarly",
    headless=True,
    timeout=30,
    window_size="1920x1080"
)