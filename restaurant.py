from menu import Menu


class Restaurant:
    def __init__(self, name) -> None:
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("\t\tEmployee List\t\t")
        print("-----------------------------------------------")
        for emp in self.employees:
            print(
                f"Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}\n"
                f"Address: {emp.address}, Age: {emp.age}\n"
                f"Designation: {emp.designation}, Salary: {emp.salary}\n"
            )
