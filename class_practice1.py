class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def show_details(self):
        print(f'Name: {self.name}, Age: {self.age}')


    def update_age(self, new_age):
        self.age = new_age


    def validate_age(self, new_age_val):
        if new_age_val >= 0:
            self.age = new_age_val
            return True
        else:
            print('Invalid age')
            return False


student1 = Student('James', 25)
student2 = Student('Bob', 30)
student1.show_details()
student2.show_details()

student1.update_age(26)
student1.show_details()

# student2.validate_age(-5)
# student2.show_details()
print(student2.validate_age(-5))