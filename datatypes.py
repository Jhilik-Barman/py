# ==========================================
# Python Data Types - Complete Basic Example
# ==========================================


# 1. String (str)
# A string is used to store text.
name = "Rahul"

print("Name:", name)
print("Data Type:", type(name))


# 2. Integer (int)
# An integer is used to store whole numbers.
age = 21

print("Age:", age)
print("Data Type:", type(age))


# 3. Float (float)
# A float is used to store decimal numbers.
price = 99.50

print("Price:", price)
print("Data Type:", type(price))


# 4. Boolean (bool)
# A boolean stores either True or False.
is_student = True

print("Is Student:", is_student)
print("Data Type:", type(is_student))


# 5. List
# A list is used to store multiple values.
# A list can contain different types of data.
students = ["Rahul", "Ananya", "Amit"]

print("Students:", students)
print("Data Type:", type(students))


# 6. Tuple
# A tuple is similar to a list,
# but its values cannot be changed after creation.
colors = ("Red", "Green", "Blue")

print("Colors:", colors)
print("Data Type:", type(colors))


# 7. Set
# A set stores multiple unique values.
# Duplicate values are automatically removed.
numbers = {10, 20, 30, 20, 10}

print("Numbers:", numbers)
print("Data Type:", type(numbers))


# 8. Dictionary (dict)
# A dictionary stores data in key-value pairs.
student = {
    "name": "Rahul",
    "age": 21,
    "city": "Kolkata"
}

print("Student:", student)
print("Data Type:", type(student))


# 9. NoneType
# None means that a variable currently has no value.
result = None

print("Result:", result)
print("Data Type:", type(result))


# 10. Complex Number
# A complex number has a real part and an imaginary part.
number = 5 + 3j

print("Complex Number:", number)
print("Data Type:", type(number))


# ==========================================
# Checking Multiple Data Types Together
# ==========================================

name = "Ananya"          # String
age = 22                 # Integer
marks = 85.5             # Float
passed = True             # Boolean
subjects = ["Math", "English"]  # List

print("\n===== Student Information =====")

print("Name:", name)
print("Type:", type(name))

print("Age:", age)
print("Type:", type(age))

print("Marks:", marks)
print("Type:", type(marks))

print("Passed:", passed)
print("Type:", type(passed))

print("Subjects:", subjects)
print("Type:", type(subjects))


# ==========================================
# End of Python Data Types Example
# ==========================================

