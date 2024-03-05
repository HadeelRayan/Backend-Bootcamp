class Item:
    def __init__(self, name, weight, properties):
        self.name = name
        self.weight = weight
        self.properties = properties

    def __str__(self):
        return f"{self.name} ({self.weight} units)"


class Bag:
    def __init__(self, max_weight=80, max_items=6):
        self.max_weight = max_weight
        self.max_items = max_items
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.max_items and self.current_weight() + item.weight <= self.max_weight:
            self.items.append(item)
            return True
        return False

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name == item_name:
                del self.items[i]
                return True
        return False

    def current_weight(self):
        return sum(item.weight for item in self.items)

    def print_items(self):
        for item in self.items:
            print(item)

    def print_items_by_category(self, category):
        for item in self.items:
            if item.properties.get("category", None) == category:
                print(item)


def main():
    items = [
        Item("Universal Charger", 12, {"Color": "Black", "Price": 50, "Size": "Medium", "Brand": "Lenovo", "category": "Electronics"}),
        Item("Passport", 1, {"Color": "Blue", "Cost": 50, "BoughtFrom": "USA", "category": "Documents"}),
        Item("Sunglasses", 10, {"HaveCase": "Yes", "Color": "Black", "Origin": "Italy", "category": "Accessories"}),
        Item("Sneakers", 14, {"Brand": "New Balance", "New": False, "Bought from": "Spain", "category": "Footwear"}),
        Item("Smartphone", 15, {"Brand": "Apple", "Operating System": "iOS", "Storage": "128GB", "Display": "AMOLED", "Camera": "Dual Lens", "Materials": "Lithium Plastic", "category": "Electronics"}),
        Item("Laptop", 60, {"Brand": "Dell", "Processor": "Intel i7", "RAM": "16GB", "Storage": "512GB SSD", "Graphics": "NVIDIA GeForce4", "category": "Electronics"}),
        Item("Smartwatch", 44, {"Brand": "Samsung", "Display": "Touchscreen", "Battery Life": "3 days", "Fitness Features": "Heart Rate Monitor", "Connectivity": "Bluetooth", "category": "Electronics"}),
        Item("Campus", 4, {"Brand": "Samsung", "Accuracy": "High", "Price": 50, "Materials": "Iron Plastic", "category": "Tools"})
    ]

    bag = Bag()
    for item in items:
        if bag.add_item(item):
            print(f"Added {item.name} to the bag.")
        else:
            print(f"Failed to add {item.name}: Bag is full or overweight.")

    print("\nItems in the bag:")
    bag.print_items()

    print("\nElectronics in the bag:")
    bag.print_items_by_category("Electronics")


if __name__ == "__main__":
    main()