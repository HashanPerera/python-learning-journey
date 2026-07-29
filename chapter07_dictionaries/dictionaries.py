"""
This file demonstrates:
- Creating dictionaries
- Accessing values
- Updating values
- Adding key-value pairs
- Removing key-value pairs
- Dictionary methods
- Looping through dictionaries
"""

# ==========================================
# CREATING A DICTIONARY
# ==========================================

print("=== CREATING A DICTIONARY ===")

student = {
    "first_name": "John",
    "last_name": "Smith",
    "age": 25,
    "country": "United Kingdom"
}

print(student)

# ==========================================
# ACCESSING VALUES
# ==========================================

print("\n=== ACCESSING VALUES ===")

print("First Name:", student["first_name"])
print("Country:", student["country"])

# Using get() (recommended)
print("Age:", student.get("age"))

# ==========================================
# UPDATING VALUES
# ==========================================

print("\n=== UPDATING VALUES ===")

student["age"] = 26

print(student)

# ==========================================
# ADDING NEW KEY-VALUE PAIRS
# ==========================================

print("\n=== ADDING VALUES ===")

student["email"] = "john.smith@example.com"

print(student)

# ==========================================
# REMOVING VALUES
# ==========================================

print("\n=== REMOVING VALUES ===")

student.pop("country")

print(student)

# ==========================================
# DICTIONARY LENGTH
# ==========================================

print("\n=== LENGTH ===")

print("Number of Items:", len(student))

# ==========================================
# KEYS
# ==========================================

print("\n=== KEYS ===")

print(student.keys())

# ==========================================
# VALUES
# ==========================================

print("\n=== VALUES ===")

print(student.values())

# ==========================================
# ITEMS
# ==========================================

print("\n=== ITEMS ===")

print(student.items())

# ==========================================
# CHECK IF KEY EXISTS
# ==========================================

print("\n=== KEY EXISTS ===")

if "email" in student:
    print("Email exists.")
else:
    print("Email not found.")

# ==========================================
# LOOP THROUGH KEYS
# ==========================================

print("\n=== LOOP THROUGH KEYS ===")

for key in student:
    print(key)

# ==========================================
# LOOP THROUGH VALUES
# ==========================================

print("\n=== LOOP THROUGH VALUES ===")

for value in student.values():
    print(value)

# ==========================================
# LOOP THROUGH KEY-VALUE PAIRS
# ==========================================

print("\n=== LOOP THROUGH ITEMS ===")

for key, value in student.items():
    print(f"{key}: {value}")

# ==========================================
# CLEAR DICTIONARY
# ==========================================

print("\n=== CLEAR ===")

colors = {
    "primary": "Red",
    "secondary": "Blue"
}

print("Before Clear:", colors)

colors.clear()

print("After Clear:", colors)

# ==========================================
# AUTOMATION EXAMPLE
# ==========================================

print("\n=== AUTOMATION EXAMPLE ===")

test_result = {
    "test_name": "Login Test",
    "browser": "Chrome",
    "status": "Passed",
    "execution_time": "1.8 seconds"
}

print("Test Result")

for key, value in test_result.items():
    print(f"{key}: {value}")

