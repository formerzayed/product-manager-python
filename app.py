from scripts.db import DB
from scripts.ui import Menu, Alerts, Prompt, loading
from scripts import AddProduct, ViewProduct, ViewAllProducts, UpdateProduct, DeleteProduct, exit


options = ["Add Product", "View Product", "View All Products",
           "Update Products", "Delete Products", "Exit"]
menu_color_scheme = ["red", "magenta", "yellow"]

db = DB()
menu = Menu(color_scheme=menu_color_scheme)

prompt = Prompt("red")
alerts = Alerts("red")

menu.options = options

# Mode Setup
add_product = AddProduct(
    "Add Product", "This is the add product mode", "blue")
view_product = ViewProduct(
    "View Product", "This is view product mode", "red")
view_all_products = ViewAllProducts(
    "View All Products", "This is view all products mode", "green")
update_product = UpdateProduct(
    "Update Product", "This is update product mode", "magenta")
delete_product = DeleteProduct(
    "Delete Product", "This is delete product mode", "yellow")


def main():
    loading("Loading Menu")
    menu.menu()
    choice = prompt.input("\nEnter your choice")

    # Mode = Add Products
    if choice == "1":
        loading(f"Loading {view_product.get_mode()} Mode")
        view_product.mode_details()

        add_product.add_product()

    # Mode = View A Single Product
    elif choice == "2":
        loading(f"Loading {view_product.get_mode()} Mode")
        view_product.mode_details()
        view_product.view_product()

    # Mode = View all products
    elif choice == "3":
        loading(f"Loading {view_all_products.get_mode()} Mode")
        view_all_products.mode_details()

        products = db.get_all_products()
        view_all_products.get_all_products(products)

    # Update products mode
    elif choice == "4":
        loading(f"Loading {update_product.get_mode()} Mode")
        update_product.mode_details()
        update_product.update_product()

    # delete_product_mode
    elif choice == "5":
        loading(f"Loading {delete_product.get_mode()} Mode")
        delete_product.mode_details()

        delete_product.delete_product()

    # Mode = Exit
    elif choice == "6":
        loading("Exiting...")
        print()
        exit()

    else:
        pass


if __name__ == "__main__":
    while True:
        main()
