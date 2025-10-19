"""
3 types of users: admin, employee, customer
"""

from abc import ABC


class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Employee(User):
    def __init__(
        self,
        name,
        phone,
        email,
        address,
        age,
        designation,
        salary,
    ) -> None:
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.__salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.employees = []

    def add_employee(
        self,
        name,
        phone,
        email,
        address,
        age,
        designation,
        salary,
    ):
        employee = Employee(
            name,
            phone,
            email,
            address,
            age,
            designation,
            salary,
        )
        self.employees.append(employee)
        print(f"{name} is added!!")

    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(
                f"Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, "
                f"Address: {emp.address}, Age: {emp.age}, "
                f"Designation: {emp.designation}, Salary: {emp.salary}"
            )
