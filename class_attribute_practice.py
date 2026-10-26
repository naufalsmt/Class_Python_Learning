class Student:
    school = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student('Alex', 26)
student2 = Student('Bob', 36)
print(student1.name)
print(student1.age)
print(student1.school)
print(student2.school)

student1.school = 'XYZ School'
print(student1.school)
print(student2.school)