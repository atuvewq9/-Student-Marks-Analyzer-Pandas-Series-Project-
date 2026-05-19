import pandas as pd

print("=== STUDENT MARKS ANALYZER ===")

n = int(input("Enter number of students: "))

data = {}

# Taking user input
for i in range(n):
    name = input(f"Enter student {i+1} name: ")
    marks = float(input(f"Enter marks for {name}: "))
    data[name] = marks

# Create Series
marks = pd.Series(data)

print("\n=== MARKS DATA ===")
print(marks)

# 1. Topper
topper_name = marks.idxmax()
print("\nTopper:", topper_name, "-", marks.max())

# 2. Average
print("Average Marks:", marks.mean())

# 3. Highest & Lowest
print("Highest Marks:", marks.max())
print("Lowest Marks:", marks.min())

# 4. Students above 75
print("\nStudents scoring above 75:")
print(marks[marks > 75])

# 5. Students below 40 (Fail)
print("\nFailed Students:")
print(marks[marks < 40])

# 6. Add new student
add = input("\nDo you want to add a new student? (y/n): ")
if add.lower() == "y":
    name = input("Enter name: ")
    mark = float(input("Enter marks: "))
    marks.loc[name] = mark

print("\nUpdated Data:")
print(marks)

# 7. Update student marks
update = input("\nDo you want to update any student? (y/n): ")
if update.lower() == "y":
    name = input("Enter student name: ")
    if name in marks.index:
        mark = float(input("Enter new marks: "))
        marks.loc[name] = mark
    else:
        print("Student not found!")

print("\nFinal Data:")
print(marks)

# 8. Sorted output
print("\nSorted Marks (High to Low):")
print(marks.sort_values(ascending=False))