from os import listdir
import pickle

from ...cli.screens.screen import Screen


class SaveGameScreen(Screen):

    def __init__(self, database) -> None:
        super().__init__()
        self.database = database
        self.existing_save_games = [i for i in listdir() if ".sav" in i]
        self.save_database(self.enter_filename())

    def enter_filename(self) -> str:
        filename = ""
        while not filename:
            self.clear_screen()
            print("Spielstand speichern", end="\n\n")
            if self.existing_save_games:
                print("Bestehende Speicherstände:\n")
                for save_file in self.existing_save_games:
                    print(save_file)
            else:
                print("Noch keine Speicherstände vorhanden.")
            print("\nGeben Sie einen Dateinamen ein, um das laufende "
                  "Spiel zu speichern.\n")
            user_input = input("> ").strip()
            if user_input != "":
                filename = user_input if user_input.endswith(".sav") \
                    else user_input + ".sav"
                if filename in self.existing_save_games and \
                        not self.confirm_overwrite(filename):
                    filename = ""
        return filename

    def confirm_overwrite(self, filename) -> bool:
        while True:
            self.clear_screen()
            print(f"Datei „{filename}“ existiert bereits. Soll sie "
                  "überschrieben werden? (j/n)\n\n")
            user_input = input("> ")
            if user_input in ["j"]:
                return True
            elif user_input in ["n"]:
                return False

    def save_database(self, filename: str) -> None:
        self.clear_screen()
        try:
            with open(f"{filename}", "wb") as file:
                pickle.dump(self.database, file)
        except Exception:
            print("Datei konnte nicht geschrieben werden.")
        else:
            self.clear_screen()
            print(f"Datei „{filename}“ erfolgreich gespeichert!\n")
            input("Weiter mit <ENTER>...")
