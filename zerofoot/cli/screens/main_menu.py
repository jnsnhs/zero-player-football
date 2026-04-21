import sys

from .screen import Screen
from .load_game import LoadGameScreen
from .new_game import NewGameScreen


class MainMenuScreen(Screen):

    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        print("Hauptmenü\n")
        print(
            "[1] Neues Spiel starten\n"
            "[2] Altes Spiel fortsetzen\n"
            "[3] Programm beenden\n"
            )
        user_input = input("> ")
        match user_input:
            case "1":
                NewGameScreen(app)
            case "2":
                LoadGameScreen(self.app)
                if self.app.db is None:
                    self.__init__(self.app)
            case "3":
                self.clear_screen()
                print("Programm beendet. Auf Wiedersehen!\n")
                sys.exit(0)
            case _:
                self.__init__(self.app)
