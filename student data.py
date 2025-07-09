# Step 1: Student class define panrom
class Student:
    def __init__(self, student_id, name, standard, Tamil, English, Maths, Science, Social):  # FIXED: __init__ spelling
        self.student_id = student_id
        self.name = name
        self.standard = standard
        self.Tamil = Tamil
        self.English = English
        self.Maths = Maths
        self.Science = Science
        self.Social = Social
    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Standard: {self.standard}, Tamil: {self.Tamil}, English: {self.English}, Maths: {self.Maths}, Science: {self.Science}, Social: {self.Social}")


# Step 2: Stuent list to store all student objects
students = []


# Step 3: Add student function
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    standard = input("Enter standard: ")
    Tamil = input("Enter Tamil: ")
    English = input("Enter English: ")
    Maths = input("Enter Maths: ")
    Science = input("Enter Science: ")
    Social = input("Enter Social: ")

    s = Student(student_id, name, standard, Tamil, English, Maths, Science, Social)  # Object create
    students.append(s)  # Add to list
    print("✅ Student added successfully!\n")


# Step 4: Display all students
def display_students():
    if not students:
        print("No students found.\n")
    else:
        print("📋 All Students:")
        for s in students:
            s.display()


# Step 5: Search by student ID
def search_student():
    sid = input("Enter student ID to search: ")
    found = False
    for s in students:
        if s.student_id == sid:
            print("🔍 Student Found:")
            s.display()
            found = True
            break
    if not found:
        print("❌ Student not found.\n")


# Step 6: Main menu
while True:
    print("\n🎓 Student Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student by ID")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting... Bye! 👋")
        break
    else:
        print("Invalid choice! Try again.\n")
