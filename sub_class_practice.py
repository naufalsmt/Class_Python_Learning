class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def show_details(self):
        print(f'Name: {self.name}, Age: {self.age}')


class Grade(Student):
    def grade_student(self):
        print("Course: Software Engineer")


student = Grade("Xavier", 26)
student.show_details()
student.grade_student()
