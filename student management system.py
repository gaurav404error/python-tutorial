class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.courses = {}  # {course_name: marks}

    def enroll_course(self, course_name):
        if course_name in self.courses:
            print(f"{self.name} is already enrolled in {course_name}")
        else:
            self.courses[course_name] = None
            print(f"{self.name} enrolled in {course_name}")

    def add_marks(self, course_name, marks):
        if course_name in self.courses:
            self.courses[course_name] = marks
            print(f"Marks updated for {self.name} in {course_name}")
        else:
            print(f"{self.name} is not enrolled in {course_name}")

    def show_report_card(self):
        print(f"\nReport Card for {self.name} (Roll No: {self.roll_no})")
        for course, marks in self.courses.items():
            status = "Not Graded" if marks is None else marks
            print(f"{course}: {status}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, roll_no, name):
        if roll_no in self.students:
            print("Student already exists!")
        else:
            self.students[roll_no] = Student(roll_no, name)
            print(f"Student {name} added successfully!")

    def get_student(self, roll_no):
        return self.students.get(roll_no, None)

    def display_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("\nList of Students:")
            for stu in self.students.values():
                print(f"Roll No: {stu.roll_no}, Name: {stu.name}")


sms = StudentManagementSystem()

# Add Students
sms.add_student(101, "Rahul")
sms.add_student(102, "Anita")

# Enroll Students in Courses
stu1 = sms.get_student(101)
stu1.enroll_course("Maths")
stu1.enroll_course("Science")
stu1.add_marks("Maths", 85)
stu1.add_marks("Science", 90)

stu2 = sms.get_student(102)
stu2.enroll_course("Maths")
stu2.add_marks("Maths", 75)

# Display Report Cards
stu1.show_report_card()
stu2.show_report_card()

# Display All Students
sms.display_all_students()
