def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >=60:
        return "C"
    else:
        return "F"

students = []


num_students = int(input("How many students do you want to enter?: "))

for i in range(num_students):
    name = input("Enter name of student: ")
    marks1 = int(input(f"Enter marks in subject 1 for {name}: "))
    marks2 = int(input(f"Enter marks in subject 2 for {name}: "))
    marks3 = int(input(f"Enter marks in subject 3 for {name}: "))

    total_subjects = 3
    total_marks = marks1 + marks2 + marks3

    average = total_marks / total_subjects

    grade = calculate_grade(average)

    student_record = {"name": name,
                      "average": average,
                      "grade": grade}

    students.append(student_record)
print("---Results---")
    

for i in students:
    print(f"Name: {i['name']}, Average: {i['average']}, Grade: {i['grade']}")


total_average = sum([i['average'] for i in students])
print(total_average)
class_average = total_average / num_students

print(f"Class Average: {class_average}")

