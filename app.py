import customtkinter
from main_page import MainPage
from product_page import ProductPage
from model import Product, IncompleteDataError
import atexit


class Application(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inventory")
        self.geometry("700x520")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.iconbitmap("img/product-64.ico")
        self.resizable(False, False)

        # create an inner container for widgets
        container = customtkinter.CTkFrame(self)
        container.grid(padx=10, pady=10, sticky="nsew")
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        self.product_page = ProductPage(container, self)
        self.main_page = MainPage(container, self)
        self.product_page.grid(row=0, column=0, sticky="nsew")
        self.main_page.grid(row=0, column=0, sticky="nsew")
        self.pages = {"Main Page": self.main_page, "Product Page": self.product_page}
        self.product = Product("orange", "9.99", "5")
        self.load_from_file()
        atexit.register(self.exit_handler)

    def change_pages(self, container):
        page = self.pages[container]
        page.tkraise()

    def save(self, name, price, quantity):
        self.product.name = name
        self.product.price = price
        self.product.quantity = quantity
        try:
            self.product.save()
            self.main_page.show_message("Product saved!", "success")
        except ValueError:
            self.main_page.show_message("Data incorrect!", "error")
        except IncompleteDataError as err:
            print(err)
            self.main_page.show_message(err, "error")

    def load(self):
        return self.product.load()

    def remove(self, product):
        try:
            self.product.products.remove(product)
        except ValueError as err:
            self.main_page.show_message(err, "error")

    def exit_handler(self):
        self.product.save_to_file()

    def load_from_file(self):
        self.product.load_from_file()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
