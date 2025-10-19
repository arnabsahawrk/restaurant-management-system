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

    @property
    def salary(self):
        return self.__salary


class Admin(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()


class Restaurant:
    def __init__(self, name) -> None:
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(
                f"Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, "
                f"Address: {emp.address}, Age: {emp.age}, "
                f"Designation: {emp.designation}, Salary: {emp.salary}"
            )


class Menu:
    def __init__(self) -> None:
        self.items = []

    def add_menu_items(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)

        if item:
            self.items.remove(item)
            print("Item deleted")
        else:
            print("Item no found")


ad = Admin("Arnab", 1517824769, "arnabsahawrk@gmail.com", "Dhaka")
# ad.add_employee("Ridom", 123, "ridom.com", "Noakhali", 24, "Editor", 20000)
res = Restaurant("Khana-Dana")
ad.add_employee(
    res,
    Employee(
        "Ridom",
        123,
        "ridom.com",
        "Noakhali",
        24,
        "Editor",
        20000,
    ),
)
ad.view_employee(res)
