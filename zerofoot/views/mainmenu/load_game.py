from os import listdir
import pickle

from ..view import View
from ..ingame.main import GameMainScreen
from ...defaults import PROMPT_PREFIX


class LoadGameScreen(View):

    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        self.existing_save_games = [i for i in listdir() if ".sav" in i]
        self.filename = self.choose_file()
        self.print_heading("Spielstand laden")

        if not self.existing_save_games:
            print("Kein Spielstand vorhanden.\n")
            print("Zurück mit <ENTER>...")
            input(PROMPT_PREFIX)
        else:
            print("\nWelchen Spielstand möchten Sie laden?\n\n")
            for i in self.existing_save_games:
                print(f"[{self.existing_save_games.index(i)}]  {i}\n")
            try:
                user_input = int(input(PROMPT_PREFIX))
                file = self.existing_save_games[user_input]
            except Exception:
                self.__init__(self.app)
            else:
                self.load_db(file)
                self.clear_screen()
                print(f" „{file}“ wird geladen...\n")
                GameMainScreen(self.app.database)

    def choose_file(self):
        pass

    def load_db(self, file):
        try:
            with open(f"./{file}", "rb") as file:
                self.app.database = pickle.load(file)
        except Exception as exception:
            print(exception)
