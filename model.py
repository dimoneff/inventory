class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.products = []

    def save(self):
        if self.name and self.price and self.quantity:
            self.products.append(Product(self.name, self.price, self.quantity))
        else:
            print("Incomplete")
            raise IncompleteDataError("Insufficient data!")

    def load(self):
        if self.products:
            return self.products

    def save_to_file(self):
        with open("products.txt", "w") as file:
            products = self.load()
            if products:
                for product in products:
                    file.write(f"{product.name}, {product.price}, {product.quantity}\n")

    def load_from_file(self):
        try:
            with open("products.txt") as file:
                products = file.readlines()
                for product in products:
                    product = product.split(",")
                    name = product[0]
                    price = float(product[1].strip())
                    qnt = int(product[2].strip())
                    self.products.append(Product(name, price, qnt))
        except FileNotFoundError:
            pass


class IncompleteDataError(TypeError):
    pass
