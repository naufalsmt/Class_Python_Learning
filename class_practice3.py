class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @property
    def age(self):
        return self._age


    # @age.setter
    # def age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         print("Invalid age")

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError('Age must be greater than 0')
        self._age = new_age


try:
    student = Student('Bob', -20)
    print(student.age)
except ValueError as e:
    print(f"Invalid input,", e)