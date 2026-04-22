import os

from ...defaults import PROMPT_PREFIX, SCREEN_WIDTH


class Screen:

    def __init__(self) -> None:
        self.PROMPT_PREFIX = PROMPT_PREFIX
        self.clear_screen()

    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def letter_spacing(self, text: str, spaces: int = 1) -> str:
        result = [char + " " * spaces for char in text]
        return "".join(result)[:-1]

    def print_line(self, char: str = "─", length: int = SCREEN_WIDTH) -> None:
        print(char * length)

    def print_heading(self, text: str) -> None:
        heading = self.letter_spacing(text)
        PADDING = 1
        print()
        print(" " * PADDING + heading.upper() + " " * PADDING)
        # print("─" * (PADDING * 2 + len(heading)), end="\n\n")
        self.print_line()
        print()
