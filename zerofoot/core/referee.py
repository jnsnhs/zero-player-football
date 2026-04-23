from random import gauss, triangular
from ..core.person import Person, Nationality
from ..core.scenario import Scenario


class Referee(Person):

    def __init__(
            self,
            scenario: Scenario
    ) -> None:
        super().__init__(
            birthyear=self.set_birthyear(scenario.STARTING_YEAR),
            nationality=self.set_nationality(scenario.STARTING_YEAR)
        )
        self.expertise: int = int(triangular(1, 13, 7))
        self.strictness: int = int(triangular(1, 13, 7))

    def set_birthyear(self, current_year) -> int:
        # Für Westdeutschland 1965
        # TODO Von scenario abhängig machen
        avg_age = 38
        age = int(gauss(avg_age, 2))
        age = age if age >= 18 else 18
        return current_year - age

    def set_nationality(self, current_year) -> Nationality:
        # Für Westdeutschland 1965
        # TODO von Scenario abhängig machen
        return Nationality.DE

    def __str__(self) -> str:
        lines = super().__str__()
        lines += f", EXP: {self.expertise}, STR: {self.strictness}"
        return lines
