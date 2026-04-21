import pickle
import sys
from uuid import uuid4

from ...cli.screens.screen import Screen
from .load_game import LoadGameScreen
from ...cli.screens.new_game import NewGameScreen


class StartScreen(Screen):

    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
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

    def create_db(self):
        unique_id = uuid4()
        self.app.db = unique_id

    def save_db(self):
        try:
            with open("./db.sav", "wb") as file:
                pickle.dump(self.app.db, file)
        except Exception as exception:
            print(exception)
