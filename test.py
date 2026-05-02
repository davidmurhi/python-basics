class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append(({"name": name, "price": price}))

    def show_items(self):
        for i in self.items:
            print(i["name"], i["price"])

    def total(self):
        total = 0
        for i in self.items:
            total += i["price"]
        return total


cart = ShoppingCart()

cart.add_item("Apple", 2)
cart.add_item("Banana", 3)
cart.add_item("Milk", 5)

print("Items in cart:")
cart.show_items()

print("Total price:", cart.total())
