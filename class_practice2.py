class Employee:
    def show_role(self):
        print("General Employee")


class QAEngineer(Employee):
    def show_role(self):
        super().show_role()
        print("QA Engineer")


# qa_engineer = Employee()
# qa_engineer.show_role()

qa_engineer = QAEngineer()
qa_engineer.show_role()