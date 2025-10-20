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
        if len(self.items):
            print("\t**********************\t")
            print("\t\tMENU\t\t")
            print("\t**********************\t")
            for item in self.items:
                print(
                    f"Name: {item.name}\tPrice: {item.price}\t",
                    f"Quantity: {item.quantity}",
                )
        else:
            print("Menu isn't available yet.")
