class Product:
    def __init__(self, product_id, name, price, quantity):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.list_product = []

    def add_product(self, _product: Product):
        self.list_product.append(_product)

    def get_product(self):
        return self.list_product