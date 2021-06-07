from rich import print


class Mode():
    def __init__(self, mode, about, theme):
        self.mode = mode
        self.about = about
        self.theme = theme

    def get_mode(self):
        """user is required to use this using rich.print"""
        return f"[bold red]{self.mode}[/bold red]"

    def get_about(self):
        return f"[bold {self.theme}]{self.about}[/bold {self.theme}]"

    def mode_details(self):
        print(
            f"[bold yellow]\n{self.mode} Mode[/bold yellow]\n[bold {self.theme}]{self.about}[/bold {self.theme}]")
