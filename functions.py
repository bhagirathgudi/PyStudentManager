students = []


def get_students_titlecase():
    students_titlecase= []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id = 332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


student_list = get_students_titlecase()


def add_students():
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    add_student(student_name, student_id)
    print_students_titlecase()


add_students()

while True:
    result = input("Do you want to add another student. If Yes enter Yes, else enter No")
    if result == "Yes":
        add_students()
    else:
        break
