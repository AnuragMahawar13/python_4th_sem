#Q50. Python program to filter student records with grade >= 95 using filter() function:

students = [
    {"name": "Anurag", "age": 19, "grade": 95},
    {"name": "Navya", "age": 19, "grade": 95},
    {"name": "Nikhilesh", "age": 19, "grade": 97},
    {"name": "Shivam", "age": 19, "grade": 88},
    {"name": "Kavyansh", "age": 19, "grade": 99}
]

# Filter students with grade >= 95
high_achievers = list(filter(lambda student: student["grade"] >= 95, students))

print("Students with grade >= 95:")
for student in high_achievers:
    print(student)