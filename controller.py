class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, name, price, quantity):
        self.model.name = name
        self.model.price = price
        self.model.quantity = quantity
        self.model.save()

    def show(self):
        return self.model.show()









