import json
from os import path

from ...defaults import PROMPT_PREFIX, SCENARIOS_DIR, ENCODING
from ...views.view import View
from ...views.ingame.main import GameMainScreen
from ...core.scenario import Scenario


class NewGameScreen(View):

    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        self.heading = "Wählen Sie ein Szenario"
        self.choose_scenario([
            "de_1965"  # West Germany 1965
            ])

    def choose_scenario(self, available_scenarios: list):
        self.clear_screen()
        self.print_heading(self.heading)
        print("Wo und wann soll das Spiel beginnen?\n\n")
        json_files = []
        for i, scenario in enumerate(available_scenarios):
            filename = f"scenario_{scenario}.json"
            path_to_file = path.join(SCENARIOS_DIR, filename)
            json_files.append(path_to_file)
            with open(path_to_file, "r", encoding=ENCODING) as file:
                scenario = json.load(file)["scenario"]
            print(f"[{i+1}]  {scenario["country"].upper()},"
                  f"{scenario["year"]}\n\n{scenario["description"]}")
        user_input = input(PROMPT_PREFIX).casefold()
        try:
            json_file: str = json_files[int(user_input) - 1]
        except Exception:
            self.choose_scenario(available_scenarios)
        else:
            self.initialize_scenario(Scenario(json_file))

    def initialize_scenario(self, scenario: Scenario):
        self.clear_screen()
        print("Datenbank wird erzeugt...\n\n")
        self.app.create_database(scenario)
        self.choose_club(self.app.database)

    def choose_club(self, database) -> None:
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

    def preview_club(self, club) -> None:
        self.clear_screen()
        self.print_heading(club.name)
        print(club)
        user_input = input("\nSoll es dieser Verein sein? (j/n)")
        if user_input.casefold() in ["j", "ja", "y", "yes"]:
            self.create_user(self.app.database, club)
        elif user_input.casefold() in ["n", "nein", "no"]:
            self.choose_club(self.app.database)
        else:
            self.clear_screen()
            self.preview_club(club)

    def create_user(self, database, club) -> None:
        database.user.club = club
        GameMainScreen(database)
