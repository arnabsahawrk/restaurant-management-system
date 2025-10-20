from abc import ABC

from food_item import FoodItem
from orders import Order


class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Admin(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_items(item)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def delete_item(self, restaurant, item):
        restaurant.menu.remove_item(item)


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


class Customer(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)

        if item:
            if item.quantity >= quantity:
                self.cart.add_item(FoodItem(item.name, item.price, quantity))
                print("Item added.")
            else:
                print("Item quantity is not available.")
        else:
            print("Item not found.")

    def view_cart(self):
        if len(self.cart.items):
            print("\t**********************\t")
            print("\t\tORDER\t\t")
            print("\t**********************\t")
            for item, quantity in self.cart.items.items():
                print(
                    f"Name: {item.name}\tPrice: {item.price}\t",
                    f"Quantity: {quantity}",
                )

            print(f"Total Price: {self.cart.total_price}")
        else:
            print("Not added any food yet.")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} taka paid successfully.")
        self.cart.clear()
