import pandas as pd
import os

FILE_NAME = "student_marks.csv"

print("=== STUDENT MARKS ANALYZER ===")

#  LOAD PREVIOUS DATA
if os.path.exists(FILE_NAME):
    try:
        df = pd.read_csv(FILE_NAME)

        # If file exists but empty/corrupted
        if df.empty or "Name" not in df.columns or "Marks" not in df.columns:
            print("CSV file was empty or invalid. Starting fresh.")
            df = pd.DataFrame(columns=["Name", "Marks"])
        else:
            print("\nPrevious data loaded successfully!")

    except Exception as e:
        print("Error loading CSV:", e)
        df = pd.DataFrame(columns=["Name", "Marks"])

else:
    print("\nNo previous data found. Starting fresh.")
    df = pd.DataFrame(columns=["Name", "Marks"])

# ADD NEW STUDENTS
try:
    n = int(input("\nEnter number of new students to add: "))

    if n < 0:
        print("Number cannot be negative!")
        n = 0

except ValueError:
    print("Invalid input! Setting number of students to 0.")
    n = 0

for i in range(n):

    # Name input validation
    while True:
        name = input(f"\nEnter student {i+1} name: ").strip()

        if name == "":
            print("Name cannot be empty!")
        else:
            break

    # Marks validation
    while True:
        try:
            marks = float(input(f"Enter marks for {name}: "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100!")
            else:
                break

        except ValueError:
            print("Invalid marks! Enter numeric value.")

    # Add to DataFrame
    new_row = pd.DataFrame({
        "Name": [name],
        "Marks": [marks]
    })

    df = pd.concat([df, new_row], ignore_index=True)

#  EMPTY DATASET CHECK
if df.empty:
    print("\nDataset is empty!")
else:

    #  DISPLAY DATA
    print("\n=== STUDENT DATA ===")
    print(df)

    # ANALYSIS
    topper_index = df["Marks"].idxmax()

    print("\nTopper:")
    print(df.loc[topper_index, "Name"], "-", df.loc[topper_index, "Marks"])

    print("\nAverage Marks:", df["Marks"].mean())

    print("Highest Marks:", df["Marks"].max())
    print("Lowest Marks:", df["Marks"].min())

    # Students above 75
    print("\nStudents scoring above 75:")
    print(df[df["Marks"] > 75])

    # Failed students
    print("\nFailed Students:")
    print(df[df["Marks"] < 40])

# UPDATE STUDENT
update = input("\nDo you want to update student marks? (y/n): ").lower()

if update == "y":

    if df.empty:
        print("No data available to update!")

    else:
        student_name = input("Enter student name to update: ").strip()

        # Check if student exists
        if student_name in df["Name"].values:

            while True:
                try:
                    new_marks = float(input("Enter new marks: "))

                    if 0 <= new_marks <= 100:
                        break
                    else:
                        print("Marks must be between 0 and 100!")

                except ValueError:
                    print("Invalid marks!")

            df.loc[df["Name"] == student_name, "Marks"] = new_marks
            print("Marks updated successfully!")

        else:
            print("Student not found!")

#  DELETE STUDENT
delete = input("\nDo you want to delete a student? (y/n): ").lower()

if delete == "y":

    if df.empty:
        print("No data available!")

    else:
        student_name = input("Enter student name to delete: ").strip()

        if student_name in df["Name"].values:

            df = df[df["Name"] != student_name]
            print("Student deleted successfully!")

        else:
            print("Student not found!")

# SORT DATA
if not df.empty:

    print("\n=== SORTED DATA (HIGH TO LOW) ===")
    sorted_df = df.sort_values(by="Marks", ascending=False)

    print(sorted_df)

#  SAVE CSV
try:
    df.to_csv(FILE_NAME, index=False)
    print(f"\nData saved successfully to '{FILE_NAME}'")

except Exception as e:
    print("Error saving CSV:", e)