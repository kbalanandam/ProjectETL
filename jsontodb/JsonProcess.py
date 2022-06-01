import json


class Student:
    def __init__(self, student_id, department, name, email):
        self.student_id = student_id
        self.department = department
        self.first_name = name['first']
        self.last_name = name['last']
        self.email = email

    @staticmethod
    def create_from_json(data):
        json_dictionary = json.loads(data)
        return Student(**json_dictionary)

    def __str__(self):
        return "<Student {0}>".format(self.first_name)


# Test
student_python = []

with open("nested_student.json", "r") as json_data:
    student_json = json.loads(json_data.read())

    for student in student_json:
        student_python.append(Student(**student))

# Displaying student from python object
print("\n\nAll student python objects")
print("------------------------------")
for student in student_python:
    print('Python Object:', student)

# Detail of first student
print("\n\nDetail of first student")
print("------------------------------")
print("student_id:", student_python[0].student_id)
print("department:", student_python[0].department)
print("first name:", student_python[0].first_name)
print("last name:", student_python[0].last_name)
print("email:", student_python[0].email)
