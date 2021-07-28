from rich import print
from rich.table import Table
from .ui import loading
from rich.console import Console
from .ui import Prompt
import time


class Mode():
    def __init__(self, mode, about, theme):
        self.mode = mode
        self.about = about
        self.theme = theme
        self.products = None

        self.table = Table(title=mode, title_justify=self.mode, title_style=self.theme,
                           caption=self.about, caption_justify="left", caption_style=self.theme, padding=(0, 5))
        self.console = Console()

        self.prompt = Prompt(self.theme)

    def get_mode(self):
        """user is required to use this using rich.print"""
        return self.mode

    def get_about(self):
        return self.about

    def mode_details(self):
        print(
            f"[bold yellow]\n{self.mode} Mode[/bold yellow]\n[bold yellow]{self.about}[/bold yellow]")

    def get_all_products(self, products):

        loading("Loading All Products")
        self.products = products
        print()

        self.console.print("All Products\n", justify="left", style="bold red")

        for product in self.products:

            self.data = f"[bold {self.theme}]ID: [bold red]{product.id}\n[bold {self.theme}]Company: [bold red]{product.company}\n[bold {self.theme}]Product: [bold red]{product.name}\n[bold {self.theme}]Date: [bold red]{product.date}\n"
            print(self.data)

        time.sleep(5)
