"""

This file demonstrates:
- Creating a class
- Creating objects
- Class attributes
- Instance methods
- The __init__() constructor
- The self keyword

"""

# ==========================================
# DEFINING A CLASS
# ==========================================

class Student:
    """A simple Student class."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduce(self):
        """Print student information."""
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")


# ==========================================
# CREATING OBJECTS
# ==========================================

print("=== STUDENT OBJECTS ===")

student1 = Student("John", "Smith", 25)
student2 = Student("Nathan", "Brown", 21)

student1.introduce()
print()

student2.introduce()

# ==========================================
# ACCESSING OBJECT ATTRIBUTES
# ==========================================

print("\n=== ACCESSING ATTRIBUTES ===")

print(student1.first_name)
print(student1.last_name)
print(student1.age)

# ==========================================
# MODIFYING ATTRIBUTES
# ==========================================

print("\n=== MODIFYING ATTRIBUTES ===")

student1.age = 26

print(f"{student1.first_name}'s new age is {student1.age}")

# ==========================================
# ANOTHER CLASS EXAMPLE
# ==========================================

class Rectangle:
    """Calculate the area of a rectangle."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


print("\n=== RECTANGLE ===")

rectangle = Rectangle(10, 5)

print("Area:", rectangle.area())

# ==========================================
# AUTOMATION EXAMPLE
# ==========================================

class Browser:
    """Represent a browser used for automation."""

    def __init__(self, name, headless):
        self.name = name
        self.headless = headless

    def launch(self):
        print(f"Launching {self.name} browser...")
        print(f"Headless Mode: {self.headless}")


print("\n=== AUTOMATION EXAMPLE ===")

chrome = Browser("Chrome", True)
firefox = Browser("Firefox", False)

chrome.launch()
print()
firefox.launch()