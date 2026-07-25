"""
This file demonstrates:
- if statement
- if...else
- if...elif...else
"""

print("=== Simple if Statement ===")

age = 20

if age >= 18:
    print("You are an adult.")

print("\n=== if...else ===")

temperature = 15

if temperature >= 20:
    print("It's a warm day.")
else:
    print("It's a cool day.")

print("\n=== if...elif...else ===")

score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
