"""
This file demonstrates:
- for loops
- while loops
- range()
- break
- continue
"""

print("=== For Loop ===")

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

print("\n=== Using range() ===")

for number in range(5):
    print(number)

print("\n=== range(start, stop) ===")

for number in range(1, 6):
    print(number)

print("\n=== range(start, stop, step) ===")

for number in range(0, 11, 2):
    print(number)

print("\n=== While Loop ===")

count = 1

while count <= 5:
    print(count)
    count += 1

print("\n=== break Statement ===")

for number in range(1, 11):

    if number == 6:
        break

    print(number)

print("\n=== continue Statement ===")

for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)

print("\n=== Automation Example ===")

test_cases = [
    "Login Test",
    "Search Test",
    "Checkout Test",
    "Logout Test"
]

for test_case in test_cases:
    print(f"Running: {test_case}")

print("\n=== Retry Example (while loop) ===")

attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    print(f"Login Attempt {attempt}")
    attempt += 1

print("Maximum attempts reached.")