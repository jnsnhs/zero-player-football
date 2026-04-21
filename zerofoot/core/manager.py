from random import triangular

from ..core.person import Person, Nationality
from ..defaults import AVG_GOALS_PER_GAME


class Manager(Person):

    def __init__(
            self,
            current_year: int,
            league_level: int,
            avg_gf: float,
            avg_ga: float
            ) -> None:
        super().__init__(
            birthyear=self.set_birthyear(current_year),
            nationality=self.set_nationality(current_year)
        )
        self.expertise: int = self.set_expertise(league_level, avg_gf, avg_ga)

    def set_birthyear(self, current_year: int) -> int:
        if current_year == 1965:
            manager_age = int(triangular(35, 60, 46))
        return current_year - manager_age

    def set_nationality(self, current_year: int) -> Nationality:
        if current_year == 1965:
            nationality = Nationality.DE
        return nationality

    def set_expertise(self, league_level, avg_gf, avg_ga) -> int:
        effect_avg_gf = avg_gf / (AVG_GOALS_PER_GAME / 2) - 1
        effect_avg_ga = 1 - avg_ga / (AVG_GOALS_PER_GAME / 2)
        effect_total = 1 + (effect_avg_gf + effect_avg_ga) / 2
        match league_level:
            case 1:
                MAX_EXPERTISE = 12
                MEAN_EXPERTISE = 8
                MIN_EXPERTISE = 7
            case 2:
                MAX_EXPERTISE = 7
                MEAN_EXPERTISE = 6
                MIN_EXPERTISE = 5
            case 3:
                MAX_EXPERTISE = 5
                MEAN_EXPERTISE = 4
                MIN_EXPERTISE = 3
            case 4:
                MAX_EXPERTISE = 3
                MEAN_EXPERTISE = 2
                MIN_EXPERTISE = 1
        expertise = round(effect_total * MEAN_EXPERTISE)
        if expertise < MIN_EXPERTISE:
            expertise = MIN_EXPERTISE
        elif expertise > MAX_EXPERTISE:
            expertise = MAX_EXPERTISE
        return expertise

    def __str__(self) -> str:
        lines = f"{super().__str__()}, EXP: {self.expertise}"
        return lines
