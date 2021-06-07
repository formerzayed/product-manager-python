from scripts.db import DB
from scripts.ui import Menu, Alerts, Prompt, loading
from scripts import AddProduct, ViewProduct, ViewAllProducts, exit

options = ["Add Product", "View Product", "View All Products", "Exit"]
menu_color_scheme = ["red", "magenta", "yellow"]

db = DB()
menu = Menu(color_scheme=menu_color_scheme)

prompt = Prompt("red")
alerts = Alerts("red")

menu.options = options

# Mode Setup
add_product = AddProduct(
    "Add Product", "This is the add product mode", "yellow")
view_product = ViewProduct(
    "View Product", "This is view product mode", "red")
view_all_products = ViewAllProducts(
    "View All Products", "This is view all products mode", "blue")


def main():
    loading()
    menu.menu()
    choice = prompt.input("Enter your choice")

    # Mode = Add Products
    if choice == "1":

        company = prompt.input("Enter Company Name")
        name = prompt.input("Enter Product", new_line=False)

        db.add_product(company=company, name=name)

    # Mode = View A Single Product
    elif choice == "2":
        pass

    # Mode = View all products
    elif choice == "3":
        products = db.get_all_products()

        view_all_products.all_products(products)

    # Mode = Exit
    elif choice == "4":
        exit()

    else:
        pass


if __name__ == "__main__":
    while True:
        main()
