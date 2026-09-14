def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_highest(marks):
    return max(marks)


def calculate_lowest(marks):
    return min(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


subjects = ["Python", "Data Structures", "Operating System"]

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    marks = []

    for subject in subjects:
        mark = float(input("Enter mark for " + subject + ": "))
        marks.append(mark)

    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = calculate_highest(marks)
    lowest = calculate_lowest(marks)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": grade
    }

    students.append(student)


students.sort(key=lambda student: student["total"], reverse=True)


print("\n----- STUDENT PERFORMANCE ANALYSIS -----")

for student in students:
    print("\nName:", student["name"])

    for i in range(len(subjects)):
        print(subjects[i] + ":", student["marks"][i])

    print("Total:", student["total"])
    print("Average:", round(student["average"], 2))
    print("Highest:", student["highest"])
    print("Lowest:", student["lowest"])
    print("Grade:", student["grade"])