import sqlite3

# Connect to database (or create if not exists)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    grade TEXT
)
''')

# Function to add student
def add_student(name, age, course, grade):
    cursor.execute("INSERT INTO students (name, age, course, grade) VALUES (?, ?, ?, ?)", (name, age, course, grade))
    conn.commit()
    print("✅ Student added successfully!")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | Grade: {row[4]}")

# Function to update student
def update_student(student_id, new_name, new_age, new_course, new_grade):
    cursor.execute("""
        UPDATE students
        SET name=?, age=?, course=?, grade=?
        WHERE id=?
    """, (new_name, new_age, new_course, new_grade, student_id))
    conn.commit()
    print("✅ Record updated successfully!")

# Function to delete student
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("🗑️ Student deleted successfully!")

# Menu system
while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        grade = input("Enter grade: ")
        add_student(name, age, course, grade)

    elif choice == '2':
        view_students()

    elif choice == '3':
        student_id = int(input("Enter student ID to update: "))
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        new_course = input("Enter new course: ")
        new_grade = input("Enter new grade: ")
        update_student(student_id, new_name, new_age, new_course, new_grade)

    elif choice == '4':
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)

    elif choice == '5':
        print("👋 Exiting system...")
        break

    else:
        print("❌ Invalid choice! Try again.")

conn.close()
