"""
This file demonstrates:
- Using **kwargs
- Passing keyword arguments
"""

# Function using **kwargs
def display_user(**user):
    """Display user information."""

    for key, value in user.items():
        print(f"{key}: {value}")


print("=== Using **kwargs ===")

display_user(
    first_name="John",
    last_name="Smith",
    age=25
)

print("\n=== Automation Example ===")


def browser_settings(**settings):
    """Display browser configuration."""

    for key, value in settings.items():
        print(f"{key}: {value}")


browser_settings(
    browser="Chrome",
    headless=True,
    timeout=30
)