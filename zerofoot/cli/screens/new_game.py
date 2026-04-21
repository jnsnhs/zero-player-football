from sys import exit

from ...cli.screens.screen import Screen
from ...cli.screens.save_game import SaveGameScreen


class NewGameScreen(Screen):

    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        self.choose_scenario()

    def choose_scenario(self):
        self.clear_screen()
        print("Wählen Sie ein Szenario...\n")
        print("[1] WESTDEUTSCHLAND, 1965\n")
        print("")
        # print("[2] ITALIEN, 1980\n")
        # print("[3] DEUTSCHLAND, 1995\n")
        user_input = input("> ")
        if user_input in ["1"]:
            self.clear_screen()
            print("Datenbank wird erzeugt...\n\n")
            self.app.create_database(1965)
            self.choose_club(self.app.database)
        else:
            self.choose_scenario()

    def choose_club(self, database):
        self.clear_screen()
        print("Westdeutschland, Saison 1965/66\n")
        listed_clubs = []
        for league in database.leagues:
            print(league.name.upper(), end="\n\n")
            for club in league.clubs:
                listed_clubs.append(club)
                print(f"[{listed_clubs.index(club)}] {club.name}")
            print("")
        print("Welchen Verein wollen Sie verfolgen?:\n")
        user_input = input("> ")
        try:
            choice = listed_clubs[int(user_input)]
        except Exception:
            self.choose_club(self.app.database)
        else:
            self.confirm_club_choice(choice)

    def confirm_club_choice(self, club):
        self.clear_screen()
        print(club)
        user_input = input("Soll es dieser Verein sein? (j/n)")
        if user_input.casefold() in ["j", "ja", "y", "yes"]:
            self.create_user(self.app.database, club)
        elif user_input.casefold() in ["n", "nein", "no"]:
            self.choose_club(self.app.database)
        else:
            self.clear_screen()
            self.confirm_club_choice(club)

    def create_user(self, database, club):
        database.user.club = club
        while True:
            self.clear_screen()
            print(f"Sie sind nun Anhänger von {club.name} und "
                  "werden die Geschicke dieses Vereins in der "
                  f"Spielzeit {"XXX"} verfolgen.", end="\n\n")
            print("[1] Spielstand speichern")
            print("[2] Spiel beenden")
            user_input = input("\n> ")
            if user_input == "1":
                SaveGameScreen(database)
            elif user_input == "2":
                exit(0)
