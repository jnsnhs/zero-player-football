from enum import Enum
from random import choice, choices, gauss, random

from ..core.person import Person, Nationality
from ..defaults import AVG_GOALS_PER_GAME


class Position(Enum):
    GK = 0   # Goalkeeper
    SW = 1   # Sweeper
    LB = 2   # Left Back
    CB = 3   # Center Back
    RB = 4   # Right Back
    DM = 5   # Defensive Midfield
    LM = 6   # Left Midfield
    RM = 7   # Right Midfield
    AM = 8   # Attacking Midfield
    LW = 9   # Left Wing
    RW = 10  # Right Wing
    CF = 11  # Center Forward


class DefPositions(Enum):
    SW = 1
    LB = 2
    CB = 3
    RB = 4


class MidPositions(Enum):
    DM = 5
    LM = 6
    RM = 7
    AM = 8


class OffPositions(Enum):
    LW = 9
    RW = 10
    CF = 11


class Player (Person):

    def __init__(
        self,
        current_year: int,
        league_level: int,
        avg_gf: float,
        avg_ga: float,
        position: Position | None = None
    ) -> None:
        super().__init__(
            birthyear=self.set_birthyear(current_year),
            nationality=self.set_nationality(current_year)
        )
        self.position_main: Position = position if position else \
            self.set_main_position()
        self.position_alt: Position | None = self.set_alt_position(
            self.position_main)
        self.strength: int = self.set_strength(
            avg_gf=avg_gf,
            avg_ga=avg_ga,
            position=self.position_main,
            league_level=league_level
        )
        self.motivation: int = self.set_motivation()

    def set_birthyear(self, current_year) -> int:
        # if current_year == 1965:
        avg_age = 26
        age = int(gauss(avg_age, 2))
        age = age if age >= 18 else 18
        return current_year - age

    def set_nationality(self, current_year: int) -> Nationality:
        if current_year == 1965:
            nationalities = [
                Nationality.DE,
                Nationality.RS,
                Nationality.NL,
                Nationality.AT,
                Nationality.TR
                ]
            # weights of nationalities in german bundesliga of 1963/64!
            weights = (317, 3, 2, 1, 1)
        return choices(nationalities, weights)[0]

    def set_main_position(self) -> Position:
        main_position = choice([
            Position.GK,
            Position.SW, Position.LB, Position.CB, Position.CB, Position.RB,
            Position.DM, Position.AM, Position.LM, Position.RM,
            Position.LW, Position.CF, Position.CF, Position.RW])
        return main_position

    def set_alt_position(self, main_position: Position) -> Position | None:
        # TODO: optimize and refine logic
        alt_position = main_position if random() < 0.25 else False
        if alt_position and main_position != Position.GK:
            while alt_position == main_position:
                if main_position.value in DefPositions:
                    alt_position = choice([
                        Position.SW, Position.LB, Position.CB, Position.RB,
                        Position.DM
                    ])
                elif main_position.value in OffPositions:
                    alt_position = choice([
                        Position.RW, Position.LW, Position.CF, Position.AM
                    ])
                else:
                    alt_position = choice([
                        Position.DM, Position.LM, Position.RM, Position.AM
                    ])
        else:
            alt_position = None
        return alt_position

    def set_strength(self, avg_gf: float, avg_ga: float,
                     position: Position, league_level: int) -> int:
        match league_level:
            case 1:
                MAX_TEAM_STR = 10
                MEAN_TEAM_STR = 8
                MIN_TEAM_STR = 7
            case 2:
                MAX_TEAM_STR = 7
                MEAN_TEAM_STR = 6
                MIN_TEAM_STR = 5
            case 3:
                MAX_TEAM_STR = 5
                MEAN_TEAM_STR = 4
                MIN_TEAM_STR = 3
            case _:
                MAX_TEAM_STR = 3
                MEAN_TEAM_STR = 2
                MIN_TEAM_STR = 1
        if position.value in DefPositions or position == Position.GK:
            exp_str = self.expected_def_strength(
                avg_ga, MIN_TEAM_STR, MEAN_TEAM_STR, MAX_TEAM_STR)
        elif position.value in OffPositions:
            exp_str = self.expected_off_strength(
                avg_gf, MIN_TEAM_STR, MEAN_TEAM_STR, MAX_TEAM_STR)
        else:
            if random() < 0.5:
                exp_str = self.expected_def_strength(
                    avg_ga, MIN_TEAM_STR, MEAN_TEAM_STR, MAX_TEAM_STR)
            else:
                exp_str = self.expected_off_strength(
                    avg_gf, MIN_TEAM_STR, MEAN_TEAM_STR, MAX_TEAM_STR)
        return round(gauss(mu=exp_str, sigma=1))

    def expected_off_strength(self, avg_gf, min_str, mean_str, max_str):
        if avg_gf <= (avg_goals := AVG_GOALS_PER_GAME) / 2:
            exp_str = avg_gf * (mean_str - min_str) / (0.25 * avg_goals) + 6
            exp_str = round(exp_str) if exp_str >= min_str else min_str
        else:
            exp_str = avg_gf * (max_str - mean_str) / (0.25 * avg_goals) + 4
            exp_str = round(exp_str) if exp_str <= max_str else max_str
        return exp_str

    def expected_def_strength(self, avg_ga, min_str, mean_str, max_str):
        if avg_ga <= (avg_goals := AVG_GOALS_PER_GAME) / 2:
            exp_str = avg_ga * (mean_str - max_str) / (0.25 * avg_goals) + 12
            exp_str = round(exp_str) if exp_str <= max_str else max_str
        else:
            exp_str = avg_ga * (min_str - mean_str) / (0.25 * avg_goals) + 10
            exp_str = round(exp_str) if exp_str >= min_str else min_str
        return exp_str

    def set_motivation(self) -> int:
        values = (90, 95, 100, 105, 110)
        weights = (0.05, 0.1, 0.7, 0.1, 0.05)
        return choices(values, weights)[0]

    def __str__(self) -> str:
        lines = super().__str__()
        lines += f", {self.position_main.name}"
        lines += f"/{self.position_alt.name}" if self.position_alt else ""
        lines += f", ST: {self.strength}, MO: {self.motivation}"
        return lines
