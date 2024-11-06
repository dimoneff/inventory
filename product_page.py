import customtkinter
from PIL import Image


class ProductPage(customtkinter.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # changing fonts
        font_header = ("Helvetica", 18, "bold")
        font_label = ("Helvetica", 16, "bold")
        # font_input = ("Helvetica", 20, "bold")

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

        # Creating the stock image
        image_file = Image.open("img/stock2.png")
        image = customtkinter.CTkImage(image_file, size=(200, 200))
        image_label = customtkinter.CTkLabel(self, text="", image=image)

        # Creating a textbox
        self.textbox = customtkinter.CTkTextbox(self,
                                                height=300,
                                                font=font_label,
                                                wrap="word",
                                                padx=20,
                                                pady=10)
        # self.textbox.tag_config("center", justify="center")

        # Creating the copy right label
        copyright_label = customtkinter.CTkLabel(self,
                                                 text="Copyright (c) 2024 dimoneff@gmail.com "
                                                      "\nAll Rights Reserved.")

        # Creating a button to the product page
        btn = customtkinter.CTkButton(self,
                                      text="Main Page",
                                      font=font_label,
                                      command=self.back_to_main)

        # Placing widgets in the grid
        company_name.grid(row=0,
                          column=0,
                          padx=50,
                          pady=5,
                          columnspan=3,
                          sticky="nwe")
        image_label.grid(row=1, column=3, rowspan=3, padx=(10, 10))
        self.textbox.grid(row=2,
                          column=0,
                          padx=10,
                          pady=10,
                          rowspan=3,
                          columnspan=3,
                          sticky="nsew")
        btn.grid(row=5,
                 column=0,
                 columnspan=3,
                 padx=10,
                 ipady=5,
                 ipadx=10,
                 sticky="w")

        copyright_label.grid(row=6,
                             column=0,
                             columnspan=4,
                             pady=(10, 5),
                             sticky="swe")

    def back_to_main(self):
        self.controller.change_pages("Main Page")
        self.textbox.delete("0.0", "end")
