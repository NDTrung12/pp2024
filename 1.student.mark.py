def students():
    student_id = input('Enter the student ID:')
    student_name = input('Enter the student name:')
    date_of_birth = input('Enter the dob of the student(DD-MM_YY) :')
    student = {
    "name":student_name,
    "id":student_id,
    "dob": date_of_birth,
    
} 
    students.append(student),

courses = []
a = 12
b = 5
numberofstudents = type(a)
numberofcourses = type(b)
print()
def courses():
    course_id = input('Enter the course ID:')
    course_name = input('Enter the course name:')
    course = {
        "name":course_name,
        "id":course_id,
    }
    courses.append(course),

def marks():
    course_id = input('Enter the ID to input marks:')
    student_id = input()
    for course in courses:
        if course[id] == course_id:
            break
        else:
            print('Not found')

    for student in students:
        mark = students[student_id][course_id]

def list_students():
    for student_id,student_name,date_of_birth in students:
        print(f"ID : {student_id},Name:{student_name},DOB:{date_of_birth}")
def list_courses():
    for course in courses:
        print(f"{course['id']:{course['name']}}")
while True:
    choice = input('Enter the choice\n')
    print('1.The number of students\n')
    print('2.The number of courses\n')
    print('3.Student details\n')
    print('4.Course details\n')
    print('5.Marks\n')
    print('6.Exit.')
    
    if choice == "1":
        numberofstudents,
    elif choice == "2":
        numberofcourses,
    elif choice == '3':
        students(),
    elif choice == '4':
        courses(),
    elif choice == '5':
        marks(),
    elif choice == '6':
        print('End'),
    else:
        print('Valid choice,try again')
