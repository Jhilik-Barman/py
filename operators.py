# ==========================================
# Python Operators - Complete Basic Example
# ==========================================


# ==========================================
# 1. Arithmetic Operators
# ==========================================
# Arithmetic operators are used for mathematical calculations.

a = 10
b = 3

print("===== Arithmetic Operators =====")

# Addition (+)
print("Addition:", a + b)

# Subtraction (-)
print("Subtraction:", a - b)

# Multiplication (*)
print("Multiplication:", a * b)

# Division (/)
print("Division:", a / b)

# Floor Division (//)
# Returns the whole number part of the division.
print("Floor Division:", a // b)

# Modulus (%)
# Returns the remainder after division.
print("Modulus:", a % b)

# Exponentiation (**)
# Raises the first number to the power of the second number.
print("Exponentiation:", a ** b)


# ==========================================
# 2. Assignment Operators
# ==========================================
# Assignment operators are used to assign or update values.

print("\n===== Assignment Operators =====")

x = 10

# Add 5 to x
x += 5
print("After += :", x)

# Subtract 3 from x
x -= 3
print("After -= :", x)

# Multiply x by 2
x *= 2
print("After *= :", x)

# Divide x by 2
x /= 2
print("After /= :", x)

# Floor divide x by 2
x //= 2
print("After //= :", x)

# Find remainder and store it in x
x %= 3
print("After %= :", x)


# ==========================================
# 3. Comparison Operators
# ==========================================
# Comparison operators compare two values.
# The result is always True or False.

print("\n===== Comparison Operators =====")

num1 = 10
num2 = 20

# Equal to
print("Equal:", num1 == num2)

# Not equal to
print("Not Equal:", num1 != num2)

# Greater than
print("Greater Than:", num1 > num2)

# Less than
print("Less Than:", num1 < num2)

# Greater than or equal to
print("Greater Than or Equal:", num1 >= num2)

# Less than or equal to
print("Less Than or Equal:", num1 <= num2)


# ==========================================
# 4. Logical Operators
# ==========================================
# Logical operators are used to combine conditions.

print("\n===== Logical Operators =====")

age = 25
has_id = True

# AND
# Returns True only when both conditions are True.
print("AND:", age >= 18 and has_id == True)

# OR
# Returns True when at least one condition is True.
print("OR:", age >= 18 or has_id == False)

# NOT
# Reverses the result of a condition.
print("NOT:", not has_id)


# ==========================================
# 5. Identity Operators
# ==========================================
# Identity operators check whether two variables
# refer to the same object in memory.

print("\n===== Identity Operators =====")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

# is
# Checks whether both variables refer to the same object.
print("list1 is list2:", list1 is list2)

# is not
# Checks whether both variables refer to different objects.
print("list1 is not list3:", list1 is not list3)


# ==========================================
# 6. Membership Operators
# ==========================================
# Membership operators check whether a value
# exists inside a sequence such as a list or string.

print("\n===== Membership Operators =====")

fruits = ["Apple", "Banana", "Mango"]

# in
# Checks whether a value exists in the list.
print("Apple in fruits:", "Apple" in fruits)

# not in
# Checks whether a value does not exist in the list.
print("Orange not in fruits:", "Orange" not in fruits)


# ==========================================
# 7. Bitwise Operators
# ==========================================
# Bitwise operators work with numbers at the binary level.

print("\n===== Bitwise Operators =====")

p = 5
q = 3

# Bitwise AND
print("Bitwise AND:", p & q)

# Bitwise OR
print("Bitwise OR:", p | q)

# Bitwise XOR
print("Bitwise XOR:", p ^ q)

# Bitwise NOT
print("Bitwise NOT:", ~p)

# Left Shift
print("Left Shift:", p << 1)

# Right Shift
print("Right Shift:", p >> 1)


# ==========================================
# 8. Operator Precedence
# ==========================================
# Python follows operator precedence when
# multiple operators are used together.

print("\n===== Operator Precedence =====")

result = 10 + 5 * 2

# Multiplication is performed before addition.
print("Result:", result)


# ==========================================
# End of Python Operators Example
# ==========================================