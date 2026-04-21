from random import gauss, triangular
from ..core.person import Person, Nationality


class Referee(Person):

    def __init__(
            self,
            current_year: int
    ) -> None:
        super().__init__(
            birthyear=self.set_birthyear(current_year),
            nationality=self.set_nationality(current_year)
        )
        self.expertise: int = int(triangular(1, 13, 7))
        self.strictness: int = int(triangular(1, 13, 7))

    def set_birthyear(self, current_year) -> int:
        # if current_year == 1965:
        avg_age = 38
        age = int(gauss(avg_age, 2))
        age = age if age >= 18 else 18
        return current_year - age

    def set_nationality(self, current_year) -> Nationality:
        # if current_year == 1965:
        return Nationality.DE

    def __str__(self) -> str:
        lines = super().__str__()
        lines += f", EXP: {self.expertise}, STR: {self.strictness}"
        return lines
