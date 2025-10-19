from abc import ABC


class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name):
        item = restaurant.menu.find_item(item_name)

        if item:
            pass
        else:
            print("Item not found.")

    def view_cart(self):
        print("\t**********************\t")
        print("\t\tORDER\t\t")
        print("\t**********************\t")
        print("Name\t\tPrice\t\tQuantity\n")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t\t{item.price}\t\t{quantity}")

        print(f"\nTotal Price: {item.total_price}")


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

    def add_menu_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def delete_item(self, restaurant, item):
        restaurant.menu.remove_item(item)


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
                f"Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}\n\n"
                f"Address: {emp.address}, Age: {emp.age}\n\n"
                f"Designation: {emp.designation}, Salary: {emp.salary}\n\n"
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

    def show_menu(self):
        print("\t**********************\t")
        print("\t\tMENU\t\t")
        print("\t**********************\t")
        print("Name\t\tPrice\t\tQuantity\n")
        for item in self.items:
            print(f"{item.name}\t\t{item.price}\t\t{item.quantity}")


class FoodItem:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity


class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

    def remove(self, item):
        if item in self.items:
            del self.items[item]
        else:
            pass

    def total_price(self):
        return sum(item.price * q for item, q in self.items.items())

    def clear(self):
        self.cart = {}


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

mn = Menu()
item = FoodItem("Kacci", 300, 100)
mn.add_menu_items(item)
mn.show_menu()
