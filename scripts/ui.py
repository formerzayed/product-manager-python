from rich import print
from rich.console import Console
import time
from rich.progress import Progress


class Alerts():
    def __init__(self, color):
        self.color = color
        self.warning_text = ""

    def warning(self, text):
        self.warning_text = f"[bold {self.color}]{text}[/bold {self.color}]"
        print(self.warning_text)

        return self.warning_text


class Menu():
    def __init__(self, options=[], color_scheme=["red", "green", "blue"]):
        self.colors = color_scheme
        self.options = options

    def menu(self):
        print(
            f"\n[bold {self.colors[0]}]      MENU      [/bold {self.colors[0]}]")
        print(
            f"[bold {self.colors[0]}]----------------[/bold {self.colors[0]}]")
        for i in range(0, len(self.options)):
            print(
                f"[bold {self.colors[1]}]{str(i+1)}.[/bold {self.colors[1]}]" + f"[bold {self.colors[2]}]{self.options[i]}[/bold {self.colors[2]}]")


class Prompt():
    def __init__(self, color):
        self.color = color

    def input(self, text):

        print(f"[bold {self.color}]{text} : [/bold {self.color}]", end="")
        self.inp = input()

        return self.inp


def loading(text):
    print()
    with Progress() as progress:
        task1 = progress.add_task(f"[blue]{text}...", total=100)

        while not progress.finished:
            progress.update(task1, advance=12)
            time.sleep(0.1)


# def get_all_products(products):
#     loading("Loading All Products")

#     print()
#     products = products

#     table.add_column(
#         "No.", header_style="bold red", style=f"bold {theme}")
#     table.add_column(
#          "Company Name", header_style="bold red", style=f"bold {theme}")
#     table.add_column(
#         "Product Name", header_style="bold red", style=f"bold {theme}")
#     table.add_column("Date", header_style="bold red",
#                             style=f"bold {theme}", no_wrap=True)

#     for product in products:
#         table.add_row(str(product.id), product.company,
#                             product.name, str(product.date))

#     console.print(table)
