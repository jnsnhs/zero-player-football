import json

from ..defaults import ENCODING


class Scenario:

    def __init__(self, json_file_path: str) -> None:
        with open(json_file_path, "r", encoding=ENCODING) as file:
            scenario = json.load(file)

        # Country Parameters

        self.COUNTRY_NAME: str = scenario["country_name"]
        self.COUNTRY_CODE: str = scenario["iso_country_code"]
        self.STARTING_DATE: str = scenario["starting_date"]
        self.STARTING_YEAR: int = int(self.STARTING_DATE.split("-")[0])
        self.REGIONS: list[str] = scenario["regions"]
        self.AVG_GOALS_PER_GAME: float = scenario["avg_goals_per_game"]
        self.POINTS_PER_WIN: int = 3

        # Domestic League Parameters

        self.LEAGUES: list[dict] = []
        for league in scenario["leagues"]:
            self.LEAGUES.append({
                "level": league["level"],
                "name": league["name"],
                "regions": league["regions"]
            })

        # Player Parameters

        self.PLAYER_AVG_AGE: int = scenario["player"]["avg_age"]
        self.PLAYER_NATION_CODES: list[str] = \
            scenario["player"]["nationalities"]["iso_codes"]
        self.PLAYER_NATION_WEIGHTS: list[int]

        # Manager Parameters

        self.MANAGER_MIN_AGE: int = scenario["manager"]["age_min"]
        self.MANAGER_AVG_AGE: int = scenario["manager"]["age_avg"]
        self.MANAGER_MAX_AGE: int = scenario["manager"]["age_max"]

        # Referee Parameters

        self.REFEREE_AVG_AGE: int = scenario["referee"]["avg_age"]
