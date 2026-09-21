students = {
    "Alex": "Maths",
    "Sam": "Physics",
    "Jamie": "English"
}

print(students.get("Alex"))

students["Jordan"] = "Science"
students["Sam"] = "Maths"

students.pop("Jamie")

print("Number of students:", len(students))

for student, subject in students.items():
    print(student, ":", subject)