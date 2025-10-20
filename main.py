from food_item import FoodItem
from restaurant import Restaurant
from users import Admin, Customer, Employee

my_restaurant = Restaurant("Eater")


def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")

    customer = Customer(name=name, email=email, phone=phone, address=address)
    print(f"Welcome {customer.name}!!")
    while True:
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(my_restaurant)
        elif choice == 2:
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))

            customer.add_to_cart(
                my_restaurant,
                item_name=name,
                quantity=quantity,
            )
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid choice.")


def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")

    admin = Admin(name=name, email=email, phone=phone, address=address)
    print(f"Welcome {admin.name}!!")
    while True:
        print("1. Add new employee")
        print("2. View employees")
        print("3. Add new item")
        print("4. View items")
        print("5. Delete item")
        print("6. Exit")

        choice = int(input("Select your option: "))
        if choice == 1:
            name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            phone = input("Enter employee phone: ")
            address = input("Enter employee address: ")
            age = int(input("Enter employee age: "))
            designation = input("Enter employee designation : ")
            salary = int(input("Enter employee salary: "))

            employee = Employee(
                name=name,
                email=email,
                phone=phone,
                address=address,
                age=age,
                designation=designation,
                salary=salary,
            )
            admin.add_employee(restaurant=my_restaurant, employee=employee)
        elif choice == 2:
            admin.view_employee(restaurant=my_restaurant)
        elif choice == 3:
            name = input("Enter item name: ")
            price = int(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))

            item = FoodItem(name=name, price=price, quantity=quantity)
            admin.add_new_item(restaurant=my_restaurant, item=item)
        elif choice == 4:
            admin.view_menu(restaurant=my_restaurant)
        elif choice == 5:
            name = input("Enter item name: ")
            admin.delete_item(my_restaurant, name)
        elif choice == 6:
            break
        else:
            print("Invalid choice.")


while True:
    print(f"Welcome to {my_restaurant.name} restaurant!!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input.")
