import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL
)
""")
conn.commit()

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print("✅ Student added successfully!\n")

def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    if records:
        print("\n--- Student Records ---")
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Grade: {row[3]}")
        print("------------------------\n")
    else:
        print("⚠️ No student records found.\n")

def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    grade = input("Enter new grade: ")
    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, student_id))
    conn.commit()
    if cursor.rowcount > 0:
        print("✅ Student updated successfully!\n")
    else:
        print("⚠️ Student ID not found.\n")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("✅ Student deleted successfully!\n")
    else:
        print("⚠️ Student ID not found.\n")

def main():
    while True:
        print("===== Student Records Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
    conn.close()
