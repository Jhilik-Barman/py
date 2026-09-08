# ==========================================
# Python Loops - Complete Basic Example
# ==========================================


# ==========================================
# 1. For Loop
# ==========================================
# A for loop is used to repeat a block of code
# for each item in a sequence.

print("===== For Loop =====")

for i in range(1, 6):
    # This code will run 5 times.
    print("Number:", i)


# ==========================================
# 2. For Loop with a List
# ==========================================
# A for loop can be used to go through each
# item in a list.

print("\n===== For Loop with List =====")

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    # Print each fruit from the list.
    print("Fruit:", fruit)


# ==========================================
# 3. range() Function
# ==========================================
# range() generates a sequence of numbers.
# range(5) generates numbers from 0 to 4.

print("\n===== range() Example =====")

for number in range(5):
    print("Number:", number)


# ==========================================
# 4. range() with Start and End
# ==========================================
# range(start, end) starts from the start value
# and stops before the end value.

print("\n===== range(start, end) =====")

for number in range(1, 6):
    print(number)


# ==========================================
# 5. range() with Step
# ==========================================
# range(start, end, step) allows us to
# control how much the number increases.

print("\n===== range() with Step =====")

for number in range(2, 11, 2):
    # The loop increases by 2 each time.
    print(number)


# ==========================================
# 6. While Loop
# ==========================================
# A while loop repeats the code as long as
# the given condition is True.

print("\n===== While Loop =====")

count = 1

while count <= 5:
    print("Count:", count)

    # Increase count by 1.
    # Without this, the loop could run forever.
    count += 1


# ==========================================
# 7. Break Statement
# ==========================================
# The break statement stops the loop immediately.

print("\n===== Break Example =====")

for number in range(1, 11):

    if number == 6:
        # Stop the loop when number becomes 6.
        break

    print(number)


# ==========================================
# 8. Continue Statement
# ==========================================
# The continue statement skips the current
# iteration and moves to the next iteration.

print("\n===== Continue Example =====")

for number in range(1, 6):

    if number == 3:
        # Skip number 3.
        continue

    print(number)


# ==========================================
# 9. Loop with if Condition
# ==========================================
# We can use if conditions inside a loop.

print("\n===== Loop with If Condition =====")

for number in range(1, 11):

    if number % 2 == 0:
        # % checks the remainder.
        # If remainder is 0, the number is even.
        print(number, "is Even")

    else:
        print(number, "is Odd")


# ==========================================
# 10. Nested Loop
# ==========================================
# A loop inside another loop is called
# a nested loop.

print("\n===== Nested Loop =====")

for i in range(1, 4):

    for j in range(1, 4):
        print("i =", i, "j =", j)


# ==========================================
# 11. Simple Multiplication Table
# ==========================================
# We can use a loop to create a multiplication table.

print("\n===== Multiplication Table =====")

number = 5

for i in range(1, 11):

    result = number * i

    print(number, "x", i, "=", result)


# ==========================================
# 12. Sum of Numbers Using Loop
# ==========================================
# We can use a loop to calculate the sum
# of multiple numbers.

print("\n===== Sum of Numbers =====")

total = 0

for number in range(1, 6):

    total = total + number

print("Total:", total)


# ==========================================
# End of Python Loops Example
# ==========================================