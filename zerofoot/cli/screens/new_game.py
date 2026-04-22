from ...cli.screens.screen import Screen
from ...cli.ingame.main import GameMainScreen
from...defaults import PROMPT_PREFIX


class NewGameScreen(Screen):

    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        self.heading = "Wählen Sie ein Szenario"
        self.choose_scenario()

    def choose_scenario(self):
        self.clear_screen()
        self.print_heading(self.heading)
        print("Wo und wann soll das Spiel beginnen?\n\n")
        print("[1]  WESTDEUTSCHLAND, 1965\n")
        # print("[2] ITALIEN, 1980\n")
        # print("[3] DEUTSCHLAND, 1995\n\n")
        user_input = input(PROMPT_PREFIX).casefold()
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
        user_input = input(PROMPT_PREFIX)
        try:
            choice = listed_clubs[int(user_input)]
        except Exception:
            self.choose_club(self.app.database)
        else:
            self.preview_club(choice)

    def preview_club(self, club):
        self.clear_screen()
        self.print_heading(club.name)
        print(club)
        user_input = input("Soll es dieser Verein sein? (j/n)")
        if user_input.casefold() in ["j", "ja", "y", "yes"]:
            self.create_user(self.app.database, club)
        elif user_input.casefold() in ["n", "nein", "no"]:
            self.choose_club(self.app.database)
        else:
            self.clear_screen()
            self.preview_club(club)

    def create_user(self, database, club):
        database.user.club = club
        self.clear_screen()
        print(f"Sie sind nun Anhänger von {club.name} und "
              "werden die Geschicke dieses Vereins in der "
              f"Spielzeit {"XXX"} verfolgen.", end="\n\n")
        print("Weiter mit <ENTER>...\n")
        input(PROMPT_PREFIX)
        GameMainScreen(database)
