from csv import DictReader
from os import path

from .cli.screens.main_menu import MainMenuScreen
from .core.club import Club, Region
from .core.referee import Referee
from .core.league import League
from .core.cup import Cup

from .defaults import STATIC_DIR, REFEREE_TO_CLUB_RATIO


class Main:

    def __init__(self) -> None:
        self.database = None
        self.settings = None
        self.controller = None

    def run(self) -> None:
        # self.database.print_leagues()
        MainMenuScreen(self)
        # print("Spiel wird gestartet mit: \n", self.db)
        # input("any key to quit")
        # self.controller.run()

    def create_database(self, year):
        self.database = Database(year)


class User:

    def __init__(self) -> None:
        self.club = None


class Database:

    def __init__(self, year: int) -> None:
        self.user: User = User()
        self.starting_year: int = year
        self.clubs: list[Club] = self.create_clubs(self.starting_year)
        self.referees = self.create_referees(
            count=round(len(self.clubs) * REFEREE_TO_CLUB_RATIO),
            current_year=self.starting_year)
        self.leagues: list[League] = self.create_leagues(
            year=self.starting_year,
            clubs=self.clubs)
        # self.cup = self.create_cup(self.starting_year, self.clubs)

    def create_clubs(self, current_year: int) -> list[Club]:
        list_of_clubs = []
        file_name = f"clubs_de_{current_year}.csv"
        path_to_file = path.join(STATIC_DIR, "clubs", file_name)
        with open(path_to_file, "r", encoding="utf8") as file:
            raw_club_data = DictReader(file)
            for record in raw_club_data:
                club = Club(
                    current_year=current_year,
                    name=record["name"],
                    avg_gf=float(record["avg_gf"]),
                    avg_ga=float(record["avg_ga"]),
                    league_level=int(record["league_lvl"]),
                    qualified_for_cup=bool(int(record["cup"])),
                    region=record["region"])
                list_of_clubs.append(club)
        return list_of_clubs

    def create_referees(self, count: int, current_year: int) -> list[Referee]:
        list_of_referees = []
        for i in range(count):
            list_of_referees.append(Referee(current_year))
        return list_of_referees

    def create_leagues(self, year: int, clubs: list[Club]) -> list[League]:
        league_data_de_1965 = [
            {"level": 1, "name": "Bundesliga", "clubs": 18,
             "regions": [Region.N, Region.W, Region.SW, Region.S, Region.NE]},
            {"level": 2, "name": "Regionalliga Nord", "regions": [Region.N]},
            {"level": 2, "name": "Regionalliga West", "regions": [Region.W]},
            {"level": 2, "name": "Regionalliga Südwest",
             "regions": [Region.SW]},
            {"level": 2, "name": "Regionalliga Süd", "regions": [Region.S]},
            {"level": 2, "name": "Regionalliga Berlin", "regions": [Region.NE]}
        ]
        leagues = []
        for league in league_data_de_1965:
            level = league["level"]
            participants = [
                club for club in clubs if club.league_level == level and
                club.region in league["regions"]]
            leagues.append(League(
                name=league["name"],
                level=league["level"],
                regions=league["regions"],
                clubs=participants
            ))
        return leagues

    def create_cup(self, year: int, clubs: list[Club]) -> Cup:
        participants = [
            club for club in clubs if club.qualified_for_cup is True]
        cup = Cup(
            name="Vereinspokal",
            clubs=participants
        )
        return cup

    def print_leagues(self) -> None:
        print(f"\nLeagues ({len(self.leagues)})\n")
        for league in self.leagues:
            print(league, end="\n")

    def print_data(self) -> None:
        print(f"\nReferees (n = {len(self.referees)})\n")
        for referee in self.referees[0:3]:
            print(referee)
        print(f"\nClubs (n = {len(self.clubs)})\n")
        for club in self.clubs[0:3]:
            print(club, end="\n\n")
