print("===== Student Result Calculator =====")

name = input("Enter Student Name: ")

math = float(input("Enter Math Marks: "))
english = float(input("Enter English Marks: "))
science = float(input("Enter Science Marks: "))

total = math + english + science
average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Result =====")
print("Student Name:", name)
print("Math:", math)
print("English:", english)
print("Science:", science)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)

if grade == "F":
    print("Result: Fail ❌")
else:
    print("Result: Pass ✅")