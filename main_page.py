import customtkinter
from PIL import Image
from CTkSpinbox import *


class MainPage(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # defining variables
        self.name = customtkinter.StringVar()
        self.price = customtkinter.StringVar()
        self.quantity = customtkinter.StringVar()
        self.message = customtkinter.StringVar()

        # changing fonts
        font_header = ("Helvetica", 18, "bold")
        font_label = ("Helvetica", 16, "bold")
        font_input = ("Helvetica", 20, "bold")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # creating a logo image
        logo_file = Image.open("img/asset.png")
        logo = customtkinter.CTkImage(logo_file, size=(80, 80))

        # creating the company's name
        company_name = customtkinter.CTkLabel(self,
                                              text="STOCK MANAGEMENT SYSTEM",
                                              image=logo,
                                              compound="left",
                                              font=font_header,
                                              text_color="orange")

        # creating widgets
        product_name = customtkinter.CTkLabel(self,
                                              text="Product name:",
                                              font=font_label)

        self.product_name_entry = customtkinter.CTkEntry(self,
                                                         textvariable=self.name,
                                                         font=font_input)

        product_price = customtkinter.CTkLabel(self,
                                               text="Product price:",
                                               font=font_label)

        product_price_entry = customtkinter.CTkEntry(self,
                                                     textvariable=self.price,
                                                     font=font_input)

        product_quantity = customtkinter.CTkLabel(self,
                                                  text="Product quantity:",
                                                  font=font_label)

        self.product_quantity_entry = CTkSpinbox(self,
                                                 variable=self.quantity,
                                                 start_value=0)

        submit_btn = customtkinter.CTkButton(self,
                                             text="GO!",
                                             command=self.button_clicked,
                                             font=font_header,
                                             height=35,
                                             fg_color="#408040",
                                             hover_color="#499349")

        values = ["Add a product",
                  "Show products",
                  "Search a product",
                  "Remove a product",
                  "Update the price",
                  "Sell a product"]

        self.option_menu = customtkinter.CTkOptionMenu(self,
                                                       values=values,
                                                       font=font_label,
                                                       dropdown_font=font_label,
                                                       height=45)

        copyright_label = customtkinter.CTkLabel(self,
                                                 text="Copyright (c) 2024 dimoneff@gmail.com "
                                                      "\nAll Rights Reserved.")

        self.message_label = customtkinter.CTkLabel(self, textvariable=self.message)

        # Creating stock image
        image_file = Image.open("img/stock2.png")
        image = customtkinter.CTkImage(image_file, size=(200, 200))
        image_label = customtkinter.CTkLabel(self, text="", image=image)

        # Placing widgets in the grid

        company_name.grid(row=0, column=0, padx=50, pady=5, columnspan=3, sticky="nwe")
        product_name.grid(row=1, column=0, padx=(50, 5), sticky="w")
        self.product_name_entry.grid(row=1, column=1, sticky="we", ipady=5)
        self.after(200, lambda: self.product_name_entry.focus())
        product_price.grid(row=2, column=0, padx=(50, 5), sticky="w")
        product_price_entry.grid(row=2, column=1, sticky="we", ipady=5)
        product_quantity.grid(row=3, column=0, padx=(50, 5), sticky="w")
        self.product_quantity_entry.grid(row=3, column=1, sticky="we")
        self.option_menu.grid(row=4, column=0, padx=(50, 5), pady=(30, 5), columnspan=2, sticky="w")
        submit_btn.grid(row=5, column=0, padx=(50, 5), pady=10, ipady=5, ipadx=10, sticky="w")
        image_label.grid(row=1, column=3, rowspan=3, padx=(10, 10))
        copyright_label.grid(row=6, column=0, columnspan=4, pady=(20, 5), sticky="swe")
        self.message_label.grid(row=5, column=1, columnspan=3, pady=(0, 40))

    def button_clicked(self):
        match self.option_menu.get():
            case "Add a product":
                self.add_product()

            case "Show products":
                products = self.controller.load()
                self.controller.change_pages("Product Page")
                self.products_to_screen(products)

            case "Search a product":
                found = self.search_product()
                self.products_to_screen(found)
                self.controller.change_pages("Product Page")

            case "Remove a product":
                self.remove_product()

            case "Update the price":
                self.update_price()

            case "Sell a product":
                self.sell_product()

    def product_exists(self, name):
        products = self.controller.load()
        for product in products:
            if product.name == name:
                return product

    def add_product(self):
        name = self.name.get().lower().strip()
        quantity = self.quantity.get()
        product = self.product_exists(name)
        if product:
            product.quantity += int(quantity)
            self.show_message(f"Quantity of {name} updated!", "success")
        else:
            price = self.price.get()
            try:
                price = float(price)
                if price > 0:
                    self.controller.save(name, price, quantity)
                    self.show_message(f"{name.capitalize()} added!", "success")
                else:
                    raise ValueError("Negative price!")
            except ValueError as err:
                print(err)
                self.show_message(err, "error")
        self.clear()

    def sell_product(self):
        name = self.name.get().lower().strip()
        quantity = self.quantity.get()
        product = self.product_exists(name)
        if product and (product.quantity - int(quantity) >= 0):
            self.show_message(f"{quantity} units of {product.name} sold!", "success")
            product.quantity -= int(quantity)
        else:
            self.show_message("Invalid data!", "error")
        self.clear()

    def products_to_screen(self, products):
        self.controller.product_page.textbox.insert("0.0", f"Name\t\tPrice\t\tQuantity\n")
        self.controller.product_page.textbox.insert("end", "*" * 60)
        self.controller.product_page.textbox.insert("end", "\n")
        if products:
            for product in products:
                self.controller.product_page.textbox.insert("end", f"{product.name}\t\t"
                                                                   f"{product.price}\t\t"
                                                                   f"{product.quantity}\n")

    def search_product(self):
        products = self.controller.load()
        name = self.name.get().lower().strip()
        price = self.price.get()
        quantity = self.quantity.get()
        self.clear()
        if name:
            return list(filter(lambda product: product.name == name, products))
        try:
            if price:
                price = float(price)
                return list(filter(lambda product: product.price >= price, products))
        except ValueError as err:
            self.show_message(err, "error")
        if quantity:
            return list(filter(lambda product: int(product.quantity) >= int(quantity), products))

    def update_price(self):
        name = self.name.get().lower().strip()
        product = self.product_exists(name)
        if product:
            try:
                price = float(self.price.get())
                if price > 0:
                    product.price = price
                    self.show_message(f"The price of {name} updated.", "success")
                else:
                    self.show_message("Negative price", "error")
            except ValueError as err:
                self.show_message(err, "error")
        else:
            self.show_message("No such product", "error")
        self.clear()

    def remove_product(self):
        name = self.name.get().lower().strip()
        product = self.product_exists(name)
        products = self.controller.load()
        if product:
            products.remove(product)
            self.show_message(f"{product.name.capitalize()} deleted.", "success")
        else:
            self.show_message("No such product.", "error")
        self.clear()

    def show_message(self, message, message_type):
        if message_type == "success":
            self.message_label.configure(text_color="green")
        elif message_type == "error":
            self.message_label.configure(text_color="red")
        self.message_label.configure(font=("Helvetica", 18, "bold"))
        self.message.set(message)
        self.message_label.after(3000, self.hide_message)

    def hide_message(self):
        self.message.set("")

    def clear(self):
        self.name.set("")
        self.price.set("")
        self.product_quantity_entry.set(0)
        self.product_name_entry.focus()
