class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Creating a list of student objects
students = [
    Student("John Doe", "A101", 3.8),
    Student("Jane Doe", "B202", 3.9),
    Student("Jim Smith", "C303", 3.7),
    Student("Jill Johnson", "D404", 4.0)
]

# Sorting the list of students
sorted_students = sort_students(students)

# Printing the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")￼Not
