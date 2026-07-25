"""
This file demonstrates:
- Creating lists
- Accessing list items
- Modifying lists
- Adding and removing items
- List length
- Iterating through lists
- Checking Membership in a List
"""

# ==========================================
# CREATING LISTS
# ==========================================

print("=== CREATING LISTS ===")

fruits = ["Apple", "Banana", "Orange"]
numbers = [10, 20, 30, 40]
mixed_list = ["John", 25, True]

print(fruits)
print(numbers)
print(mixed_list)

# ==========================================
# ACCESSING LIST ITEMS
# ==========================================

print("\n=== ACCESSING LIST ITEMS ===")

print("First Fruit:", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit:", fruits[-1])

# ==========================================
# MODIFYING LIST ITEMS
# ==========================================

print("\n=== MODIFYING LIST ITEMS ===")

fruits[1] = "Mango"

print(fruits)

# ==========================================
# ADDING ITEMS
# ==========================================

print("\n=== ADDING ITEMS ===")

fruits.append("Grapes")
print("After append():", fruits)

fruits.insert(1, "Pineapple")
print("After insert():", fruits)

# ==========================================
# EXTENDING A LIST
# ==========================================

print("\n=== EXTEND LIST ===")

more_fruits = [23.4, "Kiwi", "Strawberry", 123, 12]

fruits.extend(more_fruits)

print("After extend():", fruits)

# ==========================================
# REMOVING ITEMS
# ==========================================

print("\n=== REMOVING ITEMS ===")

fruits.remove("Orange")
print("After remove():", fruits)

fruits.remove(123)
print("After remove():", fruits)

fruits.pop(-1)
print("After pop():", fruits)

fruits.pop(4)
print("Only fruits After pop():", fruits)
#removed_fruit = fruits.pop()

#print("Removed Item:", removed_fruit)


# ==========================================
# LIST LENGTH
# ==========================================

print("\n=== LIST LENGTH ===")

print("Total Fruits:", len(fruits))

# ==========================================
# CHECK IF ITEM EXISTS
# ==========================================

print("\n=== CHECK ITEM ===")

if "Apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")

# ==========================================
# LOOP THROUGH A LIST
# ==========================================

print("\n=== LOOP THROUGH LIST ===")

for fruit in fruits:
    print(fruit)

# ==========================================
# SORTING A LIST
# ==========================================

print("\n=== SORTING ===")

numbers = [45, 12, 88, 6, 29]

print("Original:", numbers)

numbers.sort()

print("Sorted:", numbers)

# ==========================================
# CHECKING MEMBERSHIP
# ==========================================

brands = ["BMW", "BENZ", "FORD", "FERRARI", "PORCH", "BENZ"]

print("\n === check membership ===")
print("TOYOTA" in brands)

print("\n === Check amount in the list ===")
print(brands.count("Benz"))
print(brands.count("BENZ"))
print(brands.count("PORCH"))

print("\n === Check index in the list ===")
print(brands.index("PORCH"))
