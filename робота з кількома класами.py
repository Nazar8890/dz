#Реалізуйте систему для онлайн-магазину. Створіть клас Product з властивостями, такими як назва, ціна, наявність тощо. Створіть клас Cart для управління кошиком покупця з методами для додавання товарів, видалення, підрахунку загальної вартості тощо.
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, quantity):
        return self.stock >= quantity

    def reduce_stock(self, quantity):
        if self.is_available(quantity):
            self.stock -= quantity
            return True
        return False

    def __str__(self):
        return f"{self.name} | Ціна: {self.price} грн | В наявності: {self.stock}"


class Cart:
    def __init__(self):
        self.items = {}  # product -> quantity

    def add_product(self, product, quantity=1):
        if product.is_available(quantity):
            product.reduce_stock(quantity)
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            print(f"Додано {quantity} x {product.name} до кошика")
        else:
            print("Недостатньо товару на складі")

    def remove_product(self, product):
        if product in self.items:
            product.stock += self.items[product]
            del self.items[product]
            print(f"{product.name} видалено з кошика")

    def total_price(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    def show_cart(self):
        if not self.items:
            print("Кошик порожній")
            return

        print("Кошик:")
        for product, quantity in self.items.items():
            print(f"{product.name} x{quantity} = {product.price * quantity} грн")
        print(f"Загальна сума: {self.total_price()} грн")


p1 = Product("Ноутбук", 25000, 5)
p2 = Product("Миша", 500, 20)

cart = Cart()

cart.add_product(p1, 1)
cart.add_product(p2, 2)

cart.show_cart()

cart.remove_product(p2)

cart.show_cart()
