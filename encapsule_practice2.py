class Student:
    def __init__(self, marks):
        self.__marks = marks

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("You cannot withdraw negative marks")

    def get_marks(self):
        return self.__marks

student = Student(50)
print(student.get_marks())

student.update_marks(175)
print(student.get_marks())