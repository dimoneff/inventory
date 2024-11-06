import json

with open("products.txt", "r") as file:
    products = file.readlines()
print(products)
product_name = "milk"
products = [[item.strip() for item in items] for items in [product.split(",") for product in products]]
print(products)
found = list(filter(lambda item: item[0] == product_name, products))
print(found)
# with open("products.txt") as file:
#     products = file.readlines()
# print(products)
# for product in products:
#     product = product.strip()
#     print(product.split(","))

# products = [[item.strip() for item in items] for items in [product.split(", ") for product in products]]
#
#
# print(list(filter(lambda product: product[0] == "milk", products)))

#print(list(filter(lambda product: product["product_name"] == product_name, products)))