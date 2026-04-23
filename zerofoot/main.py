from csv import DictReader
from os import path
from datetime import date

from .views.mainmenu.main_menu import MainMenuScreen
from .core.club import Club
from .core.referee import Referee
from .core.league import League
from .core.scenario import Scenario

from .defaults import STATIC_DIR, REFEREE_TO_CLUB_RATIO


class Main:

    def __init__(self) -> None:
        self.database = None

    def run(self) -> None:
        MainMenuScreen(self)

    def create_database(self, year):
        self.database = Database(year)


class User:

    def __init__(self) -> None:
        self.club = None


class Database:

    def __init__(self, scenario: Scenario) -> None:
        self.user: User = User()
        self.starting_date: date = date.fromisoformat(
            scenario.STARTING_DATE)
        self.clubs: list[Club] = self.create_clubs(
            scenario=scenario)
        self.leagues: list[League] = self.create_leagues(
            scenario=scenario,
            clubs=self.clubs)
        self.referees = self.create_referees(
            count=round(len(self.clubs) * REFEREE_TO_CLUB_RATIO),
            scenario=scenario)

    def create_clubs(self, scenario: Scenario) -> list[Club]:
        list_of_clubs = []
        country_code: str = scenario.COUNTRY_CODE
        current_year: int = date.fromisoformat(scenario.STARTING_DATE).year
        file_name = f"clubs_{country_code}_{current_year}.csv"
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

    def create_leagues(
        self,
        scenario: Scenario,
        clubs: list[Club]
    ) -> list[League]:
        leagues = []
        for league in scenario.LEAGUES:
            level = league["level"]
            regions = [i.casefold() for i in league["regions"]]
            participants = [
                club for club in clubs if club.league_level == level and
                club.region in regions]
            leagues.append(League(
                name=league["name"],
                level=league["level"],
                regions=league["regions"],
                clubs=participants
            ))
        return leagues

    def create_referees(self, count: int, scenario: Scenario) -> list[Referee]:
        list_of_referees = []
        for i in range(count):
            list_of_referees.append(Referee(scenario))
        return list_of_referees

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
