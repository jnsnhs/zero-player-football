import os


class Screen:

    def __init__(self) -> None:
        self.clear_screen()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
