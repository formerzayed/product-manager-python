from rich import print
from rich.console import Console
import time
from rich.progress_bar import ProgressBar


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

    def input(self, text, new_line=True):
        if new_line:
            print()

        print(f"[bold {self.color}]{text} : [/bold {self.color}]", end="")
        self.inp = input()

        return self.inp


def loading():
    console = Console()
    bar = ProgressBar(width=100000)
    console.print(bar)
