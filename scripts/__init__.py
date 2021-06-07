from . import mode
from .ui import loading
import sys
from rich import print
from rich.table import Table
from rich.console import Console


class AddProduct(mode.Mode):
    def __init__(self, mode, about, theme):
        super().__init__(mode, about, theme)


class ViewProduct(mode.Mode):
    def __init__(self, mode, about, theme):
        super().__init__(mode, about, theme)


class ViewAllProducts(mode.Mode):
    def __init__(self, mode, about, theme):
        super().__init__(mode, about, theme)
        self.products = None

        self.table = Table(title=mode, title_justify=self.mode, title_style=self.theme,
                           caption=self.about, caption_justify="left", caption_style=self.theme, padding=(0, 5))
        self.console = Console()

    def all_products(self, products):
        loading()
        print()
        self.products = products

        self.table.add_column("No.", header_style="bold red", style=self.theme)
        self.table.add_column(
            "Company Name", header_style="bold red", style=self.theme)
        self.table.add_column(
            "Product Name", header_style="bold red", style=self.theme)
        self.table.add_column("Date", header_style="bold red",
                              style=self.theme, no_wrap=True)

        for product in self.products:
            self.table.add_row(str(product.id), product.company,
                               product.name, str(product.date))

        self.console.print(self.table)

        loading()


def exit():
    sys.exit(0)
