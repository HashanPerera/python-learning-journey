"""
This file demonstrates:
- Creating strings
- Single and double quotes
- String concatenation
- f-strings
- Common string methods
- Formatting method
"""

# Creating strings
first_name = "John"
last_name = 'Smith'

# Print strings
print(first_name)
print(last_name)

# String concatenation
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# f-string (recommended)
print(f"Welcome, {full_name}!")

# String length
print("Length:", len(full_name))

# Change case
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())

# Remove extra spaces
message = "   Python Programming   "
print("Original:", message)
print("Stripped:", message.strip())

# Replace text
course = "Python Basics"
print(course.replace("Basics", "Programming"))

# Check if a string contains text
email = "john@example.com"
print("Contains '@':", "@" in email)
print("Starts with 'john':", email.startswith("john"))
print("Ends with '.com':", email.endswith(".com"))

# String indexing
language = "Python"
print("First character:", language[0])
print("Last character:", language[-1])

# String slicing
print("First three letters:", language[:3])
print("Last three letters:", language[-3:])

# Capitalized example
browser = "chrome"
print(f"Launching {browser.capitalize()} browser...")

#Python formatting method
name = 'Nathan'
schoolYears = 5
school = "St.Stewart"
print("{} attended {}'s School in Edinburgh for {} years".format(name, school, schoolYears))
#or
print(f"{name} attended {school}'s School in Edinburgh for {schoolYears} years")
