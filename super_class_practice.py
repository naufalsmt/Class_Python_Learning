"""
Create two classes:
1. Employee with __init__(self, name) and a method called show_name().
2. QAEngineer that inherits from Employee and has a method called test_software() that prints "Testing software".
Create a QAEngineer object named "James" and call both methods.
"""

class Employee:
    def __init__(self, name):
        self.name = name


    def show_name(self):
        print(f"Employee name: {self.name}")


class QAEngineer(Employee):
    def test_software(self):
        print("Testing software")


employee = QAEngineer("James")
employee.show_name()
employee.test_software()