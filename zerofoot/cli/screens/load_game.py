import os
import pickle

from .screen import Screen


class LoadGameScreen(Screen):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.save_games = list()
        for i in os.listdir():
            if ".sav" in i:
                self.save_games.append(i)
        if self.save_games:
            print("Welchen Spielstand möchten Sie laden?\n")
            for i in self.save_games:
                print(f"[{self.save_games.index(i)}] {i}")
            try:
                user_input = int(input("\n> "))
                file = self.save_games[user_input]
            except Exception:
                self.__init__(self.parent)
            else:
                self.load_db(file)
                self.clear_screen()
                print(f"'{file}' wird geladen.\n")
                input("Weiter mit beliebiger Taste...")
        else:
            print("Kein Spielstand vorhanden.\n")
            input("Zurück mit beliebiger Taste...")

    def load_db(self, file):
        try:
            with open(f"./{file}", "rb") as file:
                self.parent.db = pickle.load(file)
        except Exception as exception:
            print(exception)
