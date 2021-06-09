from . import mode
from .ui import Alerts, loading
import sys
from rich import print
from rich.table import Table
from rich.console import Console
from .db import DB
import time

db = DB()
alerts = Alerts("red")


class AddProduct(mode.Mode):
    def __init__(self, mode, about, theme):
        super().__init__(mode, about, theme)

    def add_product(self):

        company = self.prompt.input("Enter Product Company")
        name = self.prompt.input("Enter Product Name")

        add_product = db.add_product(company, name)
        loading("Adding Product")

        if add_product:
            print("[bold green]Successfully Added")

        else:
            pass


class ViewProduct(mode.Mode):
    def __init__(self, mode, about, theme):
        super().__init__(mode, about, theme)

    def view_product(self):

        self.products = db.get_all_products()
        self.get_all_products(self.products)

        product_id = self.prompt.input("Enter Product ID")
        product = db.get_product(id=product_id)

        print(
            f"[bold blue]\nProduct ID : {product.id}\nCompany : {product.company}\nName : {product.name}\nDate : {product.date}[/bold blue]")

        time.sleep(5)


class ViewAllProducts(mode.Mode):
    def __init__(self, mode, about, theme):
        super().__init__(mode, about, theme)
        self.products = None

        self.table = Table(title=mode, title_justify=self.mode, title_style=self.theme,
                           caption=self.about, caption_justify="left", caption_style=self.theme, padding=(0, 5))
        self.console = Console()


class UpdateProduct(mode.Mode):
    def __init__(self, mode, about, theme):
        super().__init__(mode, about, theme)

    def update_product(self):

        self.products = db.get_all_products()
        self.get_all_products(self.products)

        self.id = self.prompt.input("Enter Product ID Of The Product")

        self.current_product = db.get_product(self.id)

        print(
            f"[bold blue]\nProduct ID: {self.current_product.id}\nCompany: {self.current_product.company}\nName: {self.current_product.name}\nDate: {self.current_product.date}[/bold blue]")

        self.ask = self.prompt.input("Do You Want To Continue (y/n)").lower()

        if self.ask == "y":
            print(
                f"[bold blue]\nProduct ID: {self.current_product.id}\nCompany: {self.current_product.company}\nName: {self.current_product.name}\nDate: {self.current_product.date}[/bold blue]")

            self.company = self.prompt.input("Enter New Company Name")
            self.name = self.prompt.input("Enter New Product Name")

            db.update_product(self.current_product, self.company, self.name)

            loading("Updating Product")

        elif self.ask == "n":
            alerts.warning("Redirecting To Menu")

        else:
            alerts.warning("Invalid Command")


class DeleteProduct(mode.Mode):
    def __init__(self, mode, about, theme):
        super().__init__(mode, about, theme)

    def delete_product(self):

        self.products = db.get_all_products()
        self.get_all_products(self.products)

        self.product_id = self.prompt.input("Enter Product ID")
        self.ask = self.prompt.input(
            f"Do You Want To Delete Product With ID {self.product_id} (y/n)").lower()

        if self.ask == "y":
            product_delete = db.delete_product(self.product_id)
            loading("Deleting Product")

            if product_delete:
                print("[bold green]Successfully Deleted Product")

            else:
                alerts.warning("\nCan't Delete This Product.")

        else:
            pass


def exit():
    sys.exit(0)
