students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "F"

    students[name] = {
        "Marks": marks,
        "Grade": grade
    }

print("\nStudent Report:")

for name, details in students.items():
    print(f"{name} -> Marks: {details['Marks']}, Grade: {details['Grade']}")





Enter number of students:  2
Enter student name:  sid
Enter marks:  45
Enter student name:  monu
Enter marks:  56

Student Report:
sid -> Marks: 45, Grade: F
monu -> Marks: 56, Grade: F