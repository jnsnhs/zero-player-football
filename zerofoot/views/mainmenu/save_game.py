from os import listdir
import pickle

from ..view import View


class SaveGameScreen(View):

    def __init__(self, database) -> None:
        super().__init__()
        self.database = database
        self.heading = "Spielstand speichern"
        self.existing_save_games = [i for i in listdir() if ".sav" in i]
        self.save_database(self.enter_filename())

    def enter_filename(self) -> str:
        filename = ""
        while not filename:
            self.clear_screen()
            self.print_heading(self.heading)
            if self.existing_save_games:
                print("\nBestehende Speicherstände:\n")
                for save_file in self.existing_save_games:
                    print(save_file)
            else:
                print("\nNoch keine Speicherstände vorhanden.")
            print("\nGeben Sie einen Dateinamen ein, um das laufende "
                  "Spiel zu speichern.")
            user_input = input(self.PROMPT_PREFIX).strip()
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
            self.print_heading(self.heading)
            print(f"\nDatei „{filename}“ existiert bereits. Soll sie "
                  "überschrieben werden? (j/n)\n")
            user_input = input(self.PROMPT_PREFIX)
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
            print("\nDatei konnte nicht geschrieben werden.")
            print("Weiter mit <ENTER>...")
            input(self.PROMPT_PREFIX)
            self.__init__(self.database)
        else:
            print(f"\n „{filename}“ erfolgreich gespeichert!\n")
            print("Weiter mit <ENTER>...")
            input(self.PROMPT_PREFIX)
